import string
import os

def main():
    f1, pages, freeTxt = promptInput()
    if f1 == False:
        print("BookNotes cancelled")
    else:
        getDateTime()

def promptInput():
    try:
        f1 = promptFileLoop()
        pages = prompt("Enter the pages read: ")
        freeTxt = prompt("Enter your reading notes: ")
        return f1, pages, freeTxt
    except NameError:
        print("Cancelling......")
        return False, False, False

def promptFileLoop():
    fileFlg = False
    cancelFlg = False
    # will use flags to indicate still accepting input
    while (fileFlg == False) and (cancelFlag == False)
        title = prompt("Enter a book title: ")
        if title = "":
            cancelFlag == True
        else
            fname = convertTitleToFile(title)
            f1 = openFile(fname)
            if f1 == "None"
                cancelFlg = True
            else
                fileFlg = True
                return f1

def convertTitleToFile(title):
    return title.lower().replace(' ','_') + ".txt"

def openFile(fname):
    fullPath = '~/Documents/BookNotes/' + fname
    if os.path.exists(fullPath):
        f1 = open(fullPath,'a')
    else:
        decideNew = prompt("File doesn't exist, open new? ('yes' if ok)")
        decideNew = str(decideNew).lower()
        if decideNew == "yes":
            f1 = open(fullPath,'w')
        else
            return "None"

def getDateTime():
