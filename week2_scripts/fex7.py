# Program to check if a given character is in a given string sorted alphabetically

char_in = input("Please enter the character that must be checked: ")
aStr_in = input("Please enter a string that is alphabetically sorted: ")

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    low = 0
    up = len(aStr)
    
    if aStr == "":
        return False
        
    if len(aStr) == 1:
        return aStr == char
        
    # Base case to check if the middle character is same as test character
    if char == aStr[up//2]:
        return True
    
    midIndex = len(aStr)//2 
    midChar = aStr[midIndex]
        
    if char < midChar:
        return isIn(char, aStr[:midIndex])
    else:
        return isIn(char, aStr[midIndex+1:])
        
print(isIn(char_in, aStr_in))
