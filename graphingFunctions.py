from miscFuncs import getRandomNumber, isPrint, isEven, sumOfDigits
# this program is for generating a stringList that will
# convey randomized connection between a list of houses

# returns a stringList
def generateConnections(houseList, _seed):
    if isPrint(): print("generateConnections()->start")

    stringList = [] # the final vessel of the connections
    # usually the leftmost value is pavingCost, but put that as '-1'
    # since that is not the scope of this file

    # loop should start after stringList declaration
    i = 0
    size = len(houseList)
    if isPrint(): print ("len(houseList):" + str(size))
    while True:
        # check if time to terminate loop
        if (i == size): break

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
            _seed = getRandomNumber(_seed,25)
            if isEven(sumOfDigits(_seed)): # this is a coin flip
               # TODO make connection
               stringList.append("-1," + str(currentVertex) + "," + k)
               visitedList.append(k)
            else:
               visitedList.append(k) # mark this visited anyway
        if isPrint(): print("stringlist")
        if isPrint(): print(stringList)
        if isPrint(): print("visitedlist")
        if isPrint(): print(visitedList)
        i += 1
    # for some seeds, stringList can return Null or [],
    # that is because there are only two houses
    # avoid this error during usage
    return stringList

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

if __name__ == "__main__":
    houseList = ["A","B","C","D","E"]
    print("houseList[]:")
    print(houseList)

    seed = 42 # int(input("Seed?:"))
    
    stringList = generateConnections(houseList, seed)
    print("The output of function generateTown() is:")
    print(stringList)


