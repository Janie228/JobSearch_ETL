from bs4 import BeautifulSoup as bs
import os
import pymongo
import datetime as dt   
import html, csv
import pandas as pd
import math
import JLFileMgr
import requests
import pandas as pd


# Temporary parse html file for ONLY this Job site "'https://www.itsmycareer.com/results?q=Data-Scientist&l=TN'"
def process_file(_reading_file, _passed_list, _user="system_admin", _type="html"):
        # Error handling
    try:   # Create a Beautiful Soup object   
        soup = bs(_reading_file, "lxml") 

        # Examine the results, then determine element that contains sought info
        # results are returned as an iterable list
        results = soup.find_all('div', class_='jobs-heading')

        # Loop through returned results
        for result in results:    

                # Create and add to dictionary
                file_dict = {}

                # Identify and return title of listing
                file_dict["title"] = result.find('a', class_='mh-t').text.strip()
                file_dict["desc"] = result.find('a', class_='text').text.strip()
                job_co = result.find('div', class_='help-block')
                co_loc = job_co.a.text.strip()
                # Identify and return link to listing
                file_dict["base_url"] = "https://www.itsmycareer.com/" + result.a['href']
                # Split company, city, & state into 3 fields
                splitted = co_loc.split('-')
                file_dict["company"] = splitted[0].strip()
                address = splitted[1].split(',')
                file_dict["city"] = address[0].strip()
                file_dict["state"] = address[1].strip()
                file_dict["created_date"] = dt.datetime.today().strftime("%m/%d/%Y")
                file_dict["created_by"] = _user
                # Append dictionary record to list
                _passed_list.append(file_dict)

        return _passed_list
    except Exception as e:
        return e


# Get total pages ONLY for this Job site "'https://www.itsmycareer.com/results?q=Data-Scientist&l=TN'"
def total_page_by_site(_url, _site="www.itsmycareer.com"):
    # if _site == "www.itsmycareer.com":
    # Retrieve 1 page with the requests module and get total pages
    # url = 'https://www.itsmycareer.com/results?q=Data-Scientist&l=TN'
    response = requests.get(_url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup = bs(response.text, 'lxml')
    # print(soup.prettify())

    # Examine the results, then determine element that contains sought info
    # Get total jobs return with # of jobs per page
    pg_results = soup.find_all('div', class_='cont-header')[0].text.strip().replace("\n", "").split("-")[1].replace("   ", "").strip()
    # print(pg_results)
    num_list = pg_results.split(" ")
    # print(num_list)
    per_pg = num_list[0]
    ttl_job = num_list[2]
    # print(f'Jobs/pg: {per_pg}')
    # print(f'total jobs: {ttl_job}')
    ttl_pg =  math.ceil(int(ttl_job)/int(per_pg))  

    return ttl_pg