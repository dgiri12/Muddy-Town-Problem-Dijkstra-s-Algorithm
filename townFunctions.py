import pdb
from miscFuncs import getRandomNumber, isPrint, isEven, sumOfDigits
from miscFuncs import processStringFromFile
from dModule import townProcessor, getHouseList
from edgesCalc import addEdge, isConnected

# this program is for generating a stringList that will
# convey randomized connection between a list of houses

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

def checkIfTownConnected(townData):
    print("Checking if town is connected...")
    dTable = townProcessor(townData)

    for i in dTable:
        if i.shortest == -1:
            return False
    return True

# function that displays stored town data
# your data structure itself is the stringList...
def displayTownData(townData):
    print("Name of Town: " + townData[0])
    for i in townData:
        lines = i.split(",")
        try:
            print(lines[1] + " is connected to " + lines[2] + " with paving cost " + lines[0])
        except IndexError:
            continue # to skip line with town name
        

# second type of function for generating town data, which doesn't use seed,
# but accepts user input to get how many houses and streets
def generateTownData(_seed, noOfHouses, noOfStreets):
    print("Generating town data...")
    if isPrint(): print("TotalNoOfHouses=" + str(noOfHouses))
    if isPrint(): print("TotalNoOfStreets==" + str(noOfStreets))

    # here you initialize the houselist
    houseList = []
    houseCounter = 0
    houseSeed = 0

    while houseCounter < noOfHouses:
        houseSeed += 1
        houseName = str(getRandomNumber(houseSeed))\
                + " Denver Street"
        # check if house names exists, otherwise regenerate name
        while houseName in houseList:
            houseSeed += 1
            houseName = str(getRandomNumber(houseSeed)) + " Denver Street"
        houseList.append(houseName)
        houseCounter += 1 # a house finally added, count that

    if isPrint(): print("HouseList[]:")
    if isPrint(): print(houseList)
    
    stringList = generateConnections(_seed, houseList, noOfStreets)
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

# a second version, which generates connections not from a seed,
# but from user specified number of streets
# returns a stringList
def generateConnections(_seed, houseList, noOfStreets):
    print("Generating connections...")
    if isPrint(): print("generateConnections()->start")

    stringList = [] # the final vessel of the connections
    # usually the leftmost value is pavingCost, but put that as '-1'
    # since that is not the scope of this file

    # loop should start after stringList declaration
    i = 0
    size = len(houseList)
    filled = False
    if isPrint(): print ("len(houseList):" + str(size))
    while True:
        # check if time to terminate loop
        if i == size: break

        if noOfStreets == 0: # randomly made streets have fullfilled quota
            filled = True
            break

        if isPrint(): print("---iteration----i = " + str(i))
        visitedList = [] # this list should be new for each currentVertex

        currentVertex = houseList[i]
        if isPrint(): print("currentVertex: " + currentVertex)
        visitedList.append(currentVertex)
        neighbours = []
        # in case a connection has already been made from currentVertex,
        # the neighbours need to be taken out of consideration
        # a new neighbours list for each new currentVertex iteration

        # first fill the neighbour list by iterating the houselist for
        # connections that might have been made in the past iteration
        for index, j in enumerate(stringList): # you are checking the 
            # list currently being made, in order to 
            # see any newly created neighbours

            # if stringList empty, skip
            if j == "": continue
            line = j.split(",")
            if line[1] == currentVertex:
                neighbours.append(line[2])
            # now for the reverse order, find neighbours
            if line[2] == currentVertex:
                neighbours.append(line[1])
            # as long as connections in stringList are not repeated as
            # in "6,A,B" and "6,B,A", there will be no duplicate
            # neighbours

        if isPrint(): print("Neighbours:")
        if isPrint(): print(neighbours)


        for k in houseList:
            if k in visitedList: continue # skip the visited houses
            if k in neighbours: continue # skip house if connection 
            # already exists
            _seed = getRandomNumber(_seed)
            if isEven(sumOfDigits(_seed)): # this is a coin flip
               # TODO make connection
               stringList.append("-1," + str(currentVertex) + "," + k)

               if noOfStreets == 0: break # stop if filled up
               noOfStreets -= 1 # count how many streets remaining to make

               visitedList.append(k)
            else:
               visitedList.append(k) # mark this visited anyway

        if isPrint(): print("stringlist")
        if isPrint(): print(stringList)
        if isPrint(): print("visitedlist")
        if isPrint(): print(visitedList)
        i += 1

    # now if still streets remain to be made, try to fit in some more streets
    if isPrint(): print("-------------------ADDING REMAINING STREETS--------")

    m = 0
    while True:
        if m == size: break # you have iterated through all houses
        # so whatever streets remain after this, there is no place
        # for them
        if filled == True: break # this loop not needed if streets are
        # already filled

        # if noOfStreets does get used up, then...
        if noOfStreets == 0:
            if isPrint(): print("Woohoo! All streets accomodated!")
            break

        visitedList = [] # this list should be new for each currentVertex

        currentVertex = houseList[m]
        visitedList.append(currentVertex)
        neighbours = []

        for index, j in enumerate(stringList): # you are checking the 
            # list currently being made, in order to 
            # see any newly created neighbours

            # if stringList empty, skip
            if j == "": continue
            line = j.split(",")
            if line[1] == currentVertex:
                neighbours.append(line[2])
            # now for the reverse order, find neighbours
            if line[2] == currentVertex:
                neighbours.append(line[1])

        # the neighbours list for the current vertex is filled here
        # you can't try to cram in more streets where a street
        # already exists

        for k in houseList:
            if k in visitedList: continue # skip the visited houses
            if k in neighbours: continue # skip house if connection 
            # already exists

            # at this point of code, we can infer that the
            # current vertex doesn't yet have a connection with k
            # so add street here
            stringList.append("-1," + str(currentVertex) + "," + k)
            noOfStreets -= 1 # count how many streets remaining to make
            visitedList.append(k)
        m += 1
    if isPrint(): print("No of unaccomodated streets = " + str(noOfStreets))

    # upto this point stringList has been filled with connections
    # but there can be houses remaining that weren't able to be connected,
    # so these disconnected nodes need to be encoded into stringList as well

    noOfHouses = size

    addedHouseList = getHouseList(stringList)
    remainingHouses = noOfHouses - len(addedHouseList)

    for i in houseList:
        if remainingHouses == 0: break
        currentVertex = i
        if currentVertex in addedHouseList: # if the house is already added,
            continue

        stringList.append("-1," + str(currentVertex) + "," + "Z")
        # if no connection, then 'Z', which means null
        remainingHouses -= 1

    # for some seeds, stringList can return Null or [],
    # that is because there are only two houses
    # avoid this error during usage
    if isPrint():
        print("FINAL STRINGLIST COMING OUT OF generateConnections()")
        for i in stringList:
            print(i)
    return stringList

# returns true or false
def confirmPavingPlan(townData, pavingString):
    # check1 make sure all houses from townData is specified
    # in pavingString
    houseList = getHouseList(townData)
    for i in houseList:
        skipName = False
        found = False
        for j in pavingString:
            if skipName==False:
                skipName = True
                continue
            line = j.split(",")
            if line[0] == i:
                found = True
                break
            if line[1] == i:
                found = True
                break
    if found == False: return False 

    # check2, traverse the pavingString and determine if
    # all the houses are connected via an algorithm

    n = len(houseList)
    skipName = False
    for k in pavingString:
        if skipName == False:
            skipName = True
            continue
        line = k.split(",")
        house1 = line[0]
        house2 = line[1]
        
        fromNode = 1
        toNode = 1
        for i in houseList:
            if house1 == i: break
            fromNode += 1
        for i in houseList:
            if house2 == i: break
            toNode += 1

        addEdge(fromNode, toNode)

    if (isConnected(n)):
        return True
    else:
        return False

def writeTownDataToFile(townData):
    outputlist = []
    outputlist.append("\"" + townData[0] + "\"")
    for i in townData:
        try:
            lines = i.split(",")

            pavingCost = lines[0] + ","
            fromHouse = "\"" + lines[1]+"\""+ ","
            toHouse = "\"" + lines[2]+"\""
            outputlist.append(pavingCost+fromHouse+toHouse)

        except IndexError:
            continue # to skip line with town name

    # now save to a file
    filename = townData[0] + ".txt"
    print("Writing to file " + filename)
    with open(filename, 'w') as file:
        for i in outputlist:
            file.write(i+"\n")


if __name__ == "__main__":
    houseList = ["A","B","C","D","E"]
    print("houseList[]:")
    print(houseList)

    seed = 42 # int(input("Seed?:"))
    
    stringList = generateConnections(houseList, seed)
    print("The output of function generateTown() is:")
    print(stringList)
