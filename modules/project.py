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


class Project():
    
    def __init__(self, input_name, description: str | None = None):
        self.raw_name: str = input_name
        self._parsed_name: str = Util.parse_name(input_name)
        self.p_uid: str = Util.generate_project_uid(self._parsed_name)
        self.description: str | None = description
        self.creation_datetime: dict[str, str] = Util.retrieve_datetime()
        self.status: str | None = None
        self.full_path: str = None
        self.venv_prompt: str | None = None


    @property
    def parsed_name(self) -> str:
        return str.join('_', self._parsed_name)


    def __str__(self) -> str:
        return f"""
Raw Name: {self.raw_name}
Project ID: {self.p_uid}
Parsed Name: {self.parsed_name}
Description: {self.description}
        """

if __name__ == "__main__":
    p = Project("Hello World", description="This is a simple Hello world program.")
    print(p)

# end of Project()