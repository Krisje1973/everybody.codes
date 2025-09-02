import os, sys
from re import Pattern
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\Devops\everybody.codes")
from AOCHelper import * 
input = []

def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    input = readinput_lines(filename)

def main():
   readinput("notes_ex.txt")
   first_star()       
   #second_star()
 
def first_star():
    print(input)

def second_star():
    print("Result Second Star")

if __name__ == '__main__':
    main()