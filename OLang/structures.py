from colorama import Fore
from instructions import Instructions

inst = Instructions()

class Structures:
    def __init__(self):
        self.structures = {}

    def setValue(self, name, value, line):
        if type(value) == str:
            if str(value).startswith('"') and str(value).endswith('"'):
                value = value[1:-1]
            elif value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
        else:
            try:
                value = float(value) if '.' in str(value) else int(value)
            except ValueError:
                inst.error(5, line)
                return
        self.structures[name] = value

    def getValue(self, name, line):
        if name not in self.structures:
            inst.error(6, line)
            return None
        return self.structures[name]

    def getType(self, name, line):
        if name not in self.structures:
            inst.error(6, line)
        if self.structures[name] in [True, False]:
            return "boolean"
        r = type(self.structures[name])
        if r in [int, float]:
            return "number"
        elif r in [str, chr]:
            return "string"
        
    def delValue(self, name, line):
        if name not in self.structures:
            inst.error(6, line)
            return
        del self.structures[name]
