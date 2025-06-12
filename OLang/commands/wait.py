from structures import Structures
from instructions import Instructions
from time import sleep
struc = Structures()
class WaitCommand(Instructions):
    def execute(self, lineCount, target):
        try:
            sleep(int(target))
        except ValueError:
            self.error(2, lineCount, f"Cannot wait {target} seconds")
