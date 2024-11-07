###############################################################################################################################
# Programmer.name = Nelson Chidi                                                                                              #
# Programmer.nick_name = Nelmatrix                                                                                            #
# Programmer.GitHub.username = NelMatrix743                                                                                   #
# Programmer.GitHub.url = https://github.com/NelMatrix743                                                                     #
###############################################################################################################################

import argparse
from modules.cli import CliInterface
from modules.initializer import Initializer
from modules.project import Project
from modules.pcreator import ProjectCreator
from modules.pconfig import ProjectConfigurator
from modules.pinform import ProjectInformer
from modules.pterminate import ProjectTerminator


def run_program(mainInterface: CliInterface):
    pass 


if __name__ == "__main__":

    executionPoint: CliInterface = CliInterface()
    run_program(executionPoint)

# end of program