###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################
import os 
import string 
import random 
import time 
import venv 
import sqlite3 as  sql
from enum import Enum 
from git import Repo 
from display import *
from pathlib import Path 
from datetime import datetime 
from project import Project
from databases import ProjectDatabase, TemplateDatabase, InfoContentManager, ConfigurationDatabase


class ProjectType(Enum):
    LIGHTWEIGHT: str  = "lightweight"
    HEAVYWEIGHT: str  = "heavyweight"



class ProjectCreator(): 
# Create two types of project codebases:
# Lightweight (lw) - Simple codebase structure with base files and directories like requirements.txt, README.md, test directory, etc.
# Heavyweight (hw) - Complex, fully documented codebase structure with more files and directories such as setup.py, LICENSE.md, docs directory, etc.
 
    def __init__(self):
        # work on this
        pass
    
    
    def create_project(project: Project, project_type: ProjectType):
        ConfigurationDatabase.load_configuration()
        project.full_path = Path(ConfigurationDatabase.CONFIG["Reservoir Path"]) / project.parsed_name
        ProjectCreator.create_main_dir(project.full_path)
        InfoContentManager.create_info_data_file(project) # .INFO
        match project_type:
            case ProjectType.LIGHTWEIGHT:
                pass
            case ProjectType.HEAVYWEIGHT:
                pass
            case _:
                return
            
    
   
    
    
# end of ProjectCreator()