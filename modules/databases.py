###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.username = NelMatrix743                                   #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

import sqlite3 as sql
from project import Project
from datetime import datetime


class DatabaseMixin():
    # Note: This database is used as a scafold for the database classes below
    # It must not be initialized.
    pass



class ConfigurationDatabase(DatabaseMixin):
    # Note: Static class. Must not be initialized
    pass



class TemplateDatabase(DatabaseMixin):
    # Note: Static class. Must not be initialized
    pass



class ProjectDatabase(DatabaseMixin):
    # Note: Static class. Must not be initialized
    pass


# end of program
