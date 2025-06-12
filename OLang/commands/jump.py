from structures import Structures
from instructions import Instructions

struc = Structures()
class JumpCommand(Instructions):
    def execute(self, lineCount, target):
        try:
            return int(target) - 1
        except ValueError:
            self.error(2, lineCount)
            return lineCount
