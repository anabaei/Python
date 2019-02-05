import time
import os
import csv
import json
import pandas
import configCredentials
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
## Choose whether or not chrome will run headless
chrome_options.headless = True

## Use the chrome web driver, set the options
driver = webdriver.Chrome(options=chrome_options)
## Set the implicit wait timeout
driver.implicitly_wait(15)

def wait_for_ajax(driver):
    wait = WebDriverWait(driver, 15)
    try:
        wait.until(lambda driver: driver.execute_script('return jQuery.active') == 0)
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    except Exception as e:
        pass

eventBriteLoginUrl = "https://www.eventbrite.com/signin/"
eventBriteMyEventsUrl = "https://www.eventbrite.com/myevents/"
eventBriteUsername = configCredentials.eventBriteUsername
eventBritePassword = configCredentials.eventBritePassword

## Start Selenium Automation

## Get the eventbrite signin page
driver.get(eventBriteLoginUrl)

## Login, send username and click get started for the password field
print("Entering username.")
driver.find_element_by_id("email").send_keys(eventBriteUsername)
driver.find_element_by_css_selector("button[data-automation='signup-submit-button']").click()

## Send password and click the signin button
print("Entering password.")
driver.find_element_by_id("password").send_keys(eventBritePassword)
driver.find_element_by_css_selector("button[data-automation='signup-submit-button']").click()

## Navigate to the myevents page, after a small arbitrary wait to allow the request to go through
time.sleep(2)
print("Navigating to my events page.")
driver.get(eventBriteMyEventsUrl)

## Click the past events tab, make note of how many events there are
driver.find_element_by_css_selector("a.js-past-events-toggle").click()
past_events_num = driver.find_element_by_css_selector("a.js-past-events-toggle > em").text
print("The tab says there are " + past_events_num + " past events.")
driver.find_element_by_css_selector("a.js-show-all-btn").click()
wait_for_ajax(driver)

## Create a list of all the links to the past events
list_of_links = []
past_event_cards = driver.find_elements_by_css_selector("h3.text-medium.event-card__header")
for event_card in past_event_cards:
    link_piece = event_card.find_element_by_css_selector("a")
    list_of_links.append(link_piece.get_attribute('href'))

## Find where the script is currently running, to make the download directory location
script_directory = os.getcwd()
download_directory = script_directory + "/downloaded_files/"

## Create dictionary we can use later to extract the event titles
event_title_dictionary = {}

## Run through the list of links, extract the event ID and use it to navigate to the export page
attendee_link_prefix = "https://www.eventbrite.com/myevent/"
attendee_link_suffix = "/reports/attendee/"
for event_link in list_of_links:
    ## Grab the event id by splitting the link string
    event_id = event_link.split("=")[1]

    ## Folder download configuration
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_directory + event_id}}
    command_result = driver.execute("send_command", params)

    ## Visit the attendee summary page
    attendee_summary_page = attendee_link_prefix + event_id + attendee_link_suffix
    print("Getting CSV from " + attendee_summary_page)
    driver.get(attendee_summary_page)

    wait_for_ajax(driver)

    ## Get the name of the event, taking into account whichever title field has text
    fullpage_event_name = driver.find_element_by_css_selector("div.eds-show-up-md > div > h2").text
    minpage_event_name = driver.find_element_by_css_selector("div.eds-show-down-mn > div > h2").text

    if ( len(fullpage_event_name) > len(minpage_event_name) ):
        event_name = fullpage_event_name
    else:
        event_name = minpage_event_name

    event_title_dictionary[event_id] = event_name

    ## Trigger the download
    driver.find_element_by_css_selector("a[data-download-fmt='csv']").click()

## Close the browser window, but give a second to sleep so downloads can finish 
time.sleep(1)
print("Finished scraping, closing.")
driver.quit()

## File rename portion

current_path = os.getcwd()
path_to_csvs = current_path + '/downloaded_files'
final_json_file_name = 'eventBriteEvents.json'
final_json_file = open(final_json_file_name, 'w')

## rename the csv to the name of the folder, then move it out
for root, dirs, files in os.walk(path_to_csvs):
    ## If we are not in the root folders directory
    if (root != path_to_csvs):
        current_filepath = root + '/' + files[0]
        print("Renaming: " + current_filepath)
        ## Move the csv out of the folder and rename it
        os.rename(current_filepath, root + '.csv')
        os.rmdir(root)

## convert to json
final_list = []
for root, dirs, files in os.walk(path_to_csvs):
    for file in files:
        input_file_event_id = file.split('.')[0]
        dataframe = pandas.read_csv(path_to_csvs + '/' + file)
        cleaned_dataframe = dataframe.fillna('')
        dataframe_dict = cleaned_dataframe.to_dict(orient="records")
        final_list.append( {"eventId" : input_file_event_id, "eventName": event_title_dictionary[input_file_event_id], "attendeeData" : dataframe_dict} )

json.dump(final_list, final_json_file)

