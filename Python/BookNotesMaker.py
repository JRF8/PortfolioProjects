import string
import os
import datetime

def main():
    f1, pages, freeTxt = promptInput()
    if f1 == False:
        print("BookNotes cancelled")
    elif f1 == "None":
        print("BookNotes cancelled")
    else:
        tStamp = getDateTime()
        f1.write(tStamp + "\n")
        f1.write("Pages: " + pages + "\n")
        f1.write("Notes: " + freeTxt + "\n")

def promptInput():
    try:
        f1 = promptFileLoop()
        if f1 == "Cancel":
            print("Cancelling......")
            return False, False, False
        else:
            pages = input("Enter the pages read: ")
            freeTxt = input("Enter your reading notes: ")
            return f1, pages, freeTxt
    except NameError:
        print("Cancelling......")
        return False, False, False

def promptFileLoop():
    fileFlg = False
    cancelFlg = False
    # will use flags to indicate still accepting input
    while (fileFlg == False) and (cancelFlg == False):
        title = input("Enter a book title: ")
        if title == "":
            cancelFlag = True
        else:
            fname = convertTitleToFile(title)
            f1 = openFile(fname)
            if f1 == "None":
                cancelFlg = True
                return "Cancel"
            else:
                fileFlg = True
                return f1

def convertTitleToFile(title):
    return title.lower().replace(' ','_') + ".txt"

def openFile(fname):
    fullPath = '/Users/jessefrazier/Documents/BookNotes/' + fname
    if os.path.exists(fullPath):
        f1 = open(fullPath,'a+')
        return f1
    else:
        decideNew = input("File doesn't exist, open new? ('yes' if ok)")
        decideNew = str(decideNew).lower()
        if decideNew == "yes":
            f1 = open(fullPath,'w+')
            return f1
        else:
            return "None"

def getDateTime():
    currentDT = datetime.datetime.now()
    return currentDT.strftime("%H:%M %d-%b-%y")

main()
