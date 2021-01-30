# conditional statements, logical operators, code blocks and scope

# # conditionals
# height = int(input('What is your height in cm?\n'))

# if height >= 120:
#     print('You can ride the rollercoaster!')
# else:
#     print('You are not tall enought to ride')


# # coding challenge (odd or even number)
# # ask for a number
# num = int(input('Pick a number:\n'))
# # use % and if statement to find if num == 0 then its even otherwise odd
# if num % 2 == 0:
#     print('Your number is even!')
# else:
#     print('Your number is odd!')


# # nested if / else statements
# height = int(input('What is your height?\n'))
# age = int(input('What is your age?\n'))

# if height >= 120:
#     if age < 12:
#         print('You can ride this ride for 5$')
#     elif age > 12 and age < 18:
#         print('You can ride this ride for 7$')
#     else:
#         print('You can ride this ride for $12')
# else:
#     print("You're not tall enough to ride this ride :(")


# # coding challenge 2 (BMI calculator with coresponding levels)
# # bmi = weight / height ** 2
# # ask for height in meters
# height = float(input('What is your height in meters?\n'))
# # ask for wight in kg
# weight = float(input('What is your wight in kg?\n'))
# # print(height, weight)
# # calculate the persons bmi
# bmi = round(weight / (height ** 2), 2)
# # print(bmi)
# # use conditional statement to find health comparison
# if bmi <= 18.5:
#     print(f'Your bmi is {bmi}% and you are considered underweight')
# elif bmi > 18.5 and bmi <= 25:
#     print(f'Your bmi is {bmi}% and you are considered normal weight')
# elif bmi > 25 and bmi <= 30:
#     print(f'Your bmi is {bmi}% and you are considered overweight :(')
# elif bmi > 30 and bmi <= 35:
#     print(f'Your bmi is {bmi}% and you are considered obese :*')
# else:
#     print(
#         f'Your bmi is {bmi}% and you are considered clinically obese :*******')


# # coding challenge 3 (Leap year exercise) difficult challenge
# # a leap year is a year that is evenly dvisible by 4 except if its also evenly divisible by 100 unless also dvisible by 400
# # first ask for the year
# year = int(input('What is the year?\n'))
# # create an if statement that is nested and checks the different variables
# if year % 4 == 0:
#     if year % 100 == 0 and year % 400 == 0:
#         print('This is a Leap Year')
#     elif year % 100 != 0:
#         print('This is a leap year')
#     else:
#         print('This is not a Leap Year')
# else:
#     print('Not a Leap Year')


# # multiple if statments
# # using multiple (if) vs and elif means that they will still be checked even if previously (if) is triggered
# # the multiple (if) statements have to be on same level to be checked
# height = int(input('What is your height?\n'))
# bill = 0

# if height >= 120:
#     print('You can ride the rollercoaster :)')
#     age = int(input('What is your age?\n'))
#     if age < 12:
#         print('Child tickets are 5$')
#         bill = 5
#     elif age > 12 and age < 18:
#         print('Youth tickets are 7$')
#         bill = 7
#     else:
#         print('Adult tickets are $12')
#         bill = 12

#     wants_photo = input('Do you want a photo taken? Y or N\n')
#     if wants_photo == 'Y':
#         # add $3 to bill
#         bill += 3
#         print(f'Your bill is ${bill}')
#     else:
#         print(f'Your bill is ${bill}')
# else:
#     print("You're not tall enough to ride this ride :(")


# # coding challenge 4 (Pizza Order)
# # find size (s, m, l) find pepperoni (y, n) find cheese (y, n) give total price
# # welcome message
# print('Welcome to Doms Pizza Palace')
# # set their initial price
# price = 0
# # ask which pizza they want
# choice = input(
#     'What size pizza do you want? Small, Medium, Large or Cancel?\n')
# # use conditionals to separate choice and tell them price
# # then ask if they want pepperoni
# if choice == 'Small' or choice == 'Medium' or choice == 'Large':
#     if choice == 'Small':
#         print('A small pizza is $15')
#         price += 15
#         # find out if they want pepperoni for small pizza ($2)
#         pepperoni = input('Would you like to add Pepperoni for $2? Y or N\n')
#         if pepperoni == 'Y':
#             price += 2
#     elif choice == 'Medium':
#         print('A medium pizza is $20')
#         price += 20
#         # find out if they want pepperoni for medium or large pizza ($3)
#         pepperoni = input('Would you like to add Pepperoni for $3? Y or N\n')
#         if pepperoni == 'Y':
#             price += 3
#     else:
#         print('A large pizza is $25')
#         price += 25
#         # find out if they want pepperoni for medium or large pizza ($3)
#         pepperoni = input('Would you like to add Pepperoni for $3? Y or N\n')
#         if pepperoni == 'Y':
#             price += 3

#     # ask if they want cheese $1
#     cheese = input(
#         'Would you like to add extra cheese to your pizza for $1? Y or N\n')
#     if cheese == 'Y':
#         price += 1

#     print(f'Your pizza will cost ${price}, thank you and come again!')
# else:
#     print('We hope that you come back some other time then.')


# logical operators in python (and, or, not)


# # coding challenge 5 (love calculator)

# # something.lower() will change every character in 'something' to lower case
# # name = 'Dominic'.lower() # will give you 'dominic'
# # something.count('character') will count the number of times that 'character' appears in 'something' (case sensitive)
# # name = 'Dominic'.count('i') # will give you 2

# # get two names and find out how many times that 't' 'r' 'u' 'e', 'l' 'o' 'v' 'e' occurs to give them a score
# # get the two names
# name1 = input('What is the first name?\n')
# name2 = input('What is the second name?\n')
# # make sure the names are lower case only
# lower_case_name1 = name1.lower()
# lower_case_name2 = name2.lower()
# # combine the names so that its easier to count
# combined = lower_case_name1 + lower_case_name2
# # print(combined)
# # start counting and add to score
# true_score = combined.count('t') + combined.count('r') + \
#     combined.count('u') + combined.count('e')
# love_score = combined.count('l') + combined.count('o') + \
#     combined.count('v') + combined.count('e')
# # concatinate two scores as strings for final score
# final_score = int(str(true_score) + str(love_score))
# # print(final_score)

# # create a conditional to customize message based on score
# if final_score <= 10 or final_score >= 90:
#     print(
#         f'Your score is {final_score} points, you go together like coke and mentos!')
# elif final_score >= 40 and final_score <= 50:
#     print(f'Your score is {final_score} points, you are alright together.')
# else:
#     print(f'Your score is {final_score} points.')


# day 3 project (Treasure Island)
# create a choice based game that will end in death or victory
# Begin the game with a welcome message
print('Welcome to the quickest and deadliest treasure hunt!')
print('You come across a giant lake and have a feeling that their is treasure on some random looking island.')
choice = input(
    'Do you wait for the boat or swim across the choppy water? Type wait or swim\n').lower()
# print(boat)
if choice == 'wait':
    print("You didn't have to wait long and you made it across safely.")
    choice = input(
        'You come across a wobbly bridge, do you go right and cross bridge or left and find another route? Enter left or right\n').lower()
    if choice == 'left':
        print('You quickly find an alternative and safer route across')
        choice = input(
            'You finally find three doors which do you open? Red, Yellow, or Green? Enter red, yellow, or green\n').lower()
        if choice == 'red':
            print(
                'You open the door as soon as a warlock fires a fireball. You burn to a crisp. YOU DIED!')
        elif choice == 'yellow':
            print(
                'Weirdly this was actually the right door. You find a room filled with gold. LUCKY YOU!')
        elif choice == 'green':
            print(
                'You open the door as soon as a goblin charges through with a dagger. YOU DIED!')
        else:
            print('You chose poorly and you messed up. YOU DIED!')
    else:
        print('The bridge was unsteady and you fell into a cavern. YOU DIED!')
else:
    print('You realized too late that the water was choppy because of all the sharks. YOU DIED!')
