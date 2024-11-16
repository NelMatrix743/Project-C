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


class Project():
    
    def __init__(self, input_name, description: str | None = None):
        self.raw_name: str = input_name
        self._parsed_name: str = Util.parse_name(input_name)
        self.p_uid: str = Util.generate_project_uid(self._parsed_name)
        self.description: str | None = description
        self._creation_datetime: dict[str, str] | None = None        
        self.status: str | None = None
        self.full_path: str = None
        self.venv_prompt: str | None = None


    @property
    def parsed_name(self) -> str:
        return str.join('_', self._parsed_name)


    @property
    def creation_datetime(self) -> str:
        if self._creation_datetime == None:
            return Util.retrieve_datetime()
        return self._creation_datetime


    @creation_datetime.setter
    def creation_datetime(self, dict_datetime: dict[str, str]) -> None:
        self._creation_datetime = dict_datetime


    def __str__(self) -> str:
        return f"""
Raw Name: {self.raw_name}
Project ID: {self.p_uid}
Parsed Name: {self.parsed_name}
Description: {self.description}
        """

if __name__ == "__main__":
    # p = Project("Hello World", description="This is a simple Hello world program.")
    # print(p)
    pass

# end of Project()