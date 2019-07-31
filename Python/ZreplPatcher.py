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
#-------PSEUDO CODE----------
# connect to SVN, get revisions
# from revisions, generate patches
# also, recognize and grab appropriate code
# create working directory, place code in there
# also have parallel backup directory with copy of the code
# read .patch files and overwrite with zrepl appropriate changes
# apply .patch to zrepls in working directory, flag any conflicts
# make this code modular, with a gui
#-------MAIN CALL-----
main()
