import numpy as np
import math
print("hello World")


#  Exercise 8.1 – Iteration
#  Python provides for and while loop that enable us to repeat blocks of instructions several times. For example to write “Python is cool” 5 times:
# print("This program prints a string 5 times")
# for count in range(5):
#      print("Python is cool")


#  a. Write a program that will print your full name and student number 10 times.
#  b. Write another program that will ask the user for a “wish” (eg. What do you wish for on
#  your birthday) and the number of time they want that wish to be displayed. Then print the wish the number of times specified.


# a
# for count in range(10):
#      print("Adam 304130")

""" wish = input("What do you wish for on  your birthday?: ")
repeat = input("How many times do you want your wish to be displayed?: ")


for count in range(int(repeat)):
     print(wish)
     print(count) """

# Exercise 8.2 – Sum
# Exercise 8.2 – Sum
# Given numLst = [1, 2, 3, 4, 5] we can compute the sumImperative in an imperative way.
# You have to implement it such that it uses imperative way to compute the sum of the list.

""" def sumImperative(list):
    sum = 0
    for number in list:
        sum = sum+number
    return sum

numLst = [1, 2, 3, 4, 5]
print(sumImperative(numLst)) """


# Exercise 8.3 – Even numbers
# Using the imperative way of programming, check for even numbers given a user input:
# Write a program, which repeatedly prompts the user for an integer. If the integer is even, print the integer.
# If the integer is odd, don’t print anything. Print “Bye for now!” and Exit the program if the user enters the integer 123.

def evenNumbers():
    while (1):
        num = input("Give an input(number): ")

        if (int(num) % 2 == 0):
            print(num)
        elif (int(num) == 123):
            quit()
        else:
            print("Bye for now!")

# evenNumbers()


# Exercise 8.4 – Lists
# Exercise 8.4 – Lists
# Using the imperative coding style, implement a function groupList that given a list (list) and a group length (glength),
# returns a list of lists with length glength.

# Example: list = [1, 2,3,4,5,6]
# groupList(list, 2) gives [ [1, 2], [3, 4], [5,6] ] while groupList(list, 3) gives [ [1, 2, 3], [4, 5, 6] ]


def groupList(list, gLength):

    numOfLists = int(math.ceil(len(list) / gLength))
    resList = np.empty((numOfLists, gLength))

    counter = 0
    for i in range(numOfLists):
        for j in range(gLength):
            if len(list) > 0:
                print(i, j)
                resList[i][j] = list[counter]
                counter = counter+1

    return resList


# list = [1, 2,3,4,5,6]
# res1 = groupList(list, 2) # gives [ [1, 2], [3, 4], [5,6] ]
# print(res1)

# res2 = groupList(list, 3) # gives [ [1, 2, 3], [4, 5, 6] ]
# print(res2)

# Exercise 8.5 – Dictionaries
# Create a dictionary specialle which stores software engineering specializations:

# a. populate it with these key-value pairs:
# Name              Specialle
# Bob Builder        IoT
# Dora Explorer      Interactive Media
# Paw Patrol         Data Engineering

#
# b. Change Bob Builder's specialle to Data Engineering
# c. Add a new entry for "Farmer Pickles" with specialization "Climate Engineering"
# d. Print Dora's specialization
# e. Print all the keys. Don’t worry about the format.

specialle = {
    "Bob Builder": "IoT",
    "Dora Explorer": "Interactive Media",
    "Paw Patrol": "Data Engineering",
}

specialle["Bob Builder"] = "Data Engineering"
specialle["Farmer Pickles"] = "Climate Engineering"
print(specialle["Dora Explorer"])

print(specialle.keys())


# Exercise 8.6 – Extra
# Using the imperative coding style implement a program that allows users to enter a number that represents a shape
# and then calculates the area accordingly. Recall exercises 4 from F#. For instance:

# Pick a shape(1-3):
# 1) Square
# 2) Rectangle
# 3) Triangle


def shapePicker():
    message = """ Pick a shape(1-3):
    1) Square
    2) Rectangle 
    3) Right Triangle 
    Your pick:
    """
    return int(input(message))
    
    
def sizeChooser(shape):
    if(shape == 1):
        strShape = "Square"
        sideA = float(input("Choose the side for a square: "))
        return sideA * sideA
    
    elif(shape == 2):
        strShape = "Rectangle"
        sideA = float(input("Choose side A for a Rectangle: "))
        sideB = float(input("Choose side B for a Rectangle: "))
        return sideA * sideB
    elif(shape == 3):
        strShape = "Right Triangle"
        sideA = float(input("Choose base for a Right Triangle: "))
        sideB = float(input("Choose side B for a Right Triangle: "))
        return sideA * sideB * 0.5
    else:
        print("Wrong input")
        return 0
    
    
print(sizeChooser(shapePicker()))


