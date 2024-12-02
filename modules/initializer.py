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
from display import *
from pathlib import Path
from datetime import datetime
from rich.panel import Panel
from rich.console import Console
from databases import ConfigurationDatabase, ProjectDatabase


class Initializer():
# Create Configuration database and its contents
# Create Project database and its contents

    terminalController: Console = Console()

    def initialize_project_C():
        with Initializer.terminalController.status("Initializing project-C..."):
            time.sleep(5) # 5 seconds delay
            #TODO: Check if the Databases directory and the config.db file has been created and intitialized.          
            #TODO: Throw an error message to the user to let them know that project-C has already been initialized
            #TODO: If not found, create config.db and complete the remaining setup process
            database_directory_path: Path = Path("../Databases").resolve()
            projectc_config_path: Path = Path("../Databases/config.yaml").resolve()
            projects_database_path: Path = Path("../Databases/project").resolve()
            time.sleep(2)
            if not database_directory_path.exists():
                database_directory_path.mkdir()
                time.sleep(3)
                Initializer.terminalController.print("Databases directory created!")
            if not projectc_config_path.exists():
                time.sleep(3)
                ConfigurationDatabase.create_database()
                Initializer.terminalController.print("Configuration file created!")
            if not projects_database_path.exists():
                time.sleep(3)
                ProjectDatabase.create_database()
                Initializer.terminalController.print("Project Databases created!")
            


    def display_welcome_message() -> None:   
        welcome_message: str = str.join('', 
        ["[italic bright_yellow]Project-C (Fully known as Project-Creator) is your go-to CLI tool ", 
        "for creating and managing Python projects effortlessly from the command line. ",
        "With Project-C, you can customize your project setup by selecting the files and directories you want to include ",
        "like README files,__init__ files,test directories, and more. It also offers built-in support for setting up git repositories ",
        "and Python virtual environments automatically — unless you prefer to handle those yourself. ",
        "You can go as far as viewing detailed information about a project, and deleting an entire projects if deemed neccessary. Whether you're starting a new project, ",
        "managing existing ones, or cleaning up, Project-C is here to streamline the process. [bold blink]Happy coding![/][/]"])          

        welcome_message_box: Panel = Panel(
            welcome_message,
            title = "[bold]WELCOME TO PROJECT-C[/]",
            border_style = "bold yellow",
            padding = (0, 1)
        )
        print() # Newline
        Initializer.terminalController.print(welcome_message_box)
        print() # Newline
       


if __name__ == "__main__":

    Initializer.display_welcome_message()
    Initializer.initialize_project_C()
    
# end of Iniializer()