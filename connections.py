from funcs import getRandomNumber
from coinFlip import isEven
from coinFlip import sumOfDigits
# this program is for generating a stringList that will
# convey randomized connection between a list of houses

printOutput = False
# returns a stringList
def generateConnections(houseList, _seed):
    if printOutput==True: print("generateConnections()->start")

    stringList = [] # the final vessel of the connections
    # usually the leftmost value is pavingCost, but put that as '-1'
    # since that is not the scope of this file

    # loop should start after stringList declaration
    i = 0
    size = len(houseList)
    if printOutput==True: print ("len(houseList):" + str(size))
    while True:
        # check if time to terminate loop
        if (i == size): break

        if printOutput==True: print("---iteration----i = " + str(i))
        visitedList = [] # this list should be new for each currentVertex

        currentVertex = houseList[i]
        if printOutput==True: print("currentVertex: " + currentVertex)
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

        if printOutput==True: print("Neighbours:")
        if printOutput==True: print(neighbours)


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
        if printOutput==True: print("stringlist")
        if printOutput==True: print(stringList)
        if printOutput==True: print("visitedlist")
        if printOutput==True: print(visitedList)
        i += 1
    # for some seeds, stringList can return Null or [],
    # that is because there are only two houses
    # avoid this error during usage
    return stringList

if __name__ == "__main__":
    houseList = ["A","B","C","D","E"]
    print("houseList[]:")
    print(houseList)

    seed = 42 # int(input("Seed?:"))
    
    stringList = generateConnections(houseList, seed)
    print("The output of function generateTown() is:")
    print(stringList)


