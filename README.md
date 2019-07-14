# Job Search ETL
-----
Scrape current jobs in a specific location on two websites, itsmycareer.com and/or indeed.com, and analyze job market by  comparing to government's data on employment by occupation, state, and year to get an overview on the job market and payscale. Development still in progress.
 
# Technologies/Libraries Used
-----
Visual Studio Code, Jupyter Notebook, Python 3.6+, Pandas, Mongo, chromedriver
-----
os, sys, re, csv, datetime, html, time, zipfile, shutil, math, requests, Browser (splinter), BeautifulSoup, pandas, pymongo, numpy


## Janie's Data Science Job Data Munging & Analysis for Tennessee 2017.  Steps in the snippet as followed:
-----
* Scrape websites, "https://www.indeed.com" and "https://www.itsmycareer.com", for current jobs and save each webpage as html file
* Read each html file, format, and store data into MongoDB job database
* Download excel file from "https://www.bls.gov" for employment by occupation and state
* Read the excel files into dataframe, munge the dataset and merge with US population by state
* Load the formatted job employment data to MongoDB job database
* Select the desired columns from MongoDB and read back to dataframe for analysis
* Save result dataset into excel sheet in Output directory

## Job_Cleaning_Loading_MongDB.ipynb and Job_Analysis_MongoDB.ipynb Files display the process with reusable code classes JLFileMgr.py, JLScraper.py, & JLParser.py 
------
MongoDB Job_DB

![Jobs.JPG](Images/Jobs.JPG)

![Employment.JPG](Images/Employment.JPG)

![Population.JPG](Images/Population.JPG)
