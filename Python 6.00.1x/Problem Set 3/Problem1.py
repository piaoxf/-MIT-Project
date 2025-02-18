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