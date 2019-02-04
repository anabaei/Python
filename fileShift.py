import os
import csv
import json
import pandas

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
        json_from_csv = dataframe.to_json(orient="records")
        final_list.append( {input_file_event_id : json_from_csv} )

json.dump(final_list, final_json_file)


