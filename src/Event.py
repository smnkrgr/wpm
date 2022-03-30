import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Event(object):

    def __init__(self, message, is_error=False, exit=False, 
                 is_success=False, level=0):
        # Assign event attributes
        self.message = message
        self.is_error = is_error
        self.is_success = is_success
        self.exit = exit
        self.level = level

        # Format message
        self.message = self.format_message()
        print(self.message)

        # Exit program if required
        if self.exit:
            if is_error:
                sys.exit(1)
            else:
                sys.exit(0)

    def format_message(self):
        message = ""
        if self.level == 1:
            message = " |__ "
        if self.level == 2:
            message = "     |__ "

        if self.is_error:
            message += "[" + bcolors.FAIL + "x" + bcolors.ENDC + "] " \
                    + bcolors.FAIL + "Error" + bcolors.ENDC + \
                    ": " + self.message
        elif self.is_success:
            message += "[" + bcolors.OKGREEN + "+" + bcolors.ENDC + "] " \
                    + bcolors.OKGREEN + "Success" + bcolors.ENDC + \
                    ": " + self.message
        else:
            message += "[-] " + self.message
        if self.exit:
            message += "\nExiting...\n"
        return message


