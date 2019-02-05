#!/bin bash

# Scrape the events
python3 eventScraper.py

# Upload to ftp server
echo "Uploading to ftp server, please enter password"
scp eventBriteEvents.json jtoering@fraser.sfu.ca:/home/jtoering/pub_html/eventbrite
echo "Changing permissions of eventbrite file, please enter password"
ssh jtoering@fraser.sfu.ca chmod 644 pub_html/eventbrite/eventBriteEvents.json