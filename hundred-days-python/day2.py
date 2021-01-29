# data types, numbers, operations, type conversion, f-strings

# # subscript: when you pull an element out of a whole
# word = 'Hello'
# print(word[0])  # will print out H
# print(word[-1])  # will print out the last character

# data types: string, integer, float, boolean
# # type(something) : will show the data type of the 'something'
# print(type(9))

# # using ...str(something) will convert 'somthing' into a string
# num_char = len(input('What is your name?'))
# print(num_char)
# print(type(num_char))
# new_num_char = str(num_char)
# print('Your name has ' + new_num_char + ' characters!')

# using ...int(something) will convert 'something' into an integer
# using ...float(something) will convert 'something' into an float


# # coding challenge
# # input a 2 digit number and then add the seperate parts
# # input 35 then the output should be '8' (3 + 5)
# num = input('Enter a number:\n')
# # print(type(num))
# digit1 = int(num[0])
# digit2 = int(num[1])
# # print(type(digit1))
# answer = digit1 + digit2
# print('The answer is: ' + str(answer))


# mathematical operators (+, -, *, **, /, %)


# # coding challenge
# # create a bmi calculator (bmi = weight(kg)/height**2(m))
# weight = input('Enter your weight in kg:\n')
# height = input('Enter your height in meters: \n')
# # print(type(height))
# bmi = int(weight) / (float(height)**2)
# bmi_as_int = int(bmi)
# print('Your BMI is ' + str(bmi_as_int) + '%')


# # use ...round(something, #) to round a number and the 2nd attribute if added is the precision
# print(8/3)  # will get 2.66666
# print(int(8/3))  # will get 2 (just chops off everthing after the decimal)
# print(round(8/3))  # will get 3 (actually rounds the number)
# print(round(8/3, 2))  # will get 2.67 (the 2 shows the level or precision)
# print(8//3)  # will get 2 (// is the floor division and always rounds down)


# # f'writing a string with different {values}'
# # f-string : allows you to mix data types without having to convert and using concatination
# score = 0  # int
# height = 1.8  # height
# isWinning = True  # boolean
# print(
#     f'your score is {score}, your height is {height}, and your winning is {isWinning}')  # string


# # coding challenge 3
# # use f-string and math operators to find how many weeks are left in someones life if they went to 90
# # ask for current age
# age = input('What is your current age?\n')
# weeks_so_far = int(age) * 52
# years_left = 90 - int(age)
# months_left = years_left * 12
# weeks_left = years_left * 52
# message = f'You are {age} years old which means you have lived for {weeks_so_far} weeks by the end of the year. If you were to live untill 90 you have {years_left} years left {months_left} months left and {weeks_left} weeks left. Good luck.'
# print(message)


# project day 2 (tip calculator)
# create a tip calculator that will ask for total bill, tip, # of people and then display answer
# greeting message
print('Welcome to the tip calculator!')
# ask for total bill
bill = float(input('What is the total bill?\n$'))
# get the tip
tip = int(input('What percentage of tip? 15, 20, 30?\n%'))
# get the number of people splitting the bill
num_people = int(input('How many people in the group?\n'))
# get the tip percentage (tip / 100) and round it to 2 decimal points
tip_percentage = round(tip / 100, 2)
# print(tip_percentage)
# find the bill with the cost of tip
tip_result = bill * tip_percentage
total_bill = bill + tip_result
# find the per person payment
per_person = round(total_bill / num_people, 2)
# print final message
message = f'With a bill of ${bill} and a tip of {tip}% and {num_people} people each person will pay ${per_person}'
print(message)
