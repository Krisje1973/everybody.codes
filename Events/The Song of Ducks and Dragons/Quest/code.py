import os, sys
from re import Pattern
from enum import Enum
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("/home/krisje/Projects/everybody.codes/")
from AOCHelper import * 
names = instructions = []

def readinput(Quest):
    filename = Quest.name.lower()[:5] + ".txt"
    filename = f"{os.path.dirname(__file__)}/{filename}"
    global names, instructions
    names,instructions = readinput_arrays_by_newline(filename)
    names = names[0].split(",")
    instructions =  list(map(lambda i: i.replace("R", "").replace("L", "-"), instructions[0].split(",")))
def main():
   
   quest = Quest.q3_notes
   readinput(quest)
   
   func_name = quest.name[:2]
   if hasattr(sys.modules[__name__], func_name):
       getattr(sys.modules[__name__], func_name)()
   else:
       print(f"No function found for {func_name}")
        
def q1():
    pos = 0
    for instr in instructions:
        pos += int(instr)
        pos = max(0, min(pos, len(names)-1))

    print(f"Quest 1: {names[pos]}")
def q2():
    pos = 0
    for instr in instructions:
        pos += int(instr)

    print(f"Quest 2: {names[pos%len(names)]}")
def q3():
    for instr in instructions:
        pos = int(instr) % len(names)
        name = names[pos]
        n0 = names[0]
        names[0] = name
        names[pos] = n0
        
    print(f"Quest 3: {names[0]}")

if __name__ == '__main__':
    main()