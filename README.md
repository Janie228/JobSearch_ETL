# Job Search Analysis                                                                 
-----
## Purpose:
To meet the project requirements stated in Instruction folder and to help job seekers have a glimpse of the job market and payscale, I choose to do web scraping on two websites for specific job(s) in specific location(s), and analyzing these data in relation to government employment dataset by occupation, state, and year. 

---
---

## Results of Data Science Jobs Analysis for NJ & TN  
* MongoDB Job_DB Snapshots

![Jobs.JPG](Images/Jobs.JPG)

![Employment.JPG](Images/Employment.JPG)

![Population.JPG](Images/Population.JPG)

* Output folder excel files
* Datatable results in script file: Job_Analysis_MongoDB.ipynb

---

## Technologies Used
Visual Studio Code, Python, Jupyter Notebook, MongoDB, chrome driver, pandas, Beautiful Soup, Browser (Splinter) 

---

## Installation/Setup
* Clone this repo to your computer
* Make sure all the technologies above are installed and use Python 3+ 
* Open these 2 files in jupyter notebook:
  1) Job_Cleaning_Loading_MongDB.ipynb
  2) Job_Analysis_MongoDB.ipynb
* Make sure the criteria for the search and chrome driver path (see image below) are customized and updated in Job_Cleaning_Loading_MongDB.ipynb before running the script
![Setup.JPG](Images/Setup.JPG)
* Update the appropriate codes in Job_Analysis_MongoDB.ipynb if a lot of changes are made in the above file

---

## Workflow Process
* Scrape websites, "https://www.indeed.com" and "https://www.itsmycareer.com", for current jobs and save each webpage as html file
* Read each html file, format, and store data into MongoDB job database
* Download excel file from "https://www.bls.gov" for employment by occupation and state
* Read the excel files into dataframe, clean, format and merge with US population by state, and load to job database
* Select the desired columns from MongoDB and read back to dataframe for analysis
* Save result dataset into excel sheet in Output directory

---

## :warning: Important Notes
* If the scraping web urls (itsmycareer & indeed) changed, code in the three .py scripts need to be updated.

-----

#### Copyright
© 2019 Janie. All Rights Reserved.


