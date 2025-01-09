###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

import argparse
from argparse import ArgumentParser


HELP_MESSAGE: str = {
    "cli_inteface_help" : "A command-line utility to automate the creation and management of Python projects.", 
    "sub_parser_help" : "List of available Project-C operations.",
    "init_help" : "Initialises Project-C after installation.",
    "create_help" : "Creates a new Python project.",
    "config_help" : "Used in configuring settings related to Proeject-C or a project/projects.",
    "info_help" :  "Provide information about project(s).",
    "terminate_help" : "Delete a project or group of projects."  
}

# main command parser
cli_interface: ArgumentParser = ArgumentParser(
    prog="Project-C",
    description=HELP_MESSAGE["cli_inteface_help"]
)

# subcommand parser
sub_parsers = cli_interface.add_subparsers(
    title="Project-C Commands", 
    help=HELP_MESSAGE["sub_parser_help"]
)

# subcommands
init_parser: ArgumentParser = sub_parsers.add_parser("init", help=HELP_MESSAGE["init_help"])
create_parser: ArgumentParser = sub_parsers.add_parser("create", help=HELP_MESSAGE["create_help"])
config_parser: ArgumentParser = sub_parsers.add_parser("config", help=HELP_MESSAGE["config_help"])
info_parser: ArgumentParser = sub_parsers.add_parser("info", help=HELP_MESSAGE["info_help"])
terminate_parser: ArgumentParser = sub_parsers.add_parser("terminate", help=HELP_MESSAGE["terminate_help"])



if __name__ == "__main__":
    
    # Write your test code here.
    pass

# end of source code