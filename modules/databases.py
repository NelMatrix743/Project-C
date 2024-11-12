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
    CONFIG: dict[str, any] = {
        "Setup Date" : f"{setup_date['YEAR']}-{setup_date['MONTH']}-{setup_date['DAY']}_{setup_date['DAY_NUM']}-[{setup_date['TIME']}]",
        "Version" : project_c_version,
        "Reservoir Path" : reservoir_path
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
    template_database_path: Path | None = None

    def create_database() -> None:
        TemplateDatabase.template_database_path = Path("../Databases/templates.db")



class ProjectDatabase():

    # Note: Static class. Must not be initialized
    project_database_path: Path | None = None

    def create_database() -> None:
        ProjectDatabase.project_database_path = Path("../Databases/projects.db")



if __name__ == "__main__":
    Path.mkdir("../Databases")   # Implement this specific line in the initializer.py module
    ConfigurationDatabase.create_database()

# end of program
