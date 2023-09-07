''' 
Write a program (function!) that takes a list and returns a new list that 
contains all the elements of the first list minus all the duplicates.

Extras:
Write two different functions to do this - one using a loop and constructing 
a list, and another using sets.
'''

import random

def generate_random_list(length=10):
    myRandIntList = []

    while len(myRandIntList) < length:
        randInt = random.randint(1, 10) # Generate a new random integer in each iteration.
        myRandIntList.append(randInt) # Generate the list with random int.
    return myRandIntList

def find_unique_with_loop(random_list):
    uniqueIntList = []

    for randInt in random_list:
        if randInt not in uniqueIntList: # Condition to add only unique int to the 'uniqueIntList'.
            uniqueIntList.append(randInt)
    return sorted(uniqueIntList)

def find_unique_with_set(random_list):
    uniqueIntList = list(set(random_list)) # Create a list of unique integers using set().
    return sorted(uniqueIntList)

random_List = generate_random_list()
unique_list_with_loop = find_unique_with_loop(random_List)
unique_list_with_set = find_unique_with_set(random_List)

print(f"Random Int List: \n{random_List}")
print(f"Unique Int List (Loop): \n{sorted(unique_list_with_loop)}")
print(f"Unique Int List (set() method): \n{unique_list_with_set}")



