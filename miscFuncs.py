import sys, getopt

MODULUS = 32768

# systemwide switch for printing debug messages
def isPrint():
    return False

#FUNCTION DEF: processArgs()
# returns the input filename as a string
def processArgs(argv):
    inputfile = ""
    argFormat = "Correct syntax: prog1.py -i <inputfile>"
    try:
        opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
        # only checks for incorrect format of arguments provided
        # to an option, if no option is provided, then technically
        # there is no error, so...
        print(argFormat)
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print(argFormat)
            sys.exit()
        elif opt == "-i":
            inputfile = arg
    if inputfile == "":
        print(argFormat)
        sys.exit(2)
    return inputfile

#FUNCTION DEF: processStringFromFile()
# returns a list where each list element is a line from the file
def processStringFromFile(_inputfile):
    print("Reading file " + _inputfile)
    with open(_inputfile) as f: # open file to read
        rawList = f.readlines() # read the file, each line is an
        # element in list rawList
    list1 = [] # the final list
    for i in rawList:
        list1.append(i.replace("\n", "")) # replace all \n char
        # in the list
    list2 = []
    for i in list1:
        list2.append(i.replace("\"", "")) # remove the '"' from
        # the strings
    return list2

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

def getRandomNumber(seed):
    multiplier = 11 
    increment = 17 
    seed = (multiplier * seed + increment) % MODULUS 
    while seed == 0: 
        seed = (multiplier * seed + increment) % MODULUS 
    return seed


# use this to test the random number function
# syntax: printRandomNumbers(3, 100)
def printRandomNumbers(_seed, _range):
    for i in range(_range):
        _seed = getRandomNumber(_seed)
        print("Random: ", str(_seed))

def isEven(_number):
    if _number % 2 == 0:
        return True
    else:
        return False

def sumOfDigits(_number):
    sum = 0
    for digit in str(_number):
        sum += int(digit)
    return sum

