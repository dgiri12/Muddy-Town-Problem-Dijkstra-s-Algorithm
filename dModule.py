class DField:
    def __init__(self, house, shortest, prevHouse):
        self.house = house
        self.shortest = shortest
        self.prevHouse = prevHouse

    def printValues(self):
        print(self.house + "\t" + str(self.shortest) + "\t" +
                self.prevHouse)

def djikstraModule():

    stringList = [
            "6,A,B",
            "1,A,D",
            "2,D,B",
            "1,D,E",
            "2,E,B",
            "5,E,C",
            "5,C,B"]
    # to find connection for eg for A with other houses
    # iterate the whole list and find for A,B or A,D
    # that way you know what houses A is connected to

    # before applying the djisktra algorithm,
    # first step is to make sure the file is in a proper format
    # no repitiions, like 6,A,B and 6,B,A
    # no unconnected houses, no houses by themselves
    # no street that is seperate from the rest, something 
    # always needs to connect directly or indirectly to that street

    # then, you can normally use the djikstra's algorithm with no
    # worries of these anomalies

    notVisitedList = []
    for i in stringList:
        x = i.split(",")
        if x[1] not in notVisitedList:
            notVisitedList.append(x[1])
        if x[2] not in notVisitedList:
            notVisitedList.append(x[2])
    print("notVisitedList[]:")
    print(notVisitedList)

    # create a dTable from the nonvisitedlist
    dTable = []
    for i in notVisitedList:
        temp = DField(i,-1,"Z") 
        # '-1' means infinity and 'Z' means null-string
        dTable.append(temp)
    # print the entire dTable
    print("The D-Table:")
    for x in dTable:
        x.printValues()

    # next step
    visitedList = [] # to store houses that have been visited
    visitedConnectionsList = []

    # let distance of start vertex from start vertex = 0
    # whichever is the 1st house in dTable, is the start vertex
    dTable[0].shortest = 0
    # let distance of all other vertices from start = inf
    # which is done above
    while true:
        print("New Iteration:")
        print("The updated D-Table:")
        for x in dTable:
            x.printValues()

        min = -1
        foundIndex = -1
        for idx, i in enumerate(dTable):
            if min == -1:
                min = i.shortest
                foundIndex = idx
                continue
            if i.shortest == -1: # inf cannot be min, so goto next
                continue
            if i.shortest < min:
                min = i.shortest
                foundIndex = idx
        print("lowest is: " + dTable[foundIndex].house)
        if dTable[foundIndex].house in visitedList:
            continue # goto next if this house already visited

        # for this unvisited vertex, examine its neighbours
        currentHouse = dTable[foundIndex].house
        currentConnection = ""
        for x in stringList:
           i = x.split(",")
           if i[1] == currentHouse:
               neighbour = i[2]
               currentConnection = i[1]+i[2]
               # now check if this connection is already visited
               if currentConnection not in visitedConnectionsList:

