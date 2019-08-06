import re
import os

def main():
    f1 = openOriginal()
    origLineArray = loopFile(f1)
    newLineArray = loopOrigLineArray()

def loopOrigLineArray()
    patProgChange = compProgChange()
    patLineChange = compLineChange()
    #flg will indicate if we are modifying the contents of the patch in this area.
    flg = False
    for i,line in enumerate(lineArray):
        #print("line" + str(i) + ": " + line)
        if regexMatch(patProgChange, line):
            nextLine = lineArray[i+1]
            flg = isNprLogic(nextLine)
        else
            #here is where I am going to process the non-header lines..
            #i'll need to make the zrepl changes and the line number changes

def isNprLogic(nextLine):
    if nextLine.endswith(".npr-logic"):
        return True
    else:
        return False

def openOriginal():
    #open a file
    return open("test1.patch","r")

def loopFile(f):
    lineArray = []
    for x in f:
        lineArray.append(x)
    return lineArray

def regexMatch(pattern, x):
    #x is a single line in the file
    #@@ -11,6 +11,6 @@ ohh, its line 10 now
    #the match() function will apply the pre-compiled regex called pattern to the string to search (x)
    match = pattern.match(x)
    if match:
        processLine(match)
    else:
        return

def compLineChange():
    #@@ -11,6 +11,6 @@ ohh, its line 10 now
    # compilation for regex to find line change denotations:
    return re.compile("([\D]+)(-)([\d]+),([\d]+)([\D]+)(\+)([\d]+),([\d]+)([\D]+)")

def compProgChange():
    #compilation for regex to find program changes:
    return re.compile("^[Ii]ndex")

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
