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

    def create_info_data_file(project: Project) -> None:
        INFO_DATA: dict[str, str] = {
            "PROJECT NAME" : project.raw_name,
            "PROJECT ID" : project.p_uid,
            "DESCRIPTION" : project.description,
            "CREATION DATE-TIME" : f"{project.creation_datetime['SHORT_FORM']} - {project.creation_datetime['TIME']}",
            "PROJECT RESERVOIR PATH" : project.full_path,
            "VENV PROMPT" : project.venv_prompt,
            "STATUS" : project.status
        }
        INFO_DATA_FILE: Path = Path(project.full_path) / ".info"
        if not INFO_DATA_FILE.exists():
            with INFO_DATA_FILE.open('x') as info_file:
                yaml.safe_dump(INFO_DATA, info_file, default_flow_style=False)
            
        

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
        UPDATE_ERROR_MESSAGE: str = """
        [UpdateError]: Invalid Project ID. Entry non-existent in the database, hence project id cannot be updated.
        """
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""
                UPDATE projects_table SET project_id = ? WHERE project_id = ?;
            """, (new_project_id, old_project_id))
            db_conn.commit()
            if db_cursor.rowcount == 0:
                raise ProjectEntryDoesNotExistException(UPDATE_ERROR_MESSAGE)
            
               
    def update_project_name_data(project_id: str, new_name: str) -> None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        UPDATE_ERROR_MESSAGE: str = """
        [UpdateError]: Invalid Project ID. Entry non-existent in the database, hence project name cannot be updated.
        """
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""
                UPDATE projects_table SET project_name = ? WHERE project_id = ?; 
            """, (new_name, project_id))
            db_conn.commit()
            if db_cursor.rowcount == 0:
                raise ProjectEntryDoesNotExistException(UPDATE_ERROR_MESSAGE)


    def update_project_description_data(project_id: str, new_description: str) -> None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        UPDATE_ERROR_MESSAGE: str = """
        [UpdateError]: Invalid Project ID. Entry non-existent in the database, hence project description cannot be updated.
        """
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""
                UPDATE projects_table SET project_description = ? WHERE project_id = ?; 
            """, (new_description, project_id))
            db_conn.commit()
            if db_cursor.rowcount == 0:
                raise ProjectEntryDoesNotExistException(UPDATE_ERROR_MESSAGE)


    def update_project_status_data(project_id: str, new_status: str) -> None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        UPDATE_ERROR_MESSAGE: str = """
        [UpdateError]: Invalid Project ID. Entry non-existent in the database, hence project status cannot be updated.
        """
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""
                UPDATE projects_table SET project_status = ? WHERE project_id = ?; 
            """, (new_status, project_id))
            db_conn.commit()
            if db_cursor.rowcount == 0:
                raise ProjectEntryDoesNotExistException(UPDATE_ERROR_MESSAGE)
            
        
    def update_project_venv_prompt_data(project_id: str, new_venv_promt: str) -> None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        UPDATE_ERROR_MESSAGE: str = """
        [UpdateError]: Invalid Project ID. Entry non-existent in the database, hence venv prompt cannot be updated.
        """
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""
                UPDATE projects_table SET venv_prompt = ? WHERE project_id = ?; 
            """, (new_venv_promt, project_id))
            db_conn.commit()
            if db_cursor.rowcount == 0:
                raise ProjectEntryDoesNotExistException(UPDATE_ERROR_MESSAGE)
   

    def update_project_reservoir_path_data(project_id: str, new_reservoir_path: str) -> None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        UPDATE_ERROR_MESSAGE: str = """
        [UpdateError]: Invalid Project ID. Entry non-existent in the database, hence reservoir path cannot be updated.
        """
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""
                UPDATE projects_table SET reservoir_path = ? WHERE project_id = ?; 
            """, (new_reservoir_path, project_id))
            db_conn.commit()
            if db_cursor.rowcount == 0:
                raise ProjectEntryDoesNotExistException(UPDATE_ERROR_MESSAGE)


    def delete_project_data(project_id: str) -> None:
        if not ProjectDatabase.project_database_path.exists():
            raise ProjectDatabaseNonExistentException    
        DELETE_ERROR_MESSAGE: str = """
        [DeleteError]: Invalid Project ID. Entry non-existent in the database, hence it cannot be deleted.
        """
        with sql.connect(ProjectDatabase.project_database_path) as db_conn:
            db_cursor: sql.Cursor = db_conn.cursor()
            db_cursor.execute("""
                DELETE FROM projects_table WHERE project_id = ?;
            """, (project_id,))
            db_conn.commit()
            if db_cursor.rowcount == 0:
                raise ProjectEntryDoesNotExistException(DELETE_ERROR_MESSAGE)
        


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
    
    # path: Path = Path("../Databases").resolve()
    # if not path.exists():
    #    path.mkdir()   # Implement this specific line in the initializer.py module
    # # #ConfigurationDatabase.create_database()
    # # #print(TemplateDatabase.TEMPLATE["HEADER"])
    # # # test_project: Project = Project(
    # # #     "Pygame",
    # # #     "Python library for building games in Python."
    # # # )
    # # #print(TemplateDatabase.get_info_data(test_project))
    # ProjectDatabase.create_database()
    # project: Project = Project("Fitnix", "A simple fitness mobile app.")
    # project.full_path = str(Path(f"../{project.parsed_name}").resolve())
    # project.status = "ONGOING"
    # ProjectDatabase.insert_project_data(project)
    # print("New project entry added successfully!\n")
    # print(f"Project Entry: {ProjectDatabase.retrieve_project_data(project.p_uid)}\n")
    # new_id: str = Util.generate_project_uid(project.parsed_name)
    # try:
    #     ProjectDatabase.update_project_id_data(project.p_uid, new_id)
    #     ProjectDatabase.update_project_name_data(new_id, "Sparkz")
    #     ProjectDatabase.update_project_description_data(new_id, "I changed the name to Sparkz.")
    #     ProjectDatabase.update_project_venv_prompt_data(new_id, "Sparkz")
    #     ProjectDatabase.update_project_reservoir_path_data(new_id, str(Path(f"../{project.full_path}_new").resolve()))
    #     ProjectDatabase.update_project_status_data(new_id, "COMPLETED")
    #     print(f"Update Project Entry: {ProjectDatabase.retrieve_project_data(new_id)}")
    #     print(f"ALL Entered Data: {ProjectDatabase.retrieve_all_projects_data()}")
    #     ProjectDatabase.delete_project_data(new_id)
    #     print(f"\nProject entry [{new_id}] deleted sucessfully!\n\n")
    #     print(ProjectDatabase.retrieve_all_projects_data())
    # except ProjectEntryDoesNotExistException as E:
    #     print(E)
    # Path.mkdir(project.full_path)
    # InfoContentManager.create_info_data_file(project)
    # print("Project info file created successfully!\n")
    # print(f"Project path: {project.full_path}")
    
    pass
  
# end of program