import re
import os

def main():
    f1 = openOriginal()
    origLineList = loopFile(f1)
    newLineList = loopOrigLineList(origLineList)

def loopOrigLineList(lineList):
    patProgChange = compProgChange()
    patLineChange = compLineChange()
    newLineList = []
    newLineSubList = []
    #flg will indicate if we are modifying the contents of the patch in this area.
    for line in lineList:
        #print("line" + str(i) + ": " + line)
        if regexMatch(patProgChange, line):
            newLineList = appendAList(newLineList, newLineSubList)
            newLineSubList = []
            newLineSubList.append(line)
        else:
            newLineSubList.append(line)
    newLineList = appendAList(newLineList, newLineSubList)
    for subList in newLineList:
        print(subList)
        
def appendAList(a1, a2):
    #a2 is the list to append to the target list, a1
    #don't want to append a2 to a1 if a2 is empty
    if not a2:
        return []
    else:
        a1.append(a2)
    return a1

def isNprLogic(nextLine):
    if nextLine.endswith(".npr-logic"):
        return True
    else:
        return False

def openOriginal():
    #open a file
    return open("test1.patch","r")

def loopFile(f):
    lineList = []
    for x in f:
        lineList.append(x)
    return lineList

def regexMatch(pattern, x):
    #x is a single line in the file
    #@@ -11,6 +11,6 @@ ohh, its line 10 now
    #the match() function will apply the pre-compiled regex called pattern to the string to search (x)
    match = pattern.match(x)
    if match:
        return True
    else:
        return False

def compLineChange():
    #@@ -11,6 +11,6 @@ ohh, its line 10 now
    # compilation for regex to find line change denotations:
    return re.compile("([\D]+)(-)([\d]+),([\d]+)([\D]+)(\+)([\d]+),([\d]+)([\D]+)")

def compProgChange():
    #compilation for regex to find program changes:
    return re.compile("^[Dd]iff")

def processLine(match):
    #match.groups() returns an iterable list of the pieces of the match
    a = []
    for i, s in enumerate(match.groups()):
        if representsInt(s):
            v = addToLineNums(s)
            a.append(v)
        else:
            a.append(s)
    print(a)

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def addToLineNums(myStr):
    return str(int(myStr)+2)

main()
