# Problem Set 2, hangman.py
# Name: Patryk Rogala
# Collaborators: None
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False

    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    for char in secret_word:
        if char not in letters_guessed:
            secret_word = secret_word.replace(char, "_ ")

    return secret_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase

    for char in letters_guessed:
        alphabet = alphabet.replace(char, "")

    return alphabet



def hangman(secret_word):
    guesses_left = 6
    warnings_left = 3

    letters_guessed = []

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    while guesses_left > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("-------------")
        print("You have", warnings_left, "warnings left.")
        print("You have", guesses_left, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()
        if not guess.isalpha():
            print("Oops! That is not a valid letter. You have", warnings_left, "warnings left:", get_guessed_word(secret_word, letters_guessed))
            if warnings_left > 0: warnings_left -= 1
            else: guesses_left -= 1
        elif guess in letters_guessed:
            print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
            if warnings_left > 0: warnings_left -= 1
            else: guesses_left -= 1
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("ops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            guesses_left -= 1
            letters_guessed.append(guess)

    print("-------------")
    if is_word_guessed(secret_word, letters_guessed):
        total_score = guesses_left * len(set(secret_word))
        print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        print("Your total score for this game is:", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word): return False
    for i in range(len(my_word)):
        if my_word[i] != "_" and my_word[i] != other_word[i]: return False
        if my_word[i] == "_" and other_word[i] in my_word: return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)
    if len(possible_matches) == 0:
        print("No matches found")
    else:
        print(" ".join(possible_matches))



def hangman_with_hints(secret_word):
    guesses_left = 6
    warnings_left = 3

    letters_guessed = []

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    while guesses_left > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("-------------")
        print("You have", warnings_left, "warnings left.")
        print("You have", guesses_left, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()
        if guess == "*":
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif not guess.isalpha():
            print("Oops! That is not a valid letter. You have", warnings_left, "warnings left:", get_guessed_word(secret_word, letters_guessed))
            if warnings_left > 0: warnings_left -= 1
            else: guesses_left -= 1
        elif guess in letters_guessed:
            print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
            if warnings_left > 0: warnings_left -= 1
            else: guesses_left -= 1
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("ops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            guesses_left -= 1
            letters_guessed.append(guess)

    print("-------------")
    if is_word_guessed(secret_word, letters_guessed):
        total_score = guesses_left * len(set(secret_word))
        print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        print("Your total score for this game is:", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
