#!/bin bash

# Scrape the events
python3 eventScraper.py

# Convert the csvs in folder to single json
python3 fileShift.py

# Upload to ftp server
