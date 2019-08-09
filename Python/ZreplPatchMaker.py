import re
import os

def main():
    f1 = openOriginal()
    origLineList = loopFile(f1)
    newLineList = loopOrigLineList(origLineList)
    processedList = []
    for singlePgm in newLineList:
        processedList.append(processList(singlePgm))
    f2 = openNew()
    for singlePgm in processedList:
        for line in singlePgm:
            f2.write(line)
    f2.close()

def loopOrigLineList(lineList):
    patPgmInfo = compPgmInfo()
    newLineList = []
    newLineSubList = []
    #flg will indicate if we are modifying the contents of the patch in this area.
    for line in lineList:
        if regexMatch(patPgmInfo, line):
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
    patPgmInfo = compPgmInfo()
    if regexMatch(patPgmInfo, line) == False:
        return False
    elif patPgmInfo.match(line).group(3) != ".npr-logic":
        return False
    else:
        return True

def openOriginal():
    #open a file
    return open("test1.patch","r")

def openNew():
    os.remove("test2.patch")
    return open("test2.patch","a")

def loopFile(f):
    lineList = []
    for x in f:
        lineList.append(x)
    return lineList

def regexMatch(pattern, x):
    #THIS WILL NOT RETURN A MATCH OBJECT
    #it will instead return a boolean object
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
    return re.compile("([\D]+)(-)([\d]+)(,)([\d]+)([\D]+)(\+)([\d]+)(,)([\d]+)([\D]+)(.+)(\n)")

def compPgmInfo():
    #compilation for regex to find program name info
    return re.compile("(^[Ii]ndex)(.+)(.npr-[\w]+)(.+)")

def compPgmChange():
    #--- a/test1.npr-logic
    #compilation for regex to locate the +/- info for the pgm
    return re.compile("[-+]{3} .*.npr-[\w]+")

def compPlusMinus():
    return re.compile("^[-+]")

def processList(singlePgm):
    #top line of singlePgm should be the pgm info
    if isNprLogic(singlePgm[0]):
        singlePgm = manipLineNums(singlePgm)
        singlePgm = manipZreplLines(singlePgm)
        return singlePgm
    else:
        return singlePgm

def manipLineNums(singlePgm):
    #this function will go through and replace the line numbers
    #first let's gather the index locations of all line change tags
    newSinglePgm = []
    iLoc = []
    patLineChange = compLineChange()
    for i, line in enumerate(singlePgm):
        if regexMatch(patLineChange, line):
            iLoc.append(i)
    #now time to look for the - lines we are replacing.
    rollingCounter = 0
    for n, i in enumerate(iLoc):
        counter = 0
        if nextILoc(n+1, iLoc):
            counter = processLineRange(singlePgm, i, iLoc[n+1])
        else:
            counter = processLineRange(singlePgm, i, "none")
        #we want to add the current section's counter first before we add
        #that amount to the rolling counter
        modifiedLine = modifyChangeIndicatorLine(singlePgm, i, counter, rollingCounter)
        singlePgm[i] = modifiedLine
        rollingCounter += counter
    return singlePgm


def processLineRange(singlePgm, begin, end):
    #this is where we will count the number of - lines in a section
    count = 0
    patPgmChange = compPgmChange()
    if representsInt(end):
        for line in singlePgm[begin:end]:
            if regexMatch(patPgmChange, line):
                None
            elif line[0] == "-":
                count+=1
    else:
        for line in singlePgm[begin:]:
            if regexMatch(patPgmChange, line):
                None
            elif line[0] == "-":
                count+=1
    return count

def isPlusMinusLine(line):
    patPgmChange = compPgmChange()
    patPlusMinus = compPlusMinus()
    if regexMatch(patPgmChange, line):
        return False
    elif regexMatch(patPlusMinus, line):
        return True
    else:
        return False

def modifyChangeIndicatorLine(singlePgm, i, counter, rollingCounter):
    line = singlePgm[i]
    patLineChange = compLineChange()
    lineMatch = patLineChange.search(line)
    replLine = []
    # groups 3,5,8,10 are the numbers
    # 3 and 5 represent where the removed section begins, and the section size
    # 8 and 10 represent where the new section begins, and the section size
    # the rolling counter will affect where the sections begin, not the size of them
    # the counter will affect the size of the added section
    #there are 14 groups from 1 - 14
    for n in range(1,14):
        if (n==10):
            replLine.append(strIntAdder(lineMatch.group(n),counter))
        elif (n==3)|(n==8):
            replLine.append(strIntAdder(lineMatch.group(n),rollingCounter))
        else:
            replLine.append(lineMatch.group(n))
    return ''.join(replLine)

def strIntAdder(target, addedAmt):
    return str(int(target) + addedAmt)

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

def manipZreplLines(singlePgm):
    newSinglePgm = []
    for line in singlePgm:
        if isPlusMinusLine(line):
            if line[0] == '-':
                newSinglePgm.append(line)
                newSinglePgm.append("+;~" + line[1:])
            else: #must be a plus line
                newSinglePgm.append("+~~" + line[1:])
        else:
            newSinglePgm.append(line)
    return newSinglePgm

main()
