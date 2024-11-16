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
    user_name: str | None = None #"Newton"
    nick_name: str | None = None #"NewGravity"
    github_account_name: str | None = None #"Newvento"
    github_url: str | None = None #"https://github.com/Newvento"
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
#     SOURCE_CODE_HEADER: str = f"""
# ################################################################################
# # Programmer.name = {ConfigurationDatabase.CONFIG["User Name"]}{(59 - len(ConfigurationDatabase.CONFIG["User Name"]))*' '}#
# # Programmer.nick_name = {ConfigurationDatabase.CONFIG["Nick Name"]}{(54 - len(ConfigurationDatabase.CONFIG["Nick Name"]))*' '}#
# # Programmer.GitHub.user_name = {ConfigurationDatabase.CONFIG["GitHub Name"]}{(47 - len(ConfigurationDatabase.CONFIG["GitHub Name"]))*' '}#
# # Programmer.GitHub.url = {ConfigurationDatabase.CONFIG["GitHub URL"]}{(53 - len(ConfigurationDatabase.CONFIG["GitHub URL"]))*' '}#
# ################################################################################
# """

    DEFAULT_GITIGNORE_CONTENT: str = """.venv\n.info"""

    # TEMPLATE: dict[str, str] = {
    #     "HEADER" : _SOURCE_CODE_HEADER,

    # }

    def get_info_data(project: Project) -> str:
        INFO_DATA: str = f"""
PROJECT NAME: {project.raw_name}
PROJECT ID: {project.p_uid}
PROJECT RESERVOIR PATH: {project.full_path}
CREATION DATE-TIME: {project.creation_datetime["SHORT_FORM"]} - [{project.creation_datetime["TIME"]}] 
STATUS: {project.status}
VENV NAME: {project.venv_name}
DESCRIPTION: {project.description}
"""     
        return INFO_DATA



class ProjectDatabaseNonExistentException(Exception):
    """
    This exception is thrown by the methods (except create_database()) in ProjectDatabase() when the projects.db file is missing (deleted or not yet created).
    """
    pass


class ProjectDatabase():

    # Note: Static class. Must not be initialized
    project_database_path: Path = Path("../Databases/projects.db")

    def create_database() -> None:
        db_conn: sql.Connection = sql.connect(ProjectDatabase.project_database_path)
        db_cursor: sql.Cursor = db_conn.cursor()
        db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects_table (
                id text NOT NULL PRIMARY KEY,
                name text NOT NULL,
                status text NOT NULL,
                project_description text,
                venv_prompt text NOT NULL,
                full_path text NOT NULL,
                creation_datetime text NOT NULL
            );
              """)
        db_conn.commit()
        db_conn.close()


    def insert_project_data(project: Project) -> None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException
        str_creation_datetime: str = str.join(';',[
            project.creation_datetime["SHORT_FORM"],
            project.creation_datetime["YEAR"],
            project.creation_datetime["MONTH"],
            project.creation_datetime["DAY"],
            project.creation_datetime["DAY_NUM"],
            project.creation_datetime["TIME"]
        ])
        project_data: tuple[str] = (
            project.p_uid,
            project.raw_name,
            project.description,
            str_creation_datetime,
            project.full_path,
            project.venv_prompt,
            project.status
        )
        # Implement sql-exception try-catch statements for cases such database file corruption, etc.
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""
                INSERT INTO projects_table(
                    id, name, project_description, creation_datetime, full_path, venv_prompt, status          
                    )
                VALUES(?, ?, ?, ?, ?, ?, ?);
            """, project_data)
            db_conn.commit()


    def retrieve_project_data(project_id: str) -> None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        # Implement sql-exception try-catch statements for cases such database file corruption, etc.
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""

            """)
            db_conn.commit()

   
    def update_project_data(project_id: str) -> None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        # Implement sql-exception try-catch statements for cases such database file corruption, etc.
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""

            """)
            db_conn.commit()


    def delete_project_data(project_id: str) -> None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        # Implement sql-exception try-catch statements for cases such database file corruption, etc.
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""

            """)
            db_conn.commit()



if __name__ == "__main__":
    # path: str = "../Databases"
    # if not Path(path).exists():
    #     Path.mkdir(path)   # Implement this specific line in the initializer.py module
    #ConfigurationDatabase.create_database()
    #print(TemplateDatabase.TEMPLATE["HEADER"])
    # test_project: Project = Project(
    #     "Pygame",
    #     "Python library for building games in Python."
    # )
    #print(TemplateDatabase.get_info_data(test_project))
    # ProjectDatabase.create_database()
    # project: Project = Project("PyGame Programme", "A simple game built using PyGame, a Python module.")
    # project.full_path = "home/nelmatrix/Project_Reservoir"
    # project.venv_prompt = "Game Prompt"
    # project.status = "ONGOING"
    # ProjectDatabase.insert_project_data(project)
    # print("New project entry added successfully!")
    pass

# end of program