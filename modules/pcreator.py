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
import pyperclip
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
    
    def create_project(project: Project, project_type: ProjectType):
        ConfigurationDatabase.load_configuration()
        project.full_path = Path(ConfigurationDatabase.CONFIG["Reservoir Path"]) / project.parsed_name
        ProjectCreator.__create_main_dir(project.full_path)
        # Common files and directories for both types of projects:
        InfoContentManager.create_info_data_file(project) # .INFO
        ProjectCreator.__create_gitignore_file(project.full_path)
        ProjectCreator.__create_readme_file(project.full_path)
        ProjectCreator.__create_requirement_file(project.full_path)
        ProjectCreator.__create_venv(project)
        ProjectCreator.__create_git_repo(project.full_path)
        match project_type:
            case ProjectType.LIGHTWEIGHT:
                ProjectCreator.__create_main_file(project.full_path)
            case ProjectType.HEAVYWEIGHT:
                ProjectCreator.__create_dunder_main_file(project.full_path)
                ProjectCreator.__create_setup_file(project.full_path)
                ProjectCreator.__create_license_file(project.full_path)
                ProjectCreator.__create_toml_file(project.full_path)
                ProjectCreator.__create_modules_dir(project.full_path)
                ProjectCreator.__create_dunder_init_file(str(Path(project.full_path, "modules")))
            case _:
                return # Exit the method
        pyperclip.copy(f"\"{project.full_path}\"") # Automatically copies the project path to clipboard
            
    
    def __create_main_dir(project_path: str) -> None:
        # Throws an error when the directory already exist
        Path.mkdir(project_path)
            

    def __create_gitignore_file(project_path: str) -> None: # .gitignore
        GITIGNORE_CONTENT: str = ".venv/\n.INFO\n"
        with Path(project_path, ".gitignore").open('w') as file:
             file.write(GITIGNORE_CONTENT)
    
    
    def __create_venv(project: Project) -> None: # .venv
        venv.create(str(Path(project.full_path, ".venv")), prompt=project.venv_prompt, with_pip=True)
    

    def __create_git_repo(project_path: str) -> None: # .git
        Repo.init(project_path)

 
    def __create_modules_dir(project_path: str) -> None:
        Path(project_path, "modules").mkdir()
        
        
    def __create_test_dir(project_path: str) -> None:
        Path(project_path, "test").mkdir()
 
    
    def __create_requirement_file(project_path: str) -> None: # requirements.txt
        Path(project_path, "requirements.txt").touch()
    
    
    def __create_readme_file(project_path: str) -> None: # README.md
        Path(project_path, "README.md").touch()
    
    
    def __create_setup_file(project_path: str) -> None: # setup.py
        Path(project_path, "setup.py").touch()
    
    
    def __create_license_file(project_path: str) -> None: # LICENSE.md or LINCENSE.txt
        Path(project_path, "LICENSE").touch()


    def __create_dunder_main_file(project_path: str) -> None: # __main__.py
        Path(project_path, "__main__.py").touch()
    

    def __create_main_file(project_path: str) -> None: # main.py
        Path(project_path, "main.py").touch()


    def __create_dunder_init_file(project_path: str) -> None: # __init__.py
        Path(project_path, "__init__.py").touch()
    
    
    def __create_toml_file(project_path: str) -> None: # pyproject.toml
        Path(project_path, "pyproject.toml").touch()
    
        
    
if __name__ == "__main__":

    # Test
    test_project: Project = Project("Hello World", description="A simple hello world program.")
    match int(input("Project type: 0 or 1: ")):
        case 0:
            ProjectCreator.create_project(test_project, ProjectType.LIGHTWEIGHT)
        case 1:
            ProjectCreator.create_project(test_project, ProjectType.HEAVYWEIGHT)
    print("Project created successfully!")
    
# end of ProjectCreator()