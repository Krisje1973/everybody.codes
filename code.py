import os, sys
from re import Pattern
from enum import Enum
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("/home/krisje/Projects/everybody.codes/")
from AOCHelper import * 
grid = tokens = []

def main():
   
   quest = Quest.q1_example
   readinput(quest)
   
   func_name = quest.name[:2]
   if hasattr(sys.modules[__name__], func_name):
       getattr(sys.modules[__name__], func_name)()
   else:
       print(f"No function found for {func_name}")

def readinput(Quest):
    filename = Quest.name.lower()[:5] + ".txt"
    filename = f"{os.path.dirname(__file__)}/{filename}"
    global grid, tokens
    grid,tokens = readinput_arrays_by_newline(filename)
        
def q1():
    print("Quest 1")
def q2():
    print("Quest 2")
def q3():
    print("Quest 3")

if __name__ == '__main__':
    main()