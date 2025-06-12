from commands.var import VarCommand
from commands.print import PrintCommand
from commands.nl import NLCommand
from commands.jump import JumpCommand
from commands.if_statement import IfCommand
from commands.return_statement import ReturnCommand
from commands.wait import WaitCommand
from instructions import Instructions
from structures import Structures
import time
import os, sys
import ctypes
start_time = time.perf_counter()
struc = Structures()
inst = Instructions()

lineCount = 0
if_command = None
if_stack = []
if len(sys.argv) != 2:
    print("Usage: OLang <file.o>")
    input("Press ENTER to exit...")
    sys.exit(1)
file_path = sys.argv[1]
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    input("Press ENTER to exit...")
    sys.exit(1)
with open(file_path, "r") as code:
    ctypes.windll.kernel32.SetConsoleTitleW(file_path)
    codelines = [line.strip() for line in code.readlines()]
    while lineCount < len(codelines):
        line = codelines[lineCount]
        chunks = line.split(" ")
        command = chunks[0]
        args = chunks[1:]
        if command == "#":
            lineCount += 1
            continue
        if if_stack and if_stack[-1].should_skip() and command != "endif":
            lineCount += 1
            continue
        if command == "if":
            if_command = IfCommand(struc)
            condition = " ".join(args)
            should_skip = if_command.execute(condition, lineCount)
            if_stack.append(if_command)
        elif command == "endif":
            if not if_stack:
                inst.error(7, lineCount)
            else:
                if_stack.pop()
        else:
            if if_stack and if_stack[-1].should_skip():
                lineCount += 1
                continue
        if command == "print":
            PrintCommand(struc).execute(args, lineCount)
        elif command == "var":
            name = args[0]
            operation = args[1]
            value = args[2:]
            VarCommand(struc).execute(name, operation, value, lineCount)
        elif command == "nl":
            count = args[0] if args else "1"
            if str(count).startswith("_"):
                count = struc.getValue(str(count)[1:],line)
            try:
                count = int(count)
            except:
                inst.error(2,line,"Line count must be an intiger")
                continue
            NLCommand().execute(count)

        elif command == "jump":
            target = args[0]
            lineCount = JumpCommand().execute(lineCount, target)
            continue
        elif command == "wait":
            target = args[0]
            WaitCommand().execute(lineCount, target)
        elif command == "return":
            if args:
                code = args[0]
            else:
                code = 0
            ReturnCommand().execute(code,start_time,struc)
            continue
        lineCount += 1
    inst.error(8,lineCount,"Main does not have a return statement.")