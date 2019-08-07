import re
import os

def main():
    f1 = openOriginal()
    origLineList = loopFile(f1)
    newLineList = loopOrigLineList(origLineList)
    processedList = []
    for singlePgm in newLineList:
        processedList = processList(singlePgm)

def loopOrigLineList(lineList):
    patProgChange = compProgChange()
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
    return newLineList

def appendAList(a1, a2):
    #a2 is the list to append to the target list, a1
    #don't want to append a2 to a1 if a2 is empty
    if not a2:
        return []
    else:
        a1.append(a2)
    return a1

def isNprLogic(line):
    print(line)
    if line.endswith(".npr-logic\n"):
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

def compPgmInfo():
    #--- a/test1.npr-logic
    #compilation for regex to locate pgm name line
    return re.compile("[-+]{3} .*.npr-[\w]+")

def processList(singlePgm):
    #line at index 2
    if isNprLogic(singlePgm[2]):
        return manipList(singlePgm)
    else:
        return singlePgm

def manipList(singlePgm):
    #first let's gather the index locations of all line change tags
    iLoc = []
    patLineChange = compLineChange()
    for i, line in enumerate(singlePgm):
        if regexMatch(patLineChange, line):
            iLoc.append(i)
    #now time to look for the - lines we are replacing.
    counter = 0
    for n, i in enumerate(iLoc):
        if nextILoc(n+1, iLoc):
            counter += processLineRange(singlePgm, i, iLoc[n+1])
        else:
            counter += processLineRange(singlePgm, i, "none")
    print(counter)

def processLineRange(singlePgm, begin, end):
    count = 0
    pgmInfoLine = compPgmInfo()
    if representsInt(end):
        for line in singlePgm[begin:end]:
            if regexMatch(pgmInfoLine, line):
                None
            elif line[0] == "-":
                count+=1
    else:
        for line in singlePgm[begin:]:
            if regexMatch(pgmInfoLine, line):
                None
            elif line[0] == "-":
                count+=1
    return count

def nextILoc(n, iLoc):
    try:
        v = iLoc[n]
        return True
    except IndexError:
        return False

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def addToLineNums(myStr):
    return str(int(myStr)+2)

main()
