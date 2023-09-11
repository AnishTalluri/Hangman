# assignment: programming assignment 1
# author: Anish Talluri
# date: 1/23/2023
# file: hangman.py is a program that has the user guess a word based on the length they chose (or if not randomly selected) with a limited amount of lives.
# file (cont): The user plays until they completely solve the word or run our of lives, but then are presented with the option of if they want to play again or not. 
# input: user inputs a string
# output: program outputs a string

from random import choice, randint

dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12
def import_dictionary(filename):
    dictionary = {}
    max_size = 12
    with open(dictionary_file) as f:
        lines = [line.rstrip() for line in f]
        lines = sorted(lines, key=len)      # Sort the list of words by word length (frpm shortest to longest)
        for i,val in enumerate(lines):      # Strip the tabbed spaces in the beginning of each word in the list
            lines[i] = val.strip()
        for i in lines:
           if len(i) > max_size:
              dictionary[max_size].append(i)
           else:
            if len(i) in dictionary:
                dictionary[len(i)].append(i)
            else:
               dictionary[len(i)] = [i]
    return dictionary

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options():

    # User inputs their preferred word length via the "size" variable
    try:
        size = int(input("Please choose a size of a word to be guessed [3 - 12, default any size]:\n"))
        if size >= 3 and size <= 12:
            print(f"The word size is set to {size}.\n")
    except ValueError:
        size = randint(3, 12)
        print("A dictionary word of any size will be chosen.\n")
    if size > 12 or size < 3:
        size = randint(3, 12)
        print("A dictionary word of any size will be chosen.\n")
    

    # User inputs their preferred lives amount via the "lives" variable
    try:
        lives = int(input("Please choose a number of lives [1 - 10, default 5]:\n"))
    except ValueError:
        lives = 5
    if lives < 1 or lives > 10:
        lives = 5
    print(f"You have {lives} lives.\n")

    return (size, lives)


# MAIN

if __name__ == '__main__' :
    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print a game introduction
    print("Welcome to Hangman Game!\n")

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    start_end_game = True
    while start_end_game == True:

    # set up game options (the word size and number of lives)
        (size, lives) = get_game_options()

    # select a word from a dictionary (according to the game options)
    # use choice() function that selects an item from a list randomly, for example:
    # mylist = ['apple', 'banana', 'orange', 'strawberry']
    # word = choice(mylist)
        guessing_word = choice(dictionary[size])
        letters_chosen = []
        guessing_word_list = list(['__ ']*size)
        separator = ', '
        word_reveal = '__ ' * size
        bubble_lives = 'O' * lives

        # START GAME LOOP   (INNER PROGRAM LOOP)
        while lives > 0:
            
        # format and print the game interface:
        # Letters chosen: E, S, P                list of chosen letters
        # __ P P __ E    lives: 4   XOOOO        hidden word and lives
            if "-" in guessing_word.upper():        # Checks to see if a - is in the guessing word and if so it replaces an _ in place of where the - is
                        for i, j in enumerate(guessing_word.upper()) :
                            if j == "-":
                                guessing_word_list[i] = "-" + " "  
                        word_reveal = ''.join(guessing_word_list)

            print(f'Letters chosen: {separator.join(letters_chosen)}\n')
            print(f'{word_reveal}    lives: {lives}   {bubble_lives}\n')

            letter = input("Please choose a new letter >\n").upper()        # ask the user to guess a letter

            if len(letter) == 1 and letter.isalpha():       # Checks if letter is one letter only and is a letter in the alphabet
                if letter in letters_chosen:        # Checks to see if letter is in the lost (a duplictae)
                    print('You already have chosen this letter\n')

                else:  
                    letters_chosen.append(letter)       # update the list of chosen letters
                    if letter in guessing_word.upper():        # if the letter is correct update the hidden word,
                        print("You guessed right!\n")
                        for i, j in enumerate(guessing_word.upper()) :
                            if j == letter:
                                guessing_word_list[i] = letter + " "  
                        word_reveal = ''.join(guessing_word_list)
                        if "__ " not in word_reveal:
                            print(f"Congratulations!!! You won! The word is {guessing_word.upper()}!\n")        # User correctly guesses the word
                            break       # END GAME LOOP   (INNER PROGRAM LOOP)

                    else:       # else update the number of lives
                        lives -= 1
                        print('You guessed wrong, you lost one life.\n')
                        bubble_lives = bubble_lives.replace('O', 'X', 1)
                        if lives == 0:
                            print(f"You lost! The word is {guessing_word.upper()}!\n")      # User runs out of lives --> Game over
                            break       # END GAME LOOP   (INNER PROGRAM LOOP)

        yes_no = input("Would you like to play again [Y/N]?\n").upper()        # asks if the user wants to continue playing

        if yes_no == 'n' or yes_no == 'N':      # if yes start a new game, otherwise terminate the program
            print("Goodbye!\n")
            break       # END MAIN LOOP (OUTER PROGRAM LOOP)
        else:
            start_end_game == True  # If user says Y or y --> Game starts from the top where user chooses all of their preffered settings agains