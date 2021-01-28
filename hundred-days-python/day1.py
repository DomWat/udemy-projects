# # using one line to print code on multiple lines
# print("Hello World!\nHello World!")

# # use the input function with prompt to ask questions
# input("What is your name?")
# print("Hello " + input('What is your name?'))


# # use len() to count the number of characters in a string
# name = input('What is your name?')
# print(len(name))


# # get a value for a and b and the print out the values haing switched them
# a = input("a:")
# b = input('b:')

# c = a
# a = b
# b = c
# print(a, b)


# day 1 project: Band Name Generator

# greeting for user as they enter program
greeting = 'Welcome to the world famous Band Name Generator, I hope you will love your new band name'
print(greeting)

# ask user for city they grew up in
city = input('What city did you grow up in?\n')

# ask user for the name of a pet
pet_name = input('What is your favourite pets name?\n')

# combine the two inputs and show them their band name with a message
band_name = city + ' ' + pet_name
final_output = 'Thank you for your patronage your band name is: ' + band_name
print(final_output)
