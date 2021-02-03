# functions with inputs, difference between arguments & parameters

# # FUNCTIONS
# # add a variable to ino can be passed
# def greet():
#     print('Hello')
#     print('Hello')
#     print('Hello')



# # pass info when called to replace the variable
# greet()


# name = input('What is your name?\n')


# # ('parameter')
# def greet_with_name(name):
#     print(f'Hello {name}')
#     print(f'Hello {name}')
#     print(f'Hello {name}')

# # calling function('argument')
# greet_with_name(f'{name}')



# city = input('What is your city?\n')

# # making a function with 2 parameters
# def new_function(name, city):
#     print(f'Hello {name}')
#     print(f'How is the weather in {city}')

# new_function(f'{name}', f'{city}')



# # coding challenge 1 (Area calculation)

# # import math so that you can round the final answer
# import math

# # based on height width and coverage per can find how many cans needed to paint a wall
# def area_calc(height, width, coverage):
#     # number of cans = (wall height X wall width) / coverage per can
#     # make sure that all the variables are integers
#     num_cans = (int(height) * int(width)) / int(coverage)
#     # use math.ceil() to make sure every number is rounded up
#     print(f'You will need {math.ceil(num_cans)} cans in order to paint the wall')

# height = int(input('What is the height of the wall in meters:\n'))
# width = int(input('What is the width of the wall in metters:\n'))
# coverage = int(input('What is the coverage of each can of paint:\n'))


# area_calc(f'{height}', f'{width}', f'{coverage}')



# # coding challenge 2 (prime number checker)

# # prime num can only be divided by 1 and itself

# # create the function
# # include a parameter for the number
# def prime_checker(n):
#     is_prime = True
#     for number in range(2, n):
#         if n % number == 0:
#             is_prime = False
#     if is_prime == True:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number")
# num = int(input('Pick a number to check if its prime:\n'))

# prime_checker(num)



# Day 8 project CAESAR CIPHER

# create a list for the letters of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
# create the opening inputs

# # the directions
# directions = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# # get the message they want to encrypt make sure it's all lower case
# text = input('Type your message here:\n').lower()
# # find the number that they want to shift all the text by
# shift = int(input('Type the shift number:\n'))

# # use moduls to make sure that the number they pick is within the index of alphabet
# shift = shift % 26

# # create a variable to be used to determine if the user is done
# is_done = False

# # create the encrypt function that takes in 'text' and 'shift'
# def encrypt(plain_text, shift_amount):
#     # create an empty string that will hold all of the shifted letters
#     new_word = ''
#     # shift each letter of the 'text' forward in alphabet by 'shift' number
#     for letter in plain_text:
#         # you can use .index() to find the index number of a list
#         # set it equal to position so you will have the index of the same letter in alphabet list
#         position = alphabet.index(letter)
#         # find the new position that includes the shift number
#         new_position = position + shift_amount
#         #now create a new variable that will be the letter in that new position
#         new_letter = alphabet[new_position]
#         # add all the new letters to the empty string you created
#         new_word += new_letter
#     print(f'The encoded text is {new_word}')

# # do the same thing but backwards to decrypt
# def decrypt(shifted_text, shift_number):
#     original_word = ''

#     for letter in shifted_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_number
#         # can add it straight to the empty string without having to create a new_letter
#         original_word += alphabet[new_position]
    
#     print(f'The encoded message was {original_word}')


# # create an if statement that will check if they want to encrypt or decrypt
# if directions == 'encode':
#     encrypt(text, shift)
# elif directions == 'decode':
#     decrypt(text, shift)
# else:
#     print('That was not a proper direction')





# *********************** BETTER FUNCTION ***********************

def caesar(message, key, choice):
    encrypted_word = ''
    decrypted_word = ''
    
    if choice == 'encode':
        for char in message:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + key
                encrypted_word += alphabet[new_position]
            else:
                encrypted_word += char
        print(f'The encrypted message is {encrypted_word}')
    elif choice == 'decode':
        for char in message:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position - key
                decrypted_word += alphabet[new_position]
            else:
                decrypted_word += char
        print(f'The original message was {decrypted_word}')


# put everything into a while loop so it will keep running until they quit
is_done = False

while not is_done:
    # the directions
    directions = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # get the message they want to encrypt make sure it's all lower case
    text = input('Type your message here:\n').lower()
    # find the number that they want to shift all the text by
    shift = int(input('Type the shift number:\n'))

    # use moduls to make sure that the number they pick is within the index of alphabet
    shift = shift % 26

    caesar(text, shift, directions)

    # give the option to continue or end
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no' to quit.\n")

    if restart == 'no':
        is_done = True
        print('Goodbye')

# ************ FIND A WAY TO CANCEL OR RESTART IF THEY TYPE SOMETHING THATS NOT ENCODE OR DECODE **************