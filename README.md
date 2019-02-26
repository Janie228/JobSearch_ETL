# Project_II_ETL                                                                                                    Jane Wallace
Mongo &amp; Web Scraping                                                                                             2/21/2019

## Janie's Data Science Job Data Munging & Analysis for Tennessee 2017
----
* Scrape the website, "https://www.indeed.com", for current jobs and save each webpage as html file
* Read each html file and store formatted data into MongoDB job database
* Download excel file from "https://www.bls.gov" for employment by occupation and state
* Read the excel files into dataframe, munge the dataset and merge with US population by state
* Load the formatted job employment data to MongoDB job database
* Select the desired columns from MongoDB and read back to dataframe for analysis
* Save result dataset into excel sheet in Output directory

## Jobs_Munging.ipynb File display the process with classes JLFileMgr.py, JLScraper.py, & JLParser.py
MongoDB Job_DB

![Jobs.JPG](Images/Jobs.JPG)

![JEmployment.JPG](Images/Employment.JPG)

![Population.JPG](Images/Population.JPG)
