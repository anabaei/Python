# Scrape event CSVs from EventBrite with Python3 and Selenium

## Before running
- Python3 must be installed
- Chrome must be installed
- Selenium must be installed, use: `pip3 install selenium`
- Pandas (python3 data library) must be installed, use `pip3 install pandas`
- Chromedriver must be in PATH, visit `https://sites.google.com/a/chromium.org/chromedriver/downloads`, download it and then place it into `usr/bin` or `usr/local/bin`.

## How to run
- Create a copy of `configCredentials.py.example`, fill it with the proper EventBrite details, then rename it to `configCredentials.py`
- Use `python3 eventScraper.py` to collect the CSVs from EventBrite.  They will be placed in the created folder `downloaded_files`, under another directory with the event ID as the name.
- (In progress, not yet complete) Use `python3 fileShift.py` to move all the CSVs out from the directories and rename them to the eventID from the directory.

