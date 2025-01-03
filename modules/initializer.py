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
        with terminalController.status("Initializing Project-C ...", ):
            time.sleep(2)
            INTIALIZATION_FLAG_COUNTER: int = 0
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
            ATTEMPT_EXCEEDED_MESSAGE: str = "Invalid path! Attempt exceeded. Run Project-C initialization again."
            USER_NAME_PROMPT: str = "What is first your name?"
            USER_NICK_NAME_PROMPT: str = "What is your nick name?"
            GITHUB_NAME_PROMPT: str = "What is your github user name?"
            GITHUB_URL_PROMPT: str = "What is your github url?"
            database_directory_path: Path = Path("../Databases").resolve()
            projectc_config_path: Path = Path("../Databases/config.yaml").resolve()
            projects_database_path: Path = Path("../Databases/projects.db").resolve()
            if not database_directory_path.exists():
                time.sleep(1)
                database_directory_path.mkdir()
                INTIALIZATION_FLAG_COUNTER += 1
            if not projectc_config_path.exists():
                time.sleep(1)
                ConfigurationDatabase.create_database()
                INTIALIZATION_FLAG_COUNTER += 1
            if not projects_database_path.exists():
                time.sleep(1)
                ProjectDatabase.create_database()
                INTIALIZATION_FLAG_COUNTER += 1
        if INTIALIZATION_FLAG_COUNTER:
            terminalController.print(''.join(RESERVOIR_PATH_MESSAGE))
            input_attempt_counter: int = 3
            user_input_path: str | None = None
            while input_attempt_counter:
                user_input_path = input(RESERVOIR_PROMPT)                
                if not Path(user_input_path).exists():
                    match input_attempt_counter:
                        case 3:
                            terminalController.print(''.join(INVALID_RESERVOIR_PATH_MESSAGE))
                        case 2:
                            terminalController.print(INVALID_RESERVOIR_PATH_MESSAGE_2)
                        case 1:
                            failure_msg_display(ATTEMPT_EXCEEDED_MESSAGE)
                    input_attempt_counter -= 1
                    continue
                terminalController.print(USER_NAME_PROMPT)
                ConfigurationDatabase.update_user_name(input("First name: "))
                terminalController.print(USER_NICK_NAME_PROMPT)
                ConfigurationDatabase.update_user_nickname(input("Nick name: "))
                terminalController.print(GITHUB_NAME_PROMPT)
                ConfigurationDatabase.update_github_name(input("GitHub user name: "))
                terminalController.print(GITHUB_URL_PROMPT)
                ConfigurationDatabase.update_github_url(input("GitHub URL: "))
                with terminalController.status("Finalizing the initialization process ..."):
                    ConfigurationDatabase.update_reservoir_path(str(Path(user_input_path).resolve()))
                    time.sleep(3)
                success_msg_display(
                    ''.join(["---Initialization completed!---\n", 
                            "For more information on how to use Project-C, ",
                            "run the following command:\n[italic]python project-c --help[/]  or  [italic]python pc --help[/]"]), 
                    turn_icon_off=True
                )
                break
        else:
            info_msg_display(
                ''.join(["Project-C has already been initialized. For more information on how to use Project-C, ",
                         "run the following command:\n[italic]python project-c --help[/]  or  [italic]python pc --help[/]"]),
                turn_icon_off=True
            )
        

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