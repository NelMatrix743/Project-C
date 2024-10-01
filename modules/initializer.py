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
#from git import Repo 
from display import *
from rich.panel import Panel
from rich.console import Console 


class Initializer():

    terminalController: Console = Console()

    def initialize_project_C():
        # work on this
        pass


    def verify_sudo_mode():
        pass


    def display_welcome_message() -> None:
        welcome_message: str = """
[italic bright_yellow]Project-C is your go-to CLI tool for creating and managing Python projects effortlessly from the command line.
With Project-C, you can customize your project setup by selecting the files and directories you want to include, like README files, __init__ files, test directories, and more.
It also offers built-in support for setting up git repositories and Python virtual environments automatically — unless you prefer to handle those yourself.
Whether you're starting a new project, managing existing ones, or cleaning up, Project-C is here to streamline the process. Happy coding![/]
        """
        welcome_message_box: Panel = Panel(
            welcome_message,
            title = "[bold blink]WELCOME TO PROJECT-C[/]",
            border_style = "bold yellow",
            padding = (0, 2)
        )

        Initializer.terminalController.print(welcome_message_box)
        # with Console.status():
        #     #TODO: retrieve project-c initialisation state from the config.db file


Initializer.display_welcome_message()
# end of Iniializer()