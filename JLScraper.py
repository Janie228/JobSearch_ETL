import os
from splinter import Browser
from bs4 import BeautifulSoup  as bs
import datetime as dt   
import html, csv
import pandas as pd
import time
import JLFileMgr as fm
import JLParser as ps

# This scraper download webpages and stores as html files in destinated path
#### * Input parameters: result searched url, # of pages total, local path for html files, partial name of files, 
####   the browser driver path, and application pause time (seconds)
#### * Output results: return success with the destinated url and html files in destinated path, or error messages.
#### * Currently only support Chrome browser
class Scraper():
    # A required function to initialize the class object
    def __init__(self, web_url, file_name, ttl_pgs=1, dir_path=os.getcwd(), sleep_time=0, driver_path=os.getcwd()+"/chromedriver"):
        self.web_url = web_url
        self.file_name = file_name
        self.ttl_pgs = ttl_pgs        
        self.dir_path = dir_path        
        self.sleep_time = sleep_time
        self.driver_path = driver_path

    # This function initialize and return Chrome browser 
    def init_browser(self):
        executable_path = {"executable_path": self.driver_path}
        browser = Browser("chrome", **executable_path, headless=False)
        return browser

    # This function scrape the webpages and save as html files
    # Html file name: #, date, time (hour, minutes, seconds), file name
    # Driver path default to current path & driver name
    # File directory default to current directory
    # Total pages default to 1
    # Sleep time default to 1 second
    def scrape(self):
        # Get total page base on web_url
        if "indeed.com" in self.web_url:
            self.ttl_pgs = ps.Parser.total_page_by_site(self.web_url)
            # print(self.ttl_pgs)
        elif "itsmycareer.com" in self.web_url:
            self.ttl_pgs = ps.Parser.total_page_by_site(self.web_url)

        self.ttl_pgs = self.ttl_pgs + 1

        # Error handling
        try:
            if fm.FileMgr(self.dir_path, "c").check_dir():
                # Initialize browser and browse provided website
                browser = self.init_browser()
                browser.visit(self.web_url)
                # Pause process for # seconds default to 1
                time.sleep(self.sleep_time)

                # Loop through each web page and save as html file in destinated directory
                for x in range(1, self.ttl_pgs):
                    # Browse webpage
                    html = browser.html
                    soup = bs(html, 'html.parser')


                    # Concatenate file path
                    output_path = os.path.join(".", self.dir_path, str(x) + "_" + dt.datetime.today().strftime("%m-%d-%Y_%H%M%S")  + "_" + self.file_name + ".html")

                    # Open file in destinated path and write to it
                    with open(output_path, "w") as file:
                        file.write(str(soup.encode("utf-8")))
                    
                    # Check looping if iteration meet maximum, quit if met, else continue looping
                    if x == (self.ttl_pgs - 1):
                        browser.quit()
                    else:
                        browser.click_link_by_partial_text('Next')
                            
                # Return success message and url, else return error message
                return "Successfully scrape : " + self.web_url
            else:
                return "Please make sure directory exist."

        except Exception as e:
            return e 