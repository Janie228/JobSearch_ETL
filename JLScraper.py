import os
from splinter import Browser
from bs4 import BeautifulSoup  as bs
import datetime as dt   
import html, csv
import pandas as pd
import time
import JLFileMgr as fm

# This scraper download webpages and stores as html files in destinated path
#### * Input parameters: result searched url, # of pages total, local path for html files, partial name of files, 
####   the browser driver path, and application pause time (seconds)
#### * Output results: return success with the destinated url and html files in destinated path, or error messages.
#### * Currently only support Chrome browser

# This function initialize and return Chrome browser 
def init_browser(_driver_path):
    executable_path = {"executable_path": _driver_path}
    browser = Browser("chrome", **executable_path, headless=False)

    return browser

# This function scrape the webpages and save as html files
# Html file name: #, date, time (hour, minutes, seconds), file name
# Driver path default to current path & driver name
# File directory default to current directory
# Total pages default to 1
# Sleep time default to 1 second
def scrape(_url, _file_name, _ttl_pgs=1, _dir_path=os.getcwd(), _sleep_time=0, _driver_path=os.getcwd()+"/chromedriver"):
    _ttl_pgs = _ttl_pgs + 1
    
    # Error handling
    try:
        # Initialize browser and browse provided website
        browser = init_browser(_driver_path)
        browser.visit(_url)
        # Pause process for # seconds default to 1
        time.sleep(_sleep_time)

        # Loop through each web page and save as html file in destinated directory
        for x in range(1, _ttl_pgs):
            # Browse webpage
            html = browser.html
            soup = bs(html, 'html.parser')
            fm.check_dir(_dir_path)

            # Concatenate file path
            output_path = os.path.join(".", _dir_path, str(x) + "_" + dt.datetime.today().strftime("%m-%d-%Y_%H%M%S")  + "_" + _file_name + ".html")

            # Open file in destinated path and write to it
            with open(output_path, "w") as file:
                file.write(str(soup.encode("utf-8")))
            
            # Check looping if iteration meet maximum, quit if met, else continue looping
            if x == (_ttl_pgs - 1):
                browser.quit()
            else:
                browser.click_link_by_partial_text('Next')
           
        # Return success message and url, else return error message
        return "Successfully scrape : " + _url
    except Exception as e:
        return e 