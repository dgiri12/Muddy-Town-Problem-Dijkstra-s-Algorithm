import pdb
import sys # to get argument from command line

# returns the input filename as a string
def processArgs(argv):
    inputfile = ""
    helpText = "HELP: townify.py -i <inputfile>"
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

#MAIN PROGRAM FUNCTION: ---------------------------------------------

def run_program():








# ----------------------------------------------------------------------
#the python program sequence
if __name__ == "__main__": # run code only if this program
    # instance is the main process
    run_program()

