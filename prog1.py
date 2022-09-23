import sys, getopt

#FUNCTION DEF: processArgs()
# returns the input filename as a string
def processArgs(argv):
    argFormat = "prog1.py -i <inputfile>"
    try:
        opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
        print(argFormat)
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("HELP: " + argFormat)
            sys.exit()
        elif opt == "-i":
            inputfile = arg
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

#MAIN PROGRAM SEQUENCE:
if __name__ == "__main__": # run code only if this program
    # instance is the main process
    contents = processStringFromFile(processArgs(sys.argv[1:]))
    for i in contents:
        print(i)



# accepting arguments into a python program
