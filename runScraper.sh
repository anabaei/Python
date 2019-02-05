#!/bin bash

# Set username here
username=jtoering

# Scrape the events
python3 eventScraper.py

# Upload to ftp server
echo "Uploading to ftp server, please enter password"
scp eventBriteEvents.json $username@fraser.sfu.ca:/home/$username/pub_html/eventbrite
echo "Changing permissions of eventbrite file, please enter password"
ssh $username@fraser.sfu.ca chmod 644 pub_html/eventbrite/eventBriteEvents.json