from structures import Structures
from instructions import Instructions
from colorama import Fore
from sys import getsizeof
import time
class ReturnCommand(Instructions):
    def execute(self,code, start_time, struc):
        end_time = time.perf_counter()
        print("\n\n")
        if code == 0:
            print(Fore.GREEN + f"Code stopped with a status code 0.\n" + Fore.RESET + f"Code execution took {end_time-start_time:.6f} seconds.\nFreed up {getsizeof(struc)} bytes.")
        else:
            print(Fore.RED + f"Code stopped with an error code {code}")
            print(Fore.RESET + f"Code execution took {end_time-start_time:.6f} seconds.\nFreed up {getsizeof(struc)} bytes.")
        input("Press ENTER to exit...")    
        exit()
