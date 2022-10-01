# README

This is a python script that aids in planning how to get the least cost of paving streets that connect all the houses  in a town.

## REQUIREMENTS:
This program requires python3 to be run on the system. Please install HomeBrew and refer to internet documentation for how to install python3 into your system.

## HOW TO RUN PROGRAM:

```
Please go to a Unix-based shell (bash or zsh) and type
> python3 townify.py
This will bring up the main menu of the program.

The following are the menus and a short description of what they do:

1. Load town and display town
	This menu loads and displays a town file that might be stored on disk. You will be asked to enter the name of the file to be loaded

2. Generate Random Town
	This menu generates a random town, and also saves it to a file so that it can be used to run or test the other menus

3. Generate a minimum cost paving plan for a town
	This menu generates a paving plan that will cost the lowest for a certain town. You will be asked to enter a town file name, and in return it displays (and stored to disk) the associated paving plan for that town.

4. Load and Display Paving Data and Paving Cost
	This menu can be used to load paving plan from disks, and refer to the paving cost stored on disk. You will be asked to enter a filename for the town data and for its associated paving plan file.

5. Load a paving plan and test if its valid
	This menu asks you for the filename of a town and its paving plan. In return, it determines if the paving plan correctly reflects the fact that each house in the town is connected by a paved street, and no house is left out.

6. Load a paving plan and test if it gives minimum cost
	This menu asks you to enter filename for a town file and its paving plan. It then generates its own paving plan, in order to see if the provided paving plan has the least cost, or if the plan that it generated actually has the lower cost

7. LCG vs stdlib histogram demonstration
	This menu demonstrates the usage of a Linear Congruential Generator vs an "off the shelf" random number generator, to see which has a better run time. This program has made use of python's own "random" library to compare the LCG with.

0. Exit
	Exits the program
```

## TESTS:
```
	For the time being, tests are done manually.
Testing for menu 5 can be done by using the files 'Town1.dat', 'Town1PavingPlan.dat' and 'Town1UnCon.dat'.
The 'Town1PavingPlan.dat' paving plan has all houses connected by paved roads. The program should say 'True'.
The 'Town1UnCon.dat' paving plan has a disconnected plan. The program should say 'False'.
```