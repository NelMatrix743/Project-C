###############################################################################
# Programmer.name = Nelson Chidi                                              #
# Programmer.nick_name = Nelmatrix                                            #
# Programmer.GitHub.username = NelMatrix743                                   #
# Programmer.GitHub.url = https://github.com/NelMatrix743                     #
###############################################################################

from rich.console import Console


displayController: Console = Console() # Global console controller


# Prints a message when an action is successful
def success_msg_display(message: str, newline: int = 1, turn_icon_off=False) -> None: 
    success_icon: str = '' if turn_icon_off else  "[bold bright_green]:heavy_check_mark:[/]"
    msg_indicator: str = '[' + "[bold bright_green]" + "SUCCESS" + "[/]" + ']'
    message = "[bright_green]" + message + "[/]"
    displayController.print(msg_indicator, message, success_icon, end=('\n'*newline))


# Prints a message that serves as information
def info_msg_display(message: str, newline: int = 1, turn_icon_off=False) -> None:
    info_icon: str = '' if turn_icon_off else  "[bold bright_yellow](:information_source:)[/]"
    msg_indicator: str = '[' + "[bold bright_yellow]" + "INFO" + "[/]" + ']'
    message: str = "[bright_yellow]" + message + "[/]"
    displayController.print(msg_indicator, message, info_icon, end=('\n'*newline))
 

# Print a message that indicates a warning
def warning_msg_display(message: str, newline: int = 1, turn_icon_off=False) -> None:
    warning_icon: str = '' if turn_icon_off else "[blink]:warning-emoji:[/]" 
    msg_indicator: str = '[' + "[bold bright_yellow]" + "WARNING" + "[/]" + ']'
    message = "[bright_yellow]" + message + "[/]"
    displayController.print(msg_indicator, message, warning_icon, end=('\n'*newline))


# Prints a message when an action is not sucessful
def failure_msg_display(message: str, newline: int = 1, turn_icon_off=False) -> None:
    failure_icon: str = '' if turn_icon_off else "[bold]:cross_mark:[/]" 
    msg_indicator: str = '[' + "[bold bright_red]" + "FAILURE" + "[/]" + ']'
    message = "[bright_red]" + message + "[/]"
    displayController.print(msg_indicator, message, failure_icon, end=('\n'*newline))



# Test the functions:
def __test() -> None:
   success_msg_display("This is a simple success message.")
   info_msg_display("This is a simple info message.")
   warning_msg_display("This is a simple warning message.")
   failure_msg_display("This is a simple failure message.")



if __name__ == "__main__":

    __test()

   
# end of source_code
