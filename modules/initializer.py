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


terminalController: Console = Console()


class Initializer():
# Create Configuration database and its contents
# Create Project database and its contents


    def initialize_project_C():
        with terminalController.status("Initializing Project-C...", ):
            time.sleep(5) # 5 seconds delay
            #TODO: Check if the Databases directory and the config.db file has been created and intitialized.          
            #TODO: Throw an error message to the user to let them know that project-C has already been initialized
            #TODO: If not found, create config.yaml and complete the remaining setup process
            
            RESERVOIR_PATH_MESSAGE: tuple[str, str, str] = (
                "[yellow]For Project-C to create and manage the structure of your projects, ",
                "it needs a directory/folder location to keep them. ",
                "Where in your file system would you like Project-C to keep your projects?[/]"
            )
            RESERVOIR_PROMPT: str = "Enter your selected path: "
            INVALID_RESERVOIR_PATH_MESSAGE: tuple[str, str, str] = (
                "ERROR! The path you entered is invalid. ",
                "For Project-C to proceed with initialization, it needs a valid path in your file system. ",
                "Please enter a valid path."
            )
            INVALID_RESERVOIR_PATH_MESSAGE_2: str = "Error! The path is invalid. Please enter a valid path."
            ATTEMPT_EXCEEDED_MESSAGE: str = "Invalid path! Attempt exceeded. Run Project-C again."
            database_directory_path: Path = Path("../Databases").resolve()
            projectc_config_path: Path = Path("../Databases/config.yaml").resolve()
            projects_database_path: Path = Path("../Databases/projects.db").resolve()
            if not database_directory_path.exists():
                database_directory_path.mkdir()
                time.sleep(3)
                terminalController.print("Databases directory created!")
            if not projectc_config_path.exists():
                time.sleep(3)
                ConfigurationDatabase.create_database()
                terminalController.print("Configuration file created!")
            if not projects_database_path.exists():
                time.sleep(3)
                ProjectDatabase.create_database()
                terminalController.print("Project Databases created!")
        terminalController.print(''.join(RESERVOIR_PATH_MESSAGE))
        input_attempt_counter: int = 3
        while input_attempt_counter:
            user_input_path: str = input(RESERVOIR_PROMPT)                
            if not Path(user_input_path).exists():
                match input_attempt_counter:
                    case 3:
                        terminalController.print(''.join(INVALID_RESERVOIR_PATH_MESSAGE))
                    case 2:
                        terminalController.print(INVALID_RESERVOIR_PATH_MESSAGE_2)
                    case 1:
                        terminalController.print(ATTEMPT_EXCEEDED_MESSAGE)
                input_attempt_counter -= 1
                continue
            terminalController.print("VALID PATH!")
            break
        



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
        terminalController.print(welcome_message_box)
        print() # Newline
       


if __name__ == "__main__":

    try:
        Initializer.display_welcome_message()
        Initializer.initialize_project_C()
    except KeyboardInterrupt:
        terminalController.print("Program exited!")
    
    
# end of Iniializer()