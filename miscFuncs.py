import sys, getopt
import pdb

MODULUS = 32768

# systemwide switch for printing debug messages
def isPrint():
    return False


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

   
   
