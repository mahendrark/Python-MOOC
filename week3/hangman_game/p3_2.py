word1 = 'apple' 
letters = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    lettersList = list(secretWord) # ['a', 'p', 'p', 'l', 'e']
    outputUser = list(secretWord)
    
    for char in range(len(lettersList)): # 0 to 4
        if lettersList[char] in lettersGuessed:
            outputUser[char] = lettersList[char]
        else:
            outputUser[char] = '_ '
    toUser = ''.join(outputUser)        
    return toUser

print(getGuessedWord(word1, letters))

            
