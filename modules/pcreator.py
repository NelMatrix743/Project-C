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
            
    
    def create_main_dir(project_path: str) -> None:
        Path.mkdir(project_path)
            

    def create_gitignore_file(project_path: str) -> None: # .gitignore
        GITIGNORE_CONTENT: str = ".venv/\n.INFO"
        with Path(project_path, ".gitignore").open('w') as file:
             file.write(GITIGNORE_CONTENT)
    
    
    def create_venv(project: Project) -> None: # .venv
        venv.create(str(Path(project.full_path, ".venv")), prompt=project.venv_prompt, with_pip=True)
    

    def create_git_repo(project_path: str) -> None: # .git
        pass

    
    def create_requirement_file(project_path: str) -> None: # requirements.txt
        Path(project_path, "requirements.txt").touch()
    
    
    def create_readme_file(project_path: str) -> None: # README.md
        Path(project_path, "README.md").touch()
    
    
    def create_setup_file(project_path: str) -> None: # setup.py
        Path(project_path, "setup.py").touch()
    
    
    def create_license_file(project_path: str) -> None: # LICENSE.md or LINCENSE.txt
        Path(project_path, "LICENSE").touch()


    def create_dunder_main_file(project_path: str) -> None: # __main__.py
        Path(project_path, "__main__.py").touch()
    

    def create_main_file(project_path: str) -> None: # main.py
        Path(project_path, "main.py").touch()


    def create_dunder_init_file(project_path: str) -> None: # __init__.py
        Path(project_path, "__init__.py").touch()
    
    
    def create_toml_file(project_path: str) -> None: # pyproject.toml
        Path(project_path, "pyproject.toml").touch()
    
    
# end of ProjectCreator()