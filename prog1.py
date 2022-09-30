import pdb
import sys # to get argument from command line
from funcs import processArgs, processStringFromFile, getRandomNumber
from funcs import isPrint
from dModule import townProcessor, getHouseList, findInTable 
from connections import generateConnections


# use this to test the random number function
# syntax: printRandomNumbers(3, 100)
def printRandomNumbers(_seed, _range):
    for i in range(_range):
        _seed = getRandomNumber(_seed)
        print("Random: ", str(_seed))

# generates a random town data as string values
# manually verified: it generates enoughly random, completely
# connected, and both cyclic and acyclic graphs.
# the townProcessor() function can function with acyclic graph as well
def generateTownData(_seed):
    # generate a random list of houses
    _seed = getRandomNumber(_seed)
    totalNoOfHouses = _seed # now assign the random value
    if isPrint(): print("TotalNoOfHouses=" + str(totalNoOfHouses))
    # here you initialize the houselist
    houseList = []
    houseCounter = 0
    houseSeed = 0

    while houseCounter < totalNoOfHouses:
        houseSeed += 1
        houseName = str(getRandomNumber(houseSeed))\
                + " Denver Street"
        # check if house names exists, otherwise regenerate name
        while houseName in houseList:
            houseSeed += 1
            houseName = str(getRandomNumber(i)) 
            + " Denver Street"
        houseList.append(houseName)
        houseCounter += 1 # a house finally added, count that

    if isPrint(): print("HouseList[]:")
    if isPrint(): print(houseList)

    
    # generate a new seed
    _seed = getRandomNumber(_seed)
    # feed that seed into the connection generator including
    # the list of houses to be connected
    stringList = generateConnections(houseList, _seed)
    if len(stringList) == 0:
        raise Exception("Bad seed, choose different seed value\
 to generate town data")

    # this generated string list is of the form,
    # "-1,A,B", the 1stfield ie pavingCost is randomized and 
    # entered now
    
    # we are just reading old list line by line, modifying
    # the value to include a pavingCost, then pushing those
    # values into a new list
    stringListWithPavingCost = []

    for i in stringList: # so that loop runs as long as houseList
        _seed = getRandomNumber(_seed)
        stringListWithPavingCost.append(
                i.replace("-1",str(_seed)))
    # add the town name bruv
    stringListWithPavingCost.insert(0,str(getRandomNumber(_seed)) +
            " Town")
    if isPrint(): print ("THE FINAL TOWN DATA:")
    if isPrint(): print (stringListWithPavingCost)
    return stringListWithPavingCost

# checks if the generated graph is connected
# takes in a completed town data as an argument
# complete with pavingCost and connections
# how it works: when the djikstra Algo prints out
# dTable of a disconnected graph, one of the 
# vertices will still have infinity value,
# that's how you know if the graph is disconnected

# even after updated accurate algorithm,
# generate doesn't create a single disconnected graph
# impressive ...

def checkIfGraphConnected(townData):
    dTable = townProcessor(townData)

    for i in dTable:
        if i.shortest == -1:
            return False
    return True

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

unconnectedGraph = [
        "1,A,B",
        "3,B,E",
        "4,A,C",
        "7,B,C",
        "2,D,E",
        "5,F,G"
        ]

def run2():
    dTable = townProcessor(unconnectedGraph)
    for i in dTable:
        i.printValues()

# --------------------------------------------------------
#the python program sequence
if __name__ == "__main__": # run code only if this program
    # instance is the main process
    run1()

