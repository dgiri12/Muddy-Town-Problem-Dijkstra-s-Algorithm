import pdb
import sys # to get argument from command line
from miscFuncs import processArgs, processStringFromFile, getRandomNumber
from miscFuncs import isPrint, writeTownDataToFile
from dModule import townProcessor 
from graphingFunctions import generateConnections, checkIfGraphConnected
from graphingFunctions import generateTownData, displayTownData
from graphingFunctions import generateTownData2

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


def run2():
    houses = int(input("Enter no of houses:"))
    streets = int(input("Enter no of streets:"))
    contents = generateTownData2(7, houses, streets)
    dTable = townProcessor(contents)
    for i in dTable:
        i.printValues()
    print(checkIfGraphConnected(contents))

def run0():    
    contents = processStringFromFile(processArgs(sys.argv[1:]))
    displayTownData(contents)
    writeTownDataToFile(generateTownData(7))

    dTable = townProcessor(contents)

# --------------------------------------------------------
#the python program sequence
if __name__ == "__main__": # run code only if this program
    # instance is the main process
    run2()

