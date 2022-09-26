import sys, getopt

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

def getRandomNumber(seed):
    modulus = 25 # needs to be positive
    # TODO while you develop djikstra's algorithm, keep mod = 25
    # ... later change it to 10000 to generator super large towns
    multiplier = 11 # is positive but less than modulus
    increment = 17 # is zero or more but less than modulus
    # seed = 3 # is zero or more, but less than modulus
    # for i in range(100): # i = 0 and i < 100
    return (multiplier * seed + increment) % modulus
    # this is known as an LCG (Linear Congruential Generator)
    # also, this generator has a period, i.e. the pseudo-
    # -domized numbers repeat after a certain number of
    # iterations. The modulus acts as a 'period length',
    # it's value can be changed to make the period longer
    # or shorter, lower is longer period
    # a value of modulus = 25 makes the period repeat every
    # 25 iterations

