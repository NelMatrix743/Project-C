###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.username = NelMatrix743                                   #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

import os 
import string 
import random 
import time 
import venv 
import sqlite3 as  sql 
from datetime import datetime 
from git import Repo 
from display import * 


# Characters used in forming a project ID
VALID_ID_CHARACTERS: str = string.ascii_letters + string.digits

class Project():
    
    def __init__(self, name):
        self.name: str = name 
        self.p_uid: str = Project.generate_project_uid()
        self.description: str | None = None
        self.creation_datetime: dict[str, str] = Project.retrieve_datetime()
        self.status: str | None = None
        self.full_path: str = None

    def generate_project_uid() -> str:
        """ Generate a unique ID of 20 characters """
        return ''.join([random.choice(VALID_ID_CHARACTERS) for ch in range(20)])

    def retrieve_datetime():
        date_list: list[str] = ["YEAR", "MONTH", "DAY", "TIME"]
        date_str: str = datetime.now().strftime("%Y %B %A %X")
        date_dict: dict[str, str] = dict(zip(date_list, date_str.split()))
        return date_dict
    
# end of Project()