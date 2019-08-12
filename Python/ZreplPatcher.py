#!/usr/bin/python
#----IMPORTS-----
import fileinput
import sys
#----FUNCTION DEFINITIONS-------
def main():
    find_replace()
def find_replace():
    for line in fileinput.FileInput("test.txt", inplace=1):
        char = line[0]
        if char == "+":
            char=char.replace("+","+~~",1)
            sys.stdout.write(char + line[1:])
        elif char == "-":
            char=char.replace("-","+;~",1)
            sys.stdout.write("-" + line[1:])
            sys.stdout.write(char + line[1:])
        else:
            sys.stdout.write(line)
#-------MAIN CALL-----
main()
