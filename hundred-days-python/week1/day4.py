# Randomisation and Python Lists

# first have to import Random module
# import practice_module
import random
# create a random integer using randint(1st#, 2nd#)
random_integer = random.randint(1, 10)
print(random_integer)

# # to import other files as modules
# print(practice_module.pi)

# importing a random float from 0 - 1 but not including 1
# in order to get higher than 1 multiply the random_float by an integer or a randint
# random_float * 5 will give you a random float from 0 - 4.9999999
random_float = random.random()
print(random_float)


# # coding challenge 1 (heads and tail random generator)
# toss = random.randint(0, 1)
# if toss == 1:
#     print('Heads')
# else:
#     print('Tails')


# # python Lists (data structure)
# # organizes and stores data
# fruits = ['cherry', 'apple', 'pear']
# print(fruits)
# # can pull out items from list based off index
# print(fruits[0])
# # can rename them with index as well
# fruits[0] = 'Cherry'
# print(fruits[0])
# # can also add items to the list
# fruits.append('plum')
# print(fruits)
# # using .extend will add multiple items to the list by adding another list
# fruits.extend(['pineapple', 'peach', 'mango'])
# print(fruits)
# # .remove(x) will remove the item provided
# fruits.remove('peach')
# print(fruits)
# # use .pop to remove a certain index
# fruits.pop(-1)  # will remove 'mango'
# print(fruits)


# # coding challenge 2 (Banker Roulette)
# # use .split('somthing') to split stuff into a list by 'something' like ,
# names_string = input('Give me a list of names separated by a comma\n')
# # now we will split the names into a list
# names = names_string.split(', ')
# # print(names)
# # create a variable that will account for the total length of the list for use in randint function
# list_length = len(names)
# # print(list_length)
# # make sure to subtract -1 from the length since it doesnt start counting at 0
# random_banker = random.randint(0, list_length-1)
# # final message with who is paying
# message = f'{names[random_banker]} is going to buy the meal today!'
# print(message)


# # nested lists
# fruits = ['Strawberries', 'Nectarines', 'Apples',
#           'Grapes', 'Peaches', 'Cherries', 'Pears']
# vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']
# # a list that then containes these two separate lists
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)  # will list both lists and all of their indexs
# print(dirty_dozen[0])  # will give you all of the items in [fruits]
# print(dirty_dozen[0][0])  # will print 'Strawberries'


# # coding challenge 3 (Treasure Map)
# # create a 3 x 3 table using a list that will have different x's we will then use user input to change one of those spots to an 'o'
# # first create the three rows
# row1 = ['x', 'x', 'x']
# row2 = ['x', 'x', 'x']
# row3 = ['x', 'x', 'x']
# # then create the map which is the overall table holding the nested rows
# table = [row1, row2, row3]
# # print them on seperate rows so it looks like a map
# print(f'{row1}\n{row2}\n{row3}')
# # get user input based on concatenated string of collums and row
# position = input('Where do you want to place your treasure?\n')
# # you can use [#] to find the index of a string
# # assign them to a horizontal and vertical position
# horizontal = int(position[0])
# vertical = int(position[1])
# # print(type(horizontal))
# # using that assign the indexs of the 'postion' as the points so that you can change nested list
# # table[0][0] = 'o' # will change the very first 'x' to a 'o'
# # dont forget to subtract 1 from the index
# table[vertical-1][horizontal-1] = 'o'
# print(f'{row1}\n{row2}\n{row3}')


# Day 4 project (rock, paper, scissors)
# use randint for computer choice
computer_choice = random.randint(0, 2)
# ask user for their choice
user_choice = int(input(
    'What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n'))
if computer_choice == 2 and user_choice == 1:
    print('Computer chose scissors, YOU LOSE!')
elif computer_choice == 1 and user_choice == 1:
    print('Computer also chose paper, YOU TIE')
elif computer_choice == 0 and user_choice == 1:
    print('Comptuter chose rock, YOU WIN')
elif computer_choice == 2 and user_choice == 2:
    print('Computer also chose scissors, YOU TIE')
elif computer_choice == 0 and user_choice == 2:
    print('Computer chose rock, YOU LOSE')
elif computer_choice == 1 and user_choice == 2:
    print('Computer chose paper, YOU WIN')
elif computer_choice == 2 and user_choice == 0:
    print('Computer chose scissors, YOU WIN')
elif computer_choice == 1 and user_choice == 0:
    print('Computer chose paper, YOU LOSE')
else:
    print('Computer also chose rock, YOU TIE')
