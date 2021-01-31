# for loops, range, and code blocks

# # Loops
# # for item in list_of_items: do something
# fruits = ['apple', 'peach', 'pear']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + ' Pie')


# # coding challenge 1 (average student height) *can't use len or sum functions after the initial type change
# # get a list of all of the heights of the students
# # take the list as an input and use .split to separate by space to make the list
# student_heights = input('Input the list of student heights by cm\n').split(' ')
# # print(student_heights)
# # this for loop is used to convert to int and was provided by Angela
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# # create an empty variable for the total height int and #of students
# total_height = 0
# number_students = 0
# # create a for loop
# for height in student_heights:
#     # create a variable set to 0 that will grow with each height
#     total_height += height
#     print(total_height)
#     # create a variable that will keep track of the number of participants
#     number_students += 1
#     print(number_students)

# # find the avg height and round to the nearest whole number
# avg_height = round(total_height / number_students)
# print(avg_height)


# # coding challenge 2 (heighest test score)
# # get a list of all of the scores
# student_scores = input('Enter a list of the student scores.\n').split(' ')
# # a loop provided by angela to make everything an int
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # create a variable to compare the scores against
# highest_score = 0
# # create a for loop that will go through comparing the student_scores to highest_score
# for score in student_scores:
#     # create an if statement that will compare them and change the value if higher
#     if score > highest_score:
#         highest_score = score

# print(f'The highest score in the class is: {highest_score}points')


# # Range function
# # generates a range of numbers to loop through (you dont loop through a list)
# # for number in range(a, b): print(number) ## ** does not include the 'b'
# for number in range(1, 10):  # will not include '10' if you want 10 you need b to be '11'
#     print(number)
# # 'c' is the step by what it counts 1, 3, 5 etc...
# for number in range(1, 11, 2):
#     print(number)
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)


# # coding challenge 3 (adding evens) calculate the sum of all even numbers from 1-100 including 100
# # create an empty variable for the sum of the numbers
# sum_numbers = 0
# # create a range that will go through the numbers
# for n in range(1, 101):
#     # now use an if statement that will use % to check if its even or odd
#     if n % 2 == 0:
#         sum_numbers += n

# print(sum_numbers)


# coding challenge 4 (fizz buzz)
# have to print each num from 1 to 100 with any num divisible by '3' as 'fizz' by '5' as 'buzz' and both 'fizzbuzz'

# # start with a range and print 1 to 100
# for n in range(1, 101):
#     # print(n)
#     # create an if statement to catch those numbers divisible by 3, 5, or both
#     if n % 3 == 0 and n % 5 == 0:
#         print('FizzBuzz')
#     elif n % 3 == 0:
#         print('Fizz')
#     elif n % 5 == 0:
#         print('Buzz')
#     else:
#         print(n)


# Day 5 Project (Password Generator)

# import random so that you can do random generator
import random
# create a list of all the letters numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print welcome message
print('Welcome to the PyPassword Generator!')
user_letters = int(
    input('How many letters would you like in your password?\n'))
user_numbers = int(
    input(f'How many numbers would you like in your password?\n'))
user_symbols = int(
    input(f'How many symbols would you like in your password?\n'))
# print and test
# print(user_letters, user_numbers, user_symbols)

# set initial user password
user_password = ''

# EASY LEVEL

################ ANGELAS METHOD #########################

# for char in range(1, user_letters + 1):
#     user_password += random.choice(letters) # random.choice randomly picks soemthing from a list

# for char in range(1, user_numbers + 1):
#     user_password += random.choice(numbers)

# for char in range(1, user_symbols + 1):
#     user_password += random.choice(symbols)


################# MY METHOD ###############################

# create a range that will go the amount of the letters provided by user
for l in range(1, (user_letters + 1)):
    # a randomly generated number that will represent the index of one of the letters
    random_int = random.randint(1, (len(letters) - 1))
    # print(random_int)
    user_password += letters[random_int]

# do the same thing done for letters to numbers and symbols
for n in range(1, (user_numbers + 1)):
    random_int = random.randint(1, (len(numbers) - 1))
    user_password += numbers[random_int]

for s in range(1, (user_symbols + 1)):
    random_int = random.randint(1, (len(symbols) - 1))
    user_password += symbols[random_int]

print(user_password)

# HARD LEVEL

######################## ANGELAS METHOD ########################

# user_password_list = []

# # can use += or .append
# for char in range(1, user_letters + 1):
#     # random.choice randomly picks soemthing from a list
#     user_password_list.append(random.choice(letters))

# for char in range(1, user_numbers + 1):
#     user_password_list += random.choice(numbers)

# for char in range(1, user_symbols + 1):
#     user_password_list += random.choice(symbols)


# random.shuffle(user_password_list)

# password = ''
# for char in user_password_list:
#     password += char
# print(f'Your password is: {password}')

########################## MY METHOD ###########################


# use the sample method to create a new list after shuffling everything in the string
# random.sample('something', #) 'something' being what you want shuffled and # being the number of idexes from the original list or string you want returned in the new list
new_password_list = random.sample(user_password, len(user_password))

# create a new variable that will be used for the new password
better_user_password = ''
# create a for loop that will take all of the indexs from the shuffled list and add to new password
for i in new_password_list:
    better_user_password += i

print(better_user_password)
