###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

import argparse
from argparse import ArgumentParser
from argparse import Namespace


HELP_MESSAGE: str = {
    "cli_inteface_help" : "A command-line utility to automate the creation and management of Python projects.", 
#    "sub_parser_help" : "List of available Project-C operations.",
    "init_help" : "Initialises Project-C after installation.",
    "create_help" : "Creates a new Python project.",
    "config_help" : "Used in configuring settings related to Proeject-C or a project/projects.",
    "info_help" :  "Provide information about project(s).",
    "delete_help" : "Delete a project or group of projects.",
    "lightweight" : "Create a lite project with minimal files and resources.",
    "heavyweight" : "Create a fully documented project with all necessary files (LICENSE, PYPROJECT.TOML, ETC)." 
}

USAGE_MESSAGE: str = {
    "cli_interface_usage" : "[projectc | pc] [subcommand] [argument(s)] [parameter(s)]"
}

# main command parser
cli_interface: ArgumentParser = ArgumentParser(
    prog="Project-C",
    description=HELP_MESSAGE["cli_inteface_help"],
    usage=USAGE_MESSAGE["cli_interface_usage"]
)

# subcommand parser
sub_parsers: argparse._SubParsersAction = cli_interface.add_subparsers(
    title="Project-C subcommands", 
    help="", #HELP_MESSAGE["sub_parser_help"],
    metavar=""
)

# subcommands
init_parser: ArgumentParser = sub_parsers.add_parser("init", help=HELP_MESSAGE["init_help"], usage="[projectc | pc] init")
create_parser: ArgumentParser = sub_parsers.add_parser("create", help=HELP_MESSAGE["create_help"], usage="[projectc | pc] create [argument(s)] [parameter(s)]")
config_parser: ArgumentParser = sub_parsers.add_parser("config", help=HELP_MESSAGE["config_help"], usage="[projectc | pc] config [argument(s)] [parameter(s)]")
info_parser: ArgumentParser = sub_parsers.add_parser("info", help=HELP_MESSAGE["info_help"], usage="[projectc | pc] info [argument(s)] [parameter(s)]")
delete_parser: ArgumentParser = sub_parsers.add_parser("delete", help=HELP_MESSAGE["delete_help"], usage="[projectc | pc] delete [argument(s)] [parameter(s)]")

# Defining arguments for the necessary subcommands

# CREATE
csb_option_groups: argparse._ArgumentGroup = create_parser.add_argument_group("Project Type")
ptype_options: argparse._MutuallyExclusiveGroup = csb_option_groups.add_mutually_exclusive_group(required=True)
ptype_options.add_argument("-lw", "--lightweight", action="store_true", help="Lite/Simple project stucture.")
ptype_options.add_argument("-hw", "--heavyweight", action="store_true", help="Fully documented and defined project structure.")
p_info: argparse._ArgumentGroup = create_parser.add_argument_group("Project Name and Description")
p_info.add_argument("-n", "--name")
p_info.add_argument("-d", "--description")

# CONFIG



if __name__ == "__main__":
    
    # Write your test code here.
    namespace: Namespace = cli_interface.parse_args()


# end of source code