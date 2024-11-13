###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

import yaml
from utils import Util
import sqlite3 as sql
from project import Project
from datetime import datetime
from pathlib import Path


class ConfigurationDatabase():

    # Note: Static class. Must not be initialized
    config_database_path: Path = Path("../Databases/config.yaml")
    setup_date: dict[str, str] = Util.retrieve_datetime()
    project_c_version: str = "1.0.0"
    reservoir_path: str | None = None
    user_name: str | None = None
    nick_name: str | None = None
    github_account_name: str | None = None
    github_url: str | None = None
    CONFIG: dict[str, any] = {
        "Setup Date" : f"{setup_date['YEAR']}-{setup_date['MONTH']}-{setup_date['DAY']}_{setup_date['DAY_NUM']}-[{setup_date['TIME']}]",
        "Version" : project_c_version,
        "Reservoir Path" : reservoir_path,
        "User Name" : user_name,
        "Nick Name" : nick_name,
        "GitHub Name" : github_account_name,
        "GitHub URL" : github_url
    }


    def create_database() -> None:
        with ConfigurationDatabase.config_database_path.open('x') as file:
            yaml.safe_dump(ConfigurationDatabase.CONFIG, file, default_flow_style=False)


    def load_configuration() -> dict[str, any]:
        with ConfigurationDatabase.config_database_path.open('r') as file:
            return yaml.safe_load(file)


    def save_configuration_changes(changes: dict[str, any]) -> None:
        with ConfigurationDatabase.config_database_path.open('w') as file:
            yaml.safe_dump(changes, file, default_flow_style=False)



class TemplateDatabase():

    # Note: Static class. Must not be initialized
    SOURCE_CODE_HEADER: str = f"""
################################################################################
# Programmer.name = {ConfigurationDatabase.CONFIG["User Name"]}{(59 - len(ConfigurationDatabase.CONFIG["User Name"]))*' '}#
# Programmer.nick_name = {ConfigurationDatabase.CONFIG["Nick Name"]}{(54 - len(ConfigurationDatabase.CONFIG["Nick Name"]))*' '}#
# Programmer.GitHub.user_name = {ConfigurationDatabase.CONFIG["GitHub Name"]}{(47 - len(ConfigurationDatabase.CONFIG["GitHub Name"]))*' '}#
# Programmer.GitHub.url = {ConfigurationDatabase.CONFIG["GitHub URL"]}{(53 - len(ConfigurationDatabase.CONFIG["GitHub URL"]))*' '}#
################################################################################
"""

    TEMPLATE: dict[str, str] = {
        "HEADER" : SOURCE_CODE_HEADER,

    }


class ProjectDatabase():

    # Note: Static class. Must not be initialized
    project_database_path: Path | None = None

    def create_database() -> None:
        ProjectDatabase.project_database_path = Path("../Databases/projects.db")



if __name__ == "__main__":
    # Path.mkdir("../Databases")   # Implement this specific line in the initializer.py module
    # ConfigurationDatabase.create_database()

    print(TemplateDatabase.SOURCE_CODE_HEADER)

# end of program
