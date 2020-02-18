word1 = 'apple' 
letters = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    word = secretWord
    ls = list(word)
    count = 0
    for letter in ls:
        if letter in lettersGuessed:
            count = count + 1
    if count == len(word):
        return True
    else:
        return False
print(isWordGuessed(word1, letters))
