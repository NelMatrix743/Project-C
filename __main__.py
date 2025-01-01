###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

import argparse
from modules.cli import cli_interface
# from modules.initializer import Initializer
# from modules.project import Project
# from modules.pcreator import ProjectCreator
# from modules.pconfig import ProjectConfigurator
# from modules.pinform import ProjectInformer
# from modules.pterminate import ProjectTerminator


def start_program(main_interface: argparse.ArgumentParser):
    arguments: argparse.Namespace = main_interface.parse_args()



if __name__ == "__main__":

    # main execution point
    start_program(cli_interface)

# end of program