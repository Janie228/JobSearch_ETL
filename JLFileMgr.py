import os
import sys
import re
import csv
import zipfile
import pandas as pd
import shutil
import JLParser as ps

# This class provides methods for file manipulation
class FileMgr():

    # 3 requirements to initialize this class object: source_path (default to current directory), action_type (default to none), and current_user (default to none).
    # For all the 3 types of methods in this class, additional requirements must met as followed:
    # ***check_dir: OPTINAL action_type ("c: creation" or "d: deletion" on directory)
    # ***move_file: action_type ("all" or "like"), destination_path, OPTIONAL like_criteria in a file name
    # ***reall_all_files: action_type ("html" for now), web_url (base web url), and current user
    def __init__(self, source_path=os.getcwd(), action_type=None, current_user=None):
        self.source_path = source_path
        self.action_type = action_type
        self.current_user = current_user

    # Read all files in source directory and return the formatted data depending on type of file
    # Input data: file directory path, type of file, user who call this function
    # Output data: formatted data in list 
    def read_all_files(self, base_url):      
        # Error handling
        try:
            # Read all files to list
            xList = [x for x in os.listdir(self.source_path)]
            # Create list to store dictionary data
            record_list = []
                
            # Loop thru each file in list
            for x in xList:
                # print(x)
                with open(os.path.join(".", self.source_path, x)) as rfile:
                    read_file = rfile.read()
                    # print(os.path.join(".", self.source_path, x))
                    # Process file based on action_type
                    if self.action_type == "html": 
                        parse = ps.Parser(read_file, base_url, self.current_user)

                        # Process file based on web_url
                        if "itsmycareer" in base_url:
                            record_list =  parse.parse_itsmycareer(record_list)
                        elif "indeed" in base_url:       
                            record_list =  parse.parse_indeed(record_list)

            # print(record_list)
            # Return dictionary data list if successful, else error
            return record_list
        except Exception as e:
            return e   


    # This function check directory file to see if exit.
    # *If exist return true, else false
    # *If not exist and type is "c", create directory and return true
    # *If exit and type is "d", delete direcotory and return false 
    def check_dir(self):
    
        if os.path.exists(self.source_path):
            exist = True
        else:
            exist = False
            
        if self.action_type == "c":
            if not exist:
                os.makedirs(self.source_path)
            return True
        elif self.action_type == "d":
            if exist:
                shutil.rmtree(self.source_path)
            return False
        else:
            return exist


    # Move all files or all files that met criteria from source to destination dirctory 
    def move_file(self, destination_path, like_criteria = None):      
        # Get all file from source
        xList = [x for x in os.listdir(self.source_path)]
        files = []

        if xList:
           if self.check_dir() == False:
               return f"Missing destination path."

        # Loop thru each file and move to destination
        for x in xList:
            if self.action_type == "all":
                shutil.move(self.source_path + "/" + x, destination_path)
                files.append(x)
            else:
                if like_criteria in x:
                    shutil.move(self.source_path + "/" + x, destination_path)
                    files.append(x)
        # Return success msg with all files  
        return f"Successfully moved these files: {files}!"



