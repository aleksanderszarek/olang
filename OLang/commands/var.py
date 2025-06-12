from structures import Structures
from instructions import Instructions
from random import random
from math import ceil, floor
class VarCommand(Instructions):
    def __init__(self,struc):
        super().__init__()
        self.struc = struc
    def execute(self, name, operation, value, line):
        if isinstance(value, list):
            value = " ".join(value)

        if value.startswith("_"):
            value = self.struc.getValue(value[1:], line)

        if operation == "=":
            self.struc.setValue(name, value, line)
        elif operation in ["+=", "-=", "*=", "/=", "//=", "%=", "**="]:
            current = self.struc.getValue(name, line)
            try:
                new_value = eval(f"{current} {operation[:-1]} {value}")
                self.struc.setValue(name, new_value, line)
            except Exception:
                Instructions().error(3, line, f"Cannot perform {current}{operation[:-1]}{value}")
        elif operation == "=>":
            print(f"[{self.struc.getType(name,line)} {self.struc.getValue(name,line)}]",end="")
        elif operation == "=<":
            self.struc.setValue(name,input(),line)
        elif operation == "=?":
            self.struc.setValue(name,random(),line)
        elif operation == "\\=":
            try:
                self.struc.setValue(name,floor(self.struc.getValue(name,line)),line)
            except:
                Instructions().error(2,line,f"Cannot floor {self.struc.getValue(name,line)}")
        elif operation == "=\\":
            try:
                self.struc.setValue(name,ceil(self.struc.getValue(name,line)),line)
            except:
                Instructions().error(2,line,f"Cannot ceil {self.struc.getValue(name,line)}")
        elif operation == "\\":
            try:
                self.struc.setValue(name,round(self.struc.getValue(name,line)),line)
            except:
                Instructions().error(2,line,f"Cannot round {self.struc.getValue(name,line)}")
        elif operation == "=i":
            try:
                self.struc.setValue(name,int(self.struc.getValue(name,line)),line)
            except:
                Instructions().error(5,line,f"Cannot convert {self.struc.getValue(name,line)} into an intiger")
        elif operation == "=f":
            try:
                self.struc.setValue(name,float(self.struc.getValue(name,line)),line)
            except:
                Instructions().error(2,line,f"Cannot convert {self.struc.getValue(name,line)} into a float")
        elif operation == "=s":
            try:
                self.struc.setValue(name,str(self.struc.getValue(name,line)),line)
            except:
                Instructions().error(2,line,f"Cannot convert {self.struc.getValue(name,line)} into a string")
    def getValue(self, name, line):
        return self.struc.getValue(name,line)
