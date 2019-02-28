import os
import datetime as dt   
import html, csv
import pandas as pd
from bs4 import BeautifulSoup  as bs
import math
import requests
import JLFileMgr
from bs4 import BeautifulSoup as bs

# This class provides methods for parsing files, especially "html" for websites
class Parser():
    # 3 requirements to initialize this class object: read_file, base_url, and current_user (default to none).
    # For all the 4 types of methods in this class, some requires additional parameter(s) as followed:
    # ***parse_itsmycareer & parse_indeed: record_List (list of dictionary items)
    # ***clean_data: static method that passes a string of data to be clean
    # ***total_page_by_site: static method that passes a destinated_url

    # A required function to initialize the class object
    def __init__(self, read_file, base_url, current_user=None):
        self.read_file = read_file
        self.base_url = base_url
        self.current_user = current_user

    # Job Parser for "itsmycareer.com"
    def parse_itsmycareer(self, record_List):
        # Create a Beautiful Soup object   
        soup = bs(self.read_file, "lxml") 

        # Examine the results, then determine element that contains sought info
        # results are returned as an iterable list
        results = soup.find_all('div', class_='jobs-heading')

        # Loop through returned results
        for result in results:    
            # Create and add to dictionary
            file_dict = {}

            # Identify and return title of listing
            file_dict["title"] = self.clean_data(result.find('a', class_='mh-t').text)
            file_dict["desc"] = self.clean_data(result.find('a', class_='text').text)
            job_co = result.find('div', class_='help-block')
            co_loc = self.clean_data(job_co.a.text)
            # Identify and return link to listing
            file_dict["web_url"] = self.base_url
            file_dict["job_link"] = self.base_url + result.a['href']
            # Split company, city, & state into 3 fields
            splitted = co_loc.split('- ')      # put space in between hyphen else splitting company name
            file_dict["company"] = self.clean_data(splitted[0])
            address = splitted[1].split(',')
            file_dict["city"] = self.clean_data(address[0])
            if len(address) == 2:
                file_dict["state"] = self.clean_data(address[1])
            else:
                file_dict["state"] = " "
            file_dict["created_date"] = pd.datetime.now().strftime("%m-%d-%Y %I:%M:%S") 
            file_dict["created_by"] = self.current_user

            # Append dictionary record to list
            record_List.append(file_dict)
        return record_List

    # Job Parser for "indeed.com"
    def parse_indeed(self, record_List):
        # Create a Beautiful Soup object   
        soup = bs(self.read_file, "lxml") 

        # Examine the results, then determine element that contains sought info
        # results are returned as an iterable list
        results = soup.find_all('div', class_='jobsearch-SerpJobCard')
        
        for result in results:
            
            file_dict = {}
            link = result.find('a', class_='turnstileLink') 
            file_dict["title"] = self.clean_data(link.text)
            file_dict["desc"] = self.clean_data(result.find('span', class_='summary').text)
            salary_span = result.find('span', class_='salary')
            if salary_span:
                file_dict["salary"] = self.clean_data(salary_span.text)
            else:
                file_dict["salary"] = ""
            
            file_dict["web_url"] = self.base_url
            job_Link = self.clean_data(link.attrs['href']) 
            if "/rc/clk" in job_Link:
                file_dict["job_link"]  = job_Link.replace("/rc/clk", self.base_url + "/viewjob")  # file_dict["job_link"]  
            elif "/pagead/" in job_Link:
                file_dict["job_link"] = job_Link.replace("/pagead/", self.base_url + "/pagead/")   
            else:
                file_dict["job_link"] = f"{file_dict['web_url']}{job_Link}"
            file_dict["company"] = self.clean_data(result.find('span', class_='company').text)
            try:
                location = result.find('div', class_='location').text
            except:
                location = result.find('span', class_='location').text
            address = location.split(', ')
            file_dict["city"] = self.clean_data(address[0])
            if len(address) == 2:
                state_zip = address[1].strip().split(' ')
                if len(state_zip) >= 2:
                    file_dict["state"] = self.clean_data(state_zip[0])
                    file_dict["zipcode"] = self.clean_data(state_zip[1])
                elif len(state_zip) == 1:
                    file_dict["state"] = self.clean_data(state_zip[0])
                    file_dict["zipcode"] =" "
                else:
                    file_dict["state"] = " "
                    file_dict["zipcode"] = " " 
            else:
                file_dict["state"] = " "
                file_dict["zipcode"] = " "       
            file_dict["created_date"] = pd.datetime.now().strftime("%m-%d-%Y %I:%M:%S") 
            file_dict["created_by"] = self.current_user

            # Append dictionary record to list
            record_List.append(file_dict)
        return record_List

    # This function removes all the white space and back slash
    @staticmethod
    def clean_data(data):
        result = data.replace("\\n", "").replace("\n", "").replace("\\", "").strip()
        return result    

    # Get total pages ONLY for this Job site "https://www.itsmycareer.com"
    @staticmethod
    def total_page_by_site(destinated_url):
        # Retrieve 1 page with the requests module and get total pages
        response = requests.get(destinated_url)
        # Create BeautifulSoup object; parse with 'lxml'
        soup = bs(response.text, 'lxml')
        # print(soup.prettify())

        if "itsmycareer.com" in destinated_url:
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

        elif "indeed.com" in destinated_url:
            # Retrieve 1 page with the requests module and get total pages
            # url = "https://www.indeed.com/q-Data-Analyst,-Data-Scientist,-Data-Engineer,-Software-Development-l-NJ-jobs.html"
            response = requests.get(destinated_url)
            # Create BeautifulSoup object; parse with 'lxml'
            soup = bs(response.text, 'lxml')
            # print(soup.prettify())

            pg_results = soup.find('div', id='searchCount').text.strip().split(" ")[3].replace(",", "").strip()
            # print(pg_results)
            per_pg = 10
            ttl_job = pg_results

        # CALCULATE # OF PAGES
        ttl_pg =  math.ceil(int(ttl_job)/int(per_pg)) 
        return ttl_pg