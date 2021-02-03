# Day 7 Project Hangman 

# import random
import random
# import ascii art from the module i created
import hangman_art_module as ham
# import the word list from the module i created
import hangman_words_module as hwm


# # create a word list for testing only
# word_list = ['mongoose', 'alphabet', 'wolf']

# randomly choose a word in the word list and assign it to a variable

chosen_word = random.choice(hwm.word_list)
# print(chosen_word)

# create an empty list that will be used to store the correct letters as they guess
display = []

# for each letter in 'chosen_word' have an _ in display
for letter in chosen_word:
    display.append('_')



# create a variable to keep track of users lives
lives = 6


# print the hangman entry logo
print(ham.logo)
    
# create a while loop so that it will continue playing until the player has won
# create a variable 'end_of_game' that is set to False and switched to True when everything in 'display' is finished
end_of_game = False
while not end_of_game:

    


    # ask user to guess a letter and assign it to guess. make sure its lowercase
    guess = input('Guess a letter:\n').lower()


    # check to see if they have already said a letter
    if guess in display:
        print(f'You have already guessed {guess}')

    # isolate the position in the chosen word 
    # check if 'guess' is one of the letters in 'chosen_word'
    # then replace that same position in display with the 'guess' if it's correct
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    # if their guess is not in the 'chosen_word' reduce their lives by 1
    if guess not in chosen_word:
        print(f'{guess} is not in the word. You lose a life')
        lives -= 1
        # print(lives)


    # display the 'display' at the end
    # will also get rid of the [ ] and ,
    print(f"{' '.join(display)}")

    # create a check to see if 'display' has any blanks if not then end game
    # add an elif statment to end game if they lose and have no lives left
    if '_' not in display:
        end_of_game = True
        print('YOU WIN')
    elif lives == 0:
        end_of_game = True
        print('YOU LOSE')

    # print the ascii art from module to show the lives
    print(ham.stages[lives])
