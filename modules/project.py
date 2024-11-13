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
    
    def __init__(self, input_name, description: str | None):
        self.raw_name: str = input_name
        self.parsed_name: str = Util.parse_name(input_name)
        self.p_uid: str = Util.generate_project_uid(self.parsed_name)
        self.description: str | None = description
        self.creation_datetime: dict[str, str] = Util.retrieve_datetime()
        self.status: str | None = None
        self.full_path: str = None

    
# end of Project()