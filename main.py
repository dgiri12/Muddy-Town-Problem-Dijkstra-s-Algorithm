import pdb
import sys # to get argument from command line
from miscFuncs import processArgs, processStringFromFile, getRandomNumber
from miscFuncs import isPrint, writeTownDataToFile
from dModule import townProcessor, printDTable
from graphingFunctions import generateConnections, checkIfGraphConnected
from graphingFunctions import generateTownData, displayTownData

#MAIN PROGRAM FUNCTION:
def run2():
    houses = int(input("Enter no of houses:"))
    streets = int(input("Enter no of streets:"))
    seed = int(input("Enter a seed:"))
    contents = generateTownData(seed, houses, streets)
    dTable = townProcessor(contents)
    printDTable(dTable)
    if checkIfGraphConnected(contents):
        print("Graph is connected!")
    else:
        print("Graph is not connected...")

# --------------------------------------------------------
#the python program sequence
if __name__ == "__main__": # run code only if this program
    # instance is the main process
    run2()

