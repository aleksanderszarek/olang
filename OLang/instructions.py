from colorama import Fore
from sys import exit

class Instructions:
    def error(self, id, line=None, details=""):
        errors = {
            0: "Unknown error",
            1: "Syntax error",
            2: "Type error",
            3: "Math error",
            4: "Variable name error",
            5: "Variable assign error",
            6: "Variable not defined",
            7: "Unexpected endif",
            8: "Structural error"
        }
        message = errors.get(id, "Unknown error")
        line_info = f" Line {line+1}:" if line else ""
        if id in [5,7]:
            print(Fore.YELLOW + f"\nCompiler encountered an error:\n\n {line_info} {message}. {details}" + Fore.RESET)
        else:
            print(Fore.RED + f"\nProgram execution failed due to a critical error:\n\n {line_info} {message}. {details}" + Fore.RESET)
            input("Press ENTER to exit...")
            exit()