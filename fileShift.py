import os

current_path = os.getcwd()
path_to_csvs = current_path + '/downloaded_files'

for dirName, subDirList, fileList in os.walk(path_to_csvs):
    print(fileList)

