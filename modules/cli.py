###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.user_name = NelMatrix743                                  #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

import argparse 


# main command parser
cli_interface: argparse.ArgumentParser = argparse.ArgumentParser(
    prog="Project-C",
    description="A command-line utility to automate the creation and management of Python projects."
)

# subcommand parser
sub_parsers = cli_interface.add_subparsers(
    title="Project-C Commands", 
    help="List of available Project-C operations."
)

# subcommands
init_parser: argparse.ArgumentParser = sub_parsers.add_parser("init", help="Initialises Project-C after installation.")
create_parser: argparse.ArgumentParser = sub_parsers.add_parser("create", help="Creates a new Python project.")
config_parser: argparse.ArgumentParser = sub_parsers.add_parser("config", help="Used in configuring settings related to Proeject-C or a project/projects.")
info_parser: argparse.ArgumentParser = sub_parsers.add_parser("info", help="Provide information about project(s).")
terminate_parser: argparse.ArgumentParser = sub_parsers.add_parser("terminate", help="Delete a project or group of projects.")



if __name__ == "__main__":
    
    # Write your test code here.
    pass

# end of source code