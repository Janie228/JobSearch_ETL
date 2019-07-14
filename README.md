# Job Search ETL
-----
Scrape current jobs in a specific location on two websites, itsmycareer.com and/or indeed.com, and analyze job market by  comparing to government's data on employment by occupation, state, and year to get an overview on the job market and payscale. Development still in progress.
 
# Technologies Used

Visual Studio Code, Python 3.6+, Jupyter Notebook, MongoDB, chrome driver, pandas, Beautiful Soup, Browser (splinter) 


# Snippet Process
Janie's Data Science job data munging and analysis for Tennessee 2019.  

* Scrape websites, "https://www.indeed.com" and "https://www.itsmycareer.com", for current jobs and save each webpage as html file
* Read each html file, format, and store data into MongoDB job database
* Download excel file from "https://www.bls.gov" for employment by occupation and state
* Read the excel files into dataframe, munge the dataset and merge with US population by state
* Load the formatted job employment data to MongoDB job database
* Select the desired columns from MongoDB and read back to dataframe for analysis
* Save result dataset into excel sheet in Output directory

# MongoDB Job_DB

![Jobs.JPG](Images/Jobs.JPG)

![Employment.JPG](Images/Employment.JPG)

![Population.JPG](Images/Population.JPG)

# Files
Job_Cleaning_Loading_MongDB.ipynb and Job_Analysis_MongoDB.ipynb Files display the coding process with reusable classes JLFileMgr.py, JLScraper.py, & JLParser.py 

