from structures import Structures
from instructions import Instructions

class PrintCommand(Instructions):
    def __init__(self,struc):
        super().__init__()
        self.struc = struc
    def execute(self, args, line):
        output = []
        for arg in args:
            if arg.startswith("_"):  # Check if it's a variable
                value = self.struc.getValue(arg[1:], line)
                if value is not None:
                    output.append(str(value))
                else:
                    self.error(2, line)  # Variable not defined
                    return
            else:
                output.append(arg)

        print(" ".join(output), end="")
