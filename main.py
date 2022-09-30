import pdb
import sys # to get argument from command line
from miscFuncs import processArgs, processStringFromFile, getRandomNumber
from miscFuncs import isPrint, writeTownDataToFile
from miscFuncs import readPavingDataFromFile, writePavingStringToFile
from miscFuncs import displayPavingData, generatePavingStringFromDTable
from dModule import townProcessor, printDTable
from townFunctions import generateConnections, checkIfTownConnected
from townFunctions import generateTownData, displayTownData
from townFunctions import confirmPavingPlan

#MAIN PROGRAM FUNCTION:

def run1():
    townData = processStringFromFile("MiniTown.dat")
    pavingString = readPavingDataFromFile("MiniTownPavingPlan.dat")
    displayPavingData(townData, pavingString)
    
def run3():
    houses = int(input("Enter no of houses:"))
    streets = int(input("Enter no of streets:"))
    seed = int(input("Enter a seed:"))
    townData = generateTownData(seed, houses, streets)
    dTable = townProcessor(townData)
    printDTable(dTable)
    if checkIfTownConnected(townData):
        print("Graph is connected!")
    else:
        print("Graph is not connected...")

    pavingPlanName = townData[0] + " paving plan"
    pavingString = generatePavingStringFromDTable(pavingPlanName, dTable)
    displayPavingData(townData, pavingString)
    if str(input("Wanna save paving plan? (Y/N)")) == "Y":
        writePavingStringToFile(pavingString)

def run2():
    townData = processStringFromFile("Town1.dat")
    pavingString = readPavingDataFromFile("Town1UnConPavPlan.dat")

    print(confirmPavingPlan(townData, pavingString))

# --------------------------------------------------------
#the python program sequence
if __name__ == "__main__": # run code only if this program
    # instance is the main process
    run2()

