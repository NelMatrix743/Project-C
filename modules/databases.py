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



class InfoContentManager():

    def get_info_data(project: Project) -> dict[str, str]:
        return {
            "PROJECT NAME" : project.parsed_name,
            "PROJECT ID" : project.p_uid,
            "DESCRIPTION" : project.description,
            "CREATION DATE-TIME" : f"{project.creation_datetime['SHORT_FORM']} - {project.creation_datetime['TIME']}",
            "PROJECT RESERVOIR PATH" : project.full_path,
            "VENV PROMPT" : project.venv_prompt,
            "STATUS" : project.status
        }


    def update_id(info_file_path: str, new_id: str) -> None:
        pass


    def update_name(info_file_path: str, new_name: str) -> None:
        pass       

    
    def update_description(info_file_path: str, new_description: str) -> None:
        pass


    def update_reservoir_path(info_file_path: str, new_reservoir_path: str) -> None:
        pass


    def update_venv_prompt(info_file_path: str, new_venv_prompt: str) -> None:
        pass


    def update_status(info_file_path: str, new_status: str) -> None:
        pass



class TemplateDatabase():
    
    # Note: Static class. Must not be initialized

    def get_source_code_header() -> str:
        return f"""
################################################################################
# Programmer.name = {ConfigurationDatabase.CONFIG["User Name"]}{(59 - len(ConfigurationDatabase.CONFIG["User Name"]))*' '}#
# Programmer.nick_name = {ConfigurationDatabase.CONFIG["Nick Name"]}{(54 - len(ConfigurationDatabase.CONFIG["Nick Name"]))*' '}#
# Programmer.GitHub.user_name = {ConfigurationDatabase.CONFIG["GitHub Name"]}{(47 - len(ConfigurationDatabase.CONFIG["GitHub Name"]))*' '}#
# Programmer.GitHub.url = {ConfigurationDatabase.CONFIG["GitHub URL"]}{(53 - len(ConfigurationDatabase.CONFIG["GitHub URL"]))*' '}#
################################################################################
"""


    def get_default_git_content() -> str:
        return """.venv\n.info"""
    


class ProjectDatabase():

    # Note: Static class. Must not be initialized
    project_database_path: Path = Path("../Databases/projects.db")

    def create_database() -> None:
        db_conn: sql.Connection = sql.connect(ProjectDatabase.project_database_path)
        db_cursor: sql.Cursor = db_conn.cursor()
        db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects_table (
                project_id text NOT NULL PRIMARY KEY,
                project_name text NOT NULL,
                project_description text,
                creation_datetime text NOT NULL,
                reservoir_path text NOT NULL,
                venv_prompt text NOT NULL,
                project_status text NOT NULL
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
            try:
                db_cursor.execute("""
                    INSERT INTO projects_table(
                        project_id, project_name, project_description, creation_datetime, reservoir_path, venv_prompt, project_status          
                        )
                    VALUES(?, ?, ?, ?, ?, ?, ?);
                """, project_data)
                db_conn.commit()
            except sql.IntegrityError as error:
                if "unique constraint failed" in str(error).lower():
                    project.p_uid = Util.generate_project_uid(project.parsed_name)
                    ProjectDatabase.insert_project_data(project)                    


    def retrieve_project_data(project_id: str) -> Project | None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        # Implement sql-exception try-catch statements for cases such database file corruption, etc.
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""
                SELECT * FROM projects_table WHERE project_id = ?;
            """, (project_id,))
            result: tuple[str] | None = db_cursor.fetchone()
            return_project: Project | None = None
            if result: # Not None
                return_project = Project(result[1], description=result[2])
                return_project.p_uid = result[0]
                return_project.creation_datetime = Util.parse_datetime(result[3])
                return_project.full_path = result[4]
                return_project.venv_prompt = result[5]
                return_project.status = result[6]
            return return_project


    def retrieve_all_projects_data() -> list[Project] | None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        # Implement sql-exception try-catch statements for cases such database file corruption, etc.
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""
                SELECT * FROM projects_table;
            """)
            result: list[tuple[str]] = db_cursor.fetchall() # If no row is found, an empty list is returned
            return result


    def update_project_id_data(old_project_id: str, new_project_id: str) -> None:
        if old_project_id == new_project_id:
            return
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        # Implement sql-exception try-catch statements for cases such database file corruption, etc.
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""
                  UPDATE projects_table SET project_id = ? WHERE project_id = ?;
            """, (new_project_id, old_project_id))
            db_conn.commit()
            print(f"The total number of row modified is: {db_cursor.rowcount}")
            if db_cursor.rowcount == 0:
                raise ProjectEntryDoesNotExistException
            
               
    def update_project_name_data(project_id: str, new_name: str) -> None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        # Implement sql-exception try-catch statements for cases such database file corruption, etc.
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""

            """)
            db_conn.commit()


    def update_project_description_data(project_id: str, new_description: str) -> None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        # Implement sql-exception try-catch statements for cases such database file corruption, etc.
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""

            """)
            db_conn.commit()


    def update_project_status_data(project_id: str, new_status: str) -> None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        # Implement sql-exception try-catch statements for cases such database file corruption, etc.
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""

            """)
            db_conn.commit()
            
        
    def update_project_venv_prompt_data(project_id: str, new_venv_promt: str) -> None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        # Implement sql-exception try-catch statements for cases such database file corruption, etc.
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""

            """)
            db_conn.commit()
    

    def update_project_reservoir_path_data(project_id: str, new_reservoir_path: str) -> None:
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



class ProjectDatabaseNonExistentException(Exception):
    """
    This exception is thrown by the methods (except create_database()) in ProjectDatabase() when the projects.db file is missing (deleted or not yet created).
    """
    pass



class ProjectEntryDoesNotExistException(Exception):
    """
    This exception is thrown when a user tries to query a project entry/row from the projects.db database but the entry does not exist (or has been deleted).
    """
    pass



if __name__ == "__main__":
    # path: str = "../Databases"
    # if not Path(path).exists():
    #    Path.mkdir(path)   # Implement this specific line in the initializer.py module
    # # #ConfigurationDatabase.create_database()
    # # #print(TemplateDatabase.TEMPLATE["HEADER"])
    # # # test_project: Project = Project(
    # # #     "Pygame",
    # # #     "Python library for building games in Python."
    # # # )
    # # #print(TemplateDatabase.get_info_data(test_project))
    # ProjectDatabase.create_database()
    # project: Project = Project("PyGame Programme", "A simple game built using PyGame, a Python module.")
    # project.full_path = "home/nelmatrix/Project_Reservoir"
    # project.venv_prompt = "Game Prompt"
    # project.status = "ONGOING"
    # ProjectDatabase.insert_project_data(project)
    # print("New project entry added successfully!")
    # print(f"First project: {ProjectDatabase.retrieve_project_data(project.p_uid)}")
    # new_id: str = Util.generate_project_uid(project.parsed_name)
    # try:
    #     ProjectDatabase.update_project_id_data(project.p_uid, new_id)
    #     print("Project ID updated successfully!")
    #     print(f"Update: {ProjectDatabase.retrieve_project_data(new_id)}")
    # except ProjectEntryDoesNotExistException:
    #     print("No project entry with that ID was found in the database.")
    pass
  
# end of program