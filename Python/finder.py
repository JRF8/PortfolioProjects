import re

def main():
    f = openFile()
    loopFile(f)

def openFile():
    #open a file
    f = open("test1.patch","r")
    return f

def loopFile(f):
    for x in f:
        regexMatch(x)

def regexMatch(x):
    #x is a single line in the file
    #@@ -11,6 +11,6 @@ ohh, its line 10 now
    match = re.search("(@@ )(-\d+,\d+)( )(\+\d+,\d+)",x)
    if match:
        processLine(x)
    else:
        return

def processLine(x):
    #x is the line found by our regular expression search
    #for now, let's just print what we have until this is completed.
    print(x)
main()
