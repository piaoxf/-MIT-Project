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