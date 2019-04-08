#!/bin bash

# Set username here
#username=anabaei

# Set ftp directory here
#directory=pub_html/eventbrite/

# Scrape the events
python3 eventScraper.py

# Upload to ftp server
#echo "Uploading to ftp server, please enter password"
#scp eventBriteEvents.json $username@fraser.sfu.ca:/home/${username}/${directory}
#echo "Changing permissions of eventbrite file, please enter password"
#ssh $username@fraser.sfu.ca chmod 644 ${directory}eventBriteEvents.json
cp eventBriteEvents.json  /Users/amirnabaei/Desktop/sites/server_salesforce_scrapper/server_auth
echo "Finished. Combined json file should be in https://sfu.ca/~${username}/eventbrite/eventBriteEvents.json"
