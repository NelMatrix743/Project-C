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
from rich.panel import Panel
from rich.console import Console 


class Initializer():

    def initialize_project_C():
        # work on this
        pass


    def verify_sudo_mode():
        pass


    def display_welcome_message() -> None:
        welcome_message: str = """
WELCOME TO PROJECT-C
...
        """
        Console.print(welcome_message)
        with Console.status():
            #TODO: retrieve project-c initialisation state from the config.db file



# end of Iniializer()