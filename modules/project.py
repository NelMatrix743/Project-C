###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

import os 
import string 
import random 
from display import * 
from utils import Util
from typing import Self
from pathlib import Path


class Project():
    
    def __init__(self, input_name: str, description: str | None = None):
        self.raw_name: str = input_name                                 # request the user to provide it
        self.parsed_name: str = Util.parse_name(input_name)
        self.p_uid: str = Util.generate_project_uid(self.parsed_name)
        self.description: str | None = description                      # request the user to provide it
        self._creation_datetime: dict[str, str] | None = None        
        self.status: str = "ONGOING"
        self._full_path: str = None
        self.venv_prompt: str | None = self.raw_name.upper()


    @property
    def creation_datetime(self) -> str:
        if self._creation_datetime == None:
            return Util.retrieve_datetime()
        return self._creation_datetime


    @creation_datetime.setter
    def creation_datetime(self, dict_datetime: dict[str, str]) -> None:
        self._creation_datetime = dict_datetime


    @property
    def full_path(self) -> str:
        return self._full_path
    
    
    @full_path.setter
    def full_path(self, path: str) -> None:
        self._full_path = str(Path(path, self.parsed_name))
        

    def __str__(self) -> str:
        return f"""
Raw Name: {self.raw_name}
Project ID: {self.p_uid}
Parsed Name: {self.parsed_name}
Description: {self.description}
Creation DateTime: {self._creation_datetime}
Full Path: {self.full_path}
Venv Promt: {self.venv_prompt}
Status: {self.status}
        """

if __name__ == "__main__":
    # p = Project("Hello World", description="This is a simple Hello world program.")
    # print(p)
    pass

# end of Project()