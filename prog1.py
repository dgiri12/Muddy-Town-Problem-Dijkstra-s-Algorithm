# the built in __init()__ function of every class
class Person:
    def __init__(self, name, age): #the self parameter always goes in there
        # but during usage, there is only two parameters
        # to change the value of the class's own attributes,
        # use the self.variableName syntax
        # PS the 'self' can be called anything, as long as it is
        # the first parameter, python will recognise it as 'self'
        self.name = name
        self.age = age

p2 = Person("John", 36) # this is like a C++ constructor

print(p2.name)
print(p2.age)

# methods inside class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name + " and I am " +
                str(self.age) + " years old")

p3 = Person("John", 36)
p3.myfunc()

# methods created inside class is called instance method.
# there are also class methods ...
# methods can be declared outside class all by themselves too
def myAddFunction(a, b): # standalone functions don't require the 'self' parameter
    return a + b

print("Adding 5 and 6 gives you ... " + str(myAddFunction(5,6)))
# using an integer value in between string concatenations will require using str() function
# feed integer value to str() function, and it will return a string

# File IO 
# read()
print("read() function:")
with open('MiniTown.dat') as f:
    contents = f.read() # stores entire text file as one string
    # into variable 'contents'
    # the with ... as statement automatically closes the file
    # there is a close() function if needed in case
print(contents)

# readline()
print("readline() function:")
with open('MiniTown.dat') as f:
    print(f.readline()) # read a line, moves the file cursor
    print(f.readline()) # read a line, moves the file cursor
    # the print() adds a blank line automatically, but it 
    # also prints the \n char from the file itself,
    # so there is a blank space in between ...
    # use the strip() function to remove \n chars from a string
    print(f.readline().strip())
    print(f.readline().strip())

# readlines()
print("readlines() function:")
with open('MiniTown.dat') as f:
    contents = f.readlines() # also, readlines() returns 
    # a python list
for i in contents:
    print(i)

# use strip() on each element of list 'contents' to remove '\n'
rez = []
for i in contents:
    rez.append(i.replace("\n", ""))
# print the final output without the \n char
for i in rez:
    print("rez: " + i)

# accepting arguments into a python program
# TODO ...
