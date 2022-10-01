import datetime
import pdb
from os.path import exists
from dModule import townProcessor
from miscFuncs import processStringFromFile
from pavingFunctions import confirmPavingPlan, displayPavingData, findMinCostPavingPlan, generatePavingStringFromDTable, isMinPavingPlanCost, readPavingDataFromFile, writePavingStringToFile
from townFunctions import generateTownData, writeTownDataToFile
from miscFuncs import getRandomNumber
import random

def loadTown():
    while True:
        filename = str(input("Please enter the file name of the town:"))
        fileExists = exists(filename)
        if fileExists == False:
            print("File doesn't exist, try another")
            continue
        break

    townData = processStringFromFile(filename)

    print("Successfully loaded!")
    for i in townData:
        print(i)
    print("------------------------------------------------")

def generateTown():
    while True:
        try:
            houses = int(input("Enter no of houses:"))
            streets = int(input("Enter no of streets:"))
            seed = int(input("Enter a seed (seed > 0):"))
        except:
            print("Bad value,try again")
            continue
        if seed <= 0:
            print("Bad value,try again")
            continue
        if houses <= 0:
            print("Bad value,try again")
            continue
        if streets <= 0:
            print("Bad value,try again")
            continue
        
        townData = generateTownData(seed, houses, streets)

        for i in townData:
            print(i)

        writeTownDataToFile(townData)

        break
        
def generateMinimumCostPavingPlan():
    while True:
        filename = str(input("Please enter the file name of the town:"))
        fileExists = exists(filename)
        if fileExists == False:
            print("File doesn't exist, try another")
            continue
        break
    print("Minimum paving cost for this town is " + str(findMinCostPavingPlan(filename)))

    # now save the paving plan
    townData = processStringFromFile(filename)
    pavingString = generatePavingStringFromDTable(townData[0]+"pavingplan", townProcessor(townData))
    writePavingStringToFile(pavingString)

def loadPavingDataNCost():
    while True:
        filename = str(input("Please enter the file name of the town:"))
        fileExists = exists(filename)
        if fileExists == False:
            print("File doesn't exist, try another")
            continue
        break

    while True:
        filename2 = str(input("Please enter the file name of the paving plan associated with this town:"))
        fileExists = exists(filename2)
        if fileExists == False:
            print("File doesn't exist, try another")
            continue
        break
    
    townData = processStringFromFile(filename)
    pavingString = readPavingDataFromFile(filename2)
    
    displayPavingData(townData, pavingString)

def isPavingValid():
    while True:
        filename = str(input("Please enter the file name of the town:"))
        fileExists = exists(filename)
        if fileExists == False:
            print("File doesn't exist, try another")
            continue
        break

    while True:
        filename2 = str(input("Please enter the file name of the paving plan associated with this town:"))
        fileExists = exists(filename2)
        if fileExists == False:
            print("File doesn't exist, try another")
            continue
        break

    townData = processStringFromFile(filename)
    pavingString = readPavingDataFromFile(filename2)
    condition = confirmPavingPlan(townData, pavingString)

    if condition == True:
        print("Yes the paving plan is valid")
    else:
        print("No, paving plan is not valid")


def isMinimum():
    while True:
        filename = str(input("Please enter the file name of the town:"))
        fileExists = exists(filename)
        if fileExists == False:
            print("File doesn't exist, try another")
            continue
        break

    while True:
        filename2 = str(input("Please enter the file name of the paving plan associated with this town:"))
        fileExists = exists(filename2)
        if fileExists == False:
            print("File doesn't exist, try another")
            continue
        break

    condition = isMinPavingPlanCost(filename, filename2)
    if condition:
        print("Yes the paving plan for this town shows minimum cost")
    else:
        print("No, the paving plan for this town doesn't show the minimum cost")

def histogram():
    startTime = datetime.datetime.now()

    seed = 3
    for i in range(0,10000):
        seed = getRandomNumber(seed)
        print(seed)
    endTime = datetime.datetime.now()

    deltaTime1 = (endTime - startTime)
    millis1 = deltaTime1.total_seconds() * 1000
    

    startTime = datetime.datetime.now()
    for i in range(0,10000):
        n = random.random()
        print(n)
    endTime = datetime.datetime.now()

    deltaTime2 = (endTime - startTime)
    millis2 = deltaTime2.total_seconds() * 1000

    print("Time taken by LCG: " + str(millis1))
    histoString = ""
    for i in range(0,int(millis1)):
        histoString += "#"
    print(histoString)

    print("Time taken by python -> import random: " + str(millis2))
    histoString = ""
    for i in range(0,int(millis2)):
        histoString += "#"
    print(histoString)

    pass

#MAIN PROGRAM FUNCTION: ---------------------------------------------

def run_program():
    print("Welcome to townify!")
    while True:
        print("Please choose an option number from the following:")
        print("1. Load town and display town")
        print("2. Generate Random Town")
        print("3. Generate a minimum cost paving plan for a town")
        print("4. Load and Display Paving Data and Paving Cost")
        print("5. Load a paving plan and test if its valid")
        print("6. Load a paving plan and test if it gives minimum cost")
        print("7. LCG vs stdlib histogram demonstration")
        print("0. Exit")
        
        while True:
            try:
                choice = int(input("Choice number?"))
            except:
                print("Bad choice, try again.")
                continue
            if choice > 8:
                print("Bad choice, try again.")
                continue
            if choice < 0:
                print("Bad choice, try again.")
                continue
            break

        if choice == 0:
            break

        if choice == 1:
            loadTown()
            continue
        
        if choice == 2:
            generateTown()
            continue

        if choice == 3:
            generateMinimumCostPavingPlan()
            continue

        if choice == 4:
            loadPavingDataNCost()
            continue

        if choice == 5:
            isPavingValid()
            continue

        if choice == 6:
            isMinimum()
            continue

        if choice == 7:
            histogram()
            continue

# ----------------------------------------------------------------------
#the python program sequence
if __name__ == "__main__": # run code only if this program
    # instance is the main process
    run_program()

