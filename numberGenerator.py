import re
import sys

def startProgram():
    sys.tracebacklimit = 0
    NPA = int(sys.argv[2])
    NXX = 200
    XXXX = 0000
    global phoneList
    global fileOption
    fileOption = sys.argv[1]
    if fileOption == 'file':
        phoneList = open(str(NPA)+'PhoneList', 'a+')
    numberCreation(NPA, NXX, XXXX)

def numberCreation(NPA, NXX, XXXX):
    while (NXX < 1000):
        number = str(NPA)+str(NXX)+str(XXXX).zfill(4)
        if fileOption == 'file':
            phoneList.write(number+'\n')
        if fileOption == 'stream':
            print(number)

        XXXX += 1

        if XXXX == 10000:
            NXX += 1
            XXXX = 0000

        if re.match('[2-9][1][1]', str(NXX)) is not None:
            NXX += 1

        if NXX == 555 and XXXX == int ('0100'):
            XXXX = int('0200')

startProgram()

# Wanted Changes
# 1. Add Specific Area Code or All Area Code Options
# 2. Fix Errors on Completion
