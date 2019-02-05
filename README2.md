# Scrape event CSVs from EventBrite with Python3 and Selenium

## Before running
- Python3 must be installed
- If not for mac you can `brew postinstall python3`
- if not working and gets error `Permissions issue when linking python3` use
```python
sudo mkdir /usr/local/Frameworks
sudo chown $(whoami):admin /usr/local/Frameworks
```
- Chrome must be installed
- Selenium must be installed, use: `pip3 install selenium`
- Pandas (python3 data library) must be installed, use `pip3 install pandas`
- Chromedriver must be in PATH, visit `https://sites.google.com/a/chromium.org/chromedriver/downloads`, download it and then place it into `usr/bin` or `usr/local/bin`.

## How to run
- Create a copy of `configCredentials.py.example`, fill it with the proper EventBrite details, then rename it to `configCredentials.py`
- Modify the username and directory variable in `runScraper.sh`
- Use `bash runScraper.sh` to collect the CSVs, process them and upload the combined json file to ftp server.

