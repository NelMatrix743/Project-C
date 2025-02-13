###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

import string
import random
from enum import Enum
from datetime import datetime

# This module contains general utilities like name parsing functions, id creation functions, etc...

# Characters used in forming a project ID
VALID_HEX_ID_CHARACTERS: str = "abcde" + string.digits


class ProjectType(Enum):
    
    LIGHTWEIGHT: str  = "lightweight"
    HEAVYWEIGHT: str  = "heavyweight"



class ProjectStatus(Enum):
    
    ONGOING: str = "ONGOING"
    COMPLETED: str = "COMPLETED"
    DELETED: str = "DELETED"



class TerminationType(Enum):
    PARTIAL_TERMINATION: str = "Partial Termination"
    TOTAL_TERMINATION: str = "Total Termination"



class Util():

    # Note: Static class. Must not be initialized.
    def parse_name(raw_name: str) -> str:
        for char in raw_name:
            if char in string.punctuation:
                raw_name = raw_name.replace(char, ' ')
        name_tokens: list[str] = raw_name.split(' ')
        for token in name_tokens:
            if len(token) == 0 or token == ' ':
                name_tokens.remove(token)
        return str.join('_', [token.lower() for token in name_tokens])
   
   
    def generate_project_uid(project_parsed_name: str) -> str:
        """ Generate a unique ID of the format: prjt-XXXXX-ABCDE"""
        constant_marker: str = "prjt"
        random_hex_str: str = ''.join([random.choice(VALID_HEX_ID_CHARACTERS) for ch in range(6)])
        name_tokens: list[str] = project_parsed_name.split('_')
        name_initials: str = ""
        for token in name_tokens:
            name_initials += token[0]
        return str.join('-', [constant_marker, random_hex_str, name_initials])


    def retrieve_datetime() -> dict[str, str]:
        date_list: list[str] = ["SHORT_FORM", "YEAR", "MONTH", "DAY", "DAY_NUM", "TIME"]
        date_str: str = datetime.now().strftime(r"%D %Y %B %A %d %X")
        date_dict: dict[str, str] = dict(zip(date_list, date_str.split()))
        return date_dict

    
    def parse_datetime(datetime_str: str) -> dict[str, str]:
        date_list: list[str] = ["SHORT_FORM", "YEAR", "MONTH", "DAY", "DAY_NUM", "TIME"]
        values_list: list[str] = datetime_str.split(';')
        return {key : value for key, value in zip(date_list, values_list)}



if __name__ == "__main__":
    # print(Util.retrieve_datetime()["DAY_NUM"])
    # result = Util.parse_datetime('11/16/24;2024;November;Saturday;16;23:17:18')
    # print(result)
    # name = "Pedestrian Scanner Simulator version 3"
    # print(Util.parse_name(name))
    # print(Util.generate_project_uid(name))
    pass

# end of source code
