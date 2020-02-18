word1 = 'apple' 
letters = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    availableLetters = list(string.ascii_lowercase)
    forCheck = list(string.ascii_lowercase)
    
    for char in lettersGuessed:
        if char in forCheck:
            availableLetters.remove(char)
    
    return (''.join(availableLetters))
    
print(getAvailableLetters(letters))
