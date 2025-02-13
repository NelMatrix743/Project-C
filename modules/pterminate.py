###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.username = NelMatrix743                                   #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

from databases import ProjectDatabase
from utils import TerminationType
from project import Project


class ProjectTerminator():
    
    def partial_termination(project_id: str) -> bool:
        input_project: Project = ProjectDatabase.retrieve_project_data(project_id)
        if input_project != None:
            # Proceed with the partial delete operation
            ProjectTerminator.delete_project_dir(input_project.full_path)
            return True
        return False
    
    
    def total_termination(project_id: str) -> bool:
        input_project: Project = ProjectDatabase.retrieve_project_data(project_id)
        if input_project != None:
            # Proceed with the complete delete operation
            ProjectTerminator.delete_project_dir(input_project.full_path)
            ProjectTerminator.delete_project_database_entry(project_id)
            return True
        return False


    def delete_project_dir(path: str) -> bool:
        pass 
    
    
    def delete_project_database_entry(project_id: str) -> bool:
        pass
    

# end of source code