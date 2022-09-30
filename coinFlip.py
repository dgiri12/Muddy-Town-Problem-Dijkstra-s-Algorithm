from funcs import getRandomNumber

# utility functions
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

# if running this program independently, this is what it will do
# but this program's functions can also be imported to be used in
# other files
if __name__ == "__main__":
    _seed = int(input("Seed?:"))

    for i in range(100):
        _seed = getRandomNumber(_seed,25)
        print ("Random: " + str(_seed) + 
            " sumOfDigits: " + str(sumOfDigits(_seed)) + 
            " isEven?: " + str(isEven(sumOfDigits(_seed))))



