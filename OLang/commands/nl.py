from structures import Structures
from instructions import Instructions

class NLCommand(Instructions):
    def execute(self, count):
        print("\n" * int(count), end="")
