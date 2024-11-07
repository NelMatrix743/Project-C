###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.username = NelMatrix743                                   #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

import string
import random
from datetime import datetime

# This module contains general utilities like name parsing functions, id creation functions, etc...

# Characters used in forming a project ID
VALID_HEX_ID_CHARACTERS: str = "abcde" + string.digits


class Util():

    # Note: Static class. Must not be initialized.
    def parse_name(raw_name: str) -> str:
        name_tokens: list[str] = raw_name.replace('-', ' ').replace('_', ' ').split(" ")


    def generate_project_uid(project_name: str) -> str:
        """ Generate a unique ID of the format: prjt-XXXX-ABCDE"""
        prefix: str = "prjt"
        random_hex_str: str = ''.join([random.choice(VALID_HEX_ID_CHARACTERS) for ch in range(5)])


    def retrieve_datetime():
        date_list: list[str] = ["YEAR", "MONTH", "DAY", "TIME"]
        date_str: str = datetime.now().strftime("%Y %B %A %X")
        date_dict: dict[str, str] = dict(zip(date_list, date_str.split()))
        return date_dict


# end of source code