import pdb
import sys # to get argument from command line
from miscFuncs import processArgs, processStringFromFile, getRandomNumber
from miscFuncs import isPrint
from dModule import townProcessor 
from graphingFunctions import generateConnections, checkIfGraphConnected
from graphingFunctions import generateTownData

#MAIN PROGRAM FUNCTION:
def run1():
    m = 0
    while m < 100:
        try:
            seedx = generateTownData(m)
        except:
            m += 1
            continue # if bad seed encountered, skip to next
        condition = checkIfGraphConnected(seedx)
        if (condition==False):
            print("Is seed"+str(m)+" a connected graph?")
            print(condition)
        m += 1
    print("End of run1")


def run0():    
    contents = processStringFromFile(processArgs(sys.argv[1:]))
    dTable = townProcessor(contents)

    for i in dTable:
        i.printValues()

# --------------------------------------------------------
#the python program sequence
if __name__ == "__main__": # run code only if this program
    # instance is the main process
    run1()

