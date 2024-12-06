###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

from .databases import ConfigurationDatabase
from .databases import ProjectDatabase
from pathlib import Path
import yaml


class ProjectConfigurator():
    
    # Project-C related configuration methods:

    def set_reservoir_path(input_path: Path) -> None:    
        PROJECT_C_CONFIG: dict[str, any] = ConfigurationDatabase.load_configuration()
        PROJECT_C_CONFIG["Reservoir Path"] = str(input_path)
        ConfigurationDatabase.save_configuration_changes(PROJECT_C_CONFIG)


    def get_reservoir_path() -> str | None:
        PROJECT_C_CONFIG: dict[str, any] = ConfigurationDatabase.load_configuration()
        return PROJECT_C_CONFIG["Reservoir Path"]


    # User projects related configuration methods:

    # Next method starts from this particular line



if __name__ == "__main__":

    # Test and Debug Run

    user_path: Path = Path("/home/n3lm4tr1x/project_s/Python_Programs/projectc")
    ProjectConfigurator.set_reservoir_path(user_path)
    print(f"User entered the following path: {ProjectConfigurator.get_reservoir_path()}")



# end of source code