import sys # to get argument from command line
from funcs import processArgs
from funcs import processStringFromFile
from funcs import getRandomNumber

# use this to test the random number function
def printRandomNumbers(_seed, _range):
    for i in range(_range):
        _seed = getRandomNumber(_seed)
        print("Random: ", str(_seed))

#MAIN PROGRAM FUNCTION:
def run():
    contents = processStringFromFile(processArgs(sys.argv[1:]))
    for i in contents:
        print(i)

    printRandomNumbers(3, 100)

# --------------------------------------------------------
#the python program sequence
if __name__ == "__main__": # run code only if this program
    # instance is the main process
    run()

