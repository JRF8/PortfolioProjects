import re
from array import array

def main():
    f1 = openOriginal()
    loopFile(f1)

def openOriginal():
    #open a file
    return open("test1.patch","r")


def loopFile(f):
    for x in f:
        regexMatch(x)

def regexMatch(x):
    #x is a single line in the file
    #@@ -11,6 +11,6 @@ ohh, its line 10 now
    pattern = compiledPattern()
    #the match() function will apply the pre-compiled regex called pattern to the string to search (x)
    match = pattern.match(x)
    if match:
        processLine(match)
    else:
        return

def compiledPattern():
    #@@ -11,6 +11,6 @@ ohh, its line 10 now
    # the following line compiles a regular expression ahead of time for use later
    return re.compile("([\D]+)(-)([\d]+),([\d]+)([\D]+)(\+)([\d]+),([\d]+)([\D]+)")

def processLine(match):
    #match.groups() returns an iterable list of the pieces of the match
    a = []
    for i, s in enumerate(match.groups()):
        if representsInt(s):
            a.append(str(int(s)+1))
        else:
            a.append(s)
    print(a)

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
#def addOne(myIntStr):
    #return str(int(myIntStr) + 1)
main()
