import os
import sys
import re
import csv
import zipfile
import pandas as pd
import shutil
import JLParser


# Read all files in destinated directory and return the formatted data depending on type of file
# Input data: file directory path, type of file, user who call this function
# Output data: formatted data in list 
# * Directory default to current
# * File type default to html
# * User default to system admin 
def read_all_files(_dir_path=os.getcwd(), _type="html", _user="system_admin"):      
    # Error handling
    try:
        # Read all files to list
        xList = [x for x in os.listdir(_dir_path)]
        # Create list to store dictionary data
        read_data = []
            
        # Loop thru each file in list
        for file in xList:
            with open(os.path.join(".", _dir_path, file)) as rfile:
                reading_file = rfile.read()
                read_data =  JLParser.process_file(reading_file, read_data, _user, _type)
            print(read_data)
        # Return success message and url, else return error message
        return read_data
    except Exception as e:
        return e   


# This function check directory file to see if exit.
# *If exist return true, else false
# *If not exist and type is "c", create directory and return true
# *If exit and type is "d", delete direcotory and return false 
def check_dir(_dir_path, _type=None):
   
    if os.path.exists(_dir_path):
        exist = True
    else:
        exist = False
        
    if _type == "c":
        if not exist:
            os.makedirs(_dir_path)
        return True
    elif _type == "d":
        if exist:
            shutil.rmtree(_dir_path)
        return False
    else:
        return True
