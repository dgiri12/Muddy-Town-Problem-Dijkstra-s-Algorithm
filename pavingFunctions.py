from miscFuncs import processStringFromFile

# reads paving data from file, and stores it in
# the system as a string
def readPavingDataFromFile(inputfile):
    pavingString = processStringFromFile(inputfile)
    return pavingString

def generatePavingStringFromDTable(planName, dTable):
    pavingString = []
    pavingString.append(planName)
    for i in dTable:
        if i.prevHouse != "Z" and i.house != "Z":
            pavingString.append(i.house+","+i.prevHouse)
    return pavingString

# generate a file1
def writePavingStringToFile(pavingString):
    outputlist = []
    outputlist.append("\"" + pavingString[0] + "\"")
    for i in pavingString:
        try:
            lines = i.split(",")
            fromHouse = "\"" + lines[0]+"\""+ ","
            toHouse = "\"" + lines[1]+"\""
            outputlist.append(fromHouse+toHouse)
        except IndexError:
            continue # to skip line with town name

    # now save to a file
    filename = pavingString[0] + ".txt"
    print("Writing to file " + filename)
    with open(filename, 'w') as file:
        for i in outputlist:
            file.write(i+"\n")

# also returns the total pavingCost
def displayPavingData(townData, pavingString):
    pavingCost = 0

    pavingStringNameSkip = False
    for i in pavingString:
        if pavingStringNameSkip == False:
            pavingStringNameSkip = True
            continue
        line = i.split(",")
        pave_house1 = line[0]
        pave_house2 = line[1]

        townDataNameSkip = False
        for j in townData:
            if townDataNameSkip == False:
                townDataNameSkip = True
                continue
            line2 = j.split(",")
            town_house1 = line2[1]
            town_house2 = line2[2]

            # now find connection, also the data shouldn't have repeated
            # connections, so you can ignore that here
            if pave_house1 == town_house1 and pave_house2 == town_house2:
                pavingCost += int(line2[0])
            if pave_house1 == town_house2 and pave_house2 == town_house1:
                pavingCost += int(line2[0])

    print("The paving plan is:")
    for i in pavingString:
        print(i)
    print("Total cost with this paving plan: " + str(pavingCost))
    return pavingCost

# 5a function that determines if a given paving plan achieves the
# minimum cost of any plan that allows travel from building to
# any other building using only paved street

def isMinPavingPlanCost(townDataFile, pavingPlanFile):
    # first construct your own dTable with the provided files
    # then calculate the pavingCost, that is the minimum 
    # paving cost supposed to be for your town

    townData = processStringFromFile(townDataFile)

    dTable = townProcessor(townData)
    pavingPlanName = townData[0] + " paving plan"
    pavingString = generatePavingStringFromDTable(pavingPlanName, dTable)
    ownCost = displayPavingData(townData, pavingString)
    
    # now calculate paving cost of provided file
    providedPavingString = readPavingDataFromFile(pavingPlanFile)
    providedCost = displayPavingData(townData, providedPavingString)
    if providedCost > ownCost:
        return False
    else:
        return True

# 6a function that determines a minimum cost paving plan
def findMinCostPavingPlan(townDataFile):
    townData = processStringFromFile(townDataFile)
    dTable = townProcessor(townData)
    pavingPlanName = townData[0] + " paving plan"
    pavingString = generatePavingStringFromDTable(pavingPlanName, dTable)
    minCost = displayPavingData(townData, pavingString)
    return minCost

