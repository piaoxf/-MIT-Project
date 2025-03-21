# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

#同じフォルダにある場合は、以下のように記述する
WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    isAllGuessed = True
    for letter in secretWord:
        if letter not in lettersGuessed:
            isAllGuessed = False
            break
    return isAllGuessed



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            secretWord = secretWord.replace(letter, '_ ')

    return secretWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string

    getAvailableLetters = string.ascii_lowercase
    for letter in lettersGuessed:
        if letter in getAvailableLetters:
            getAvailableLetters = getAvailableLetters.replace(letter, '')
    
    return getAvailableLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("-------------")

    leftGuesses = 8
    lettersGuessed = []
    while leftGuesses > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
        
        print("You have", leftGuesses, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))

        guss = input("Please guess a letter: ").lower()

        if guss in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
            continue
        
        lettersGuessed.append(guss)
        
        if guss in secretWord:
            print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
            continue
        else:
            print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
        
        leftGuesses -= 1
        print("-------------")

    if leftGuesses == 0:
        print("Sorry, you ran out of guesses. The word was else.")







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
secretWord = 'apple'
hangman(secretWord)
