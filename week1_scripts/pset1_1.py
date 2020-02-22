# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5

def vowelCount(strings):
    """
    Input: a string
    Returns: number of vowels in that string
    """
    count = 0

    for ch in strings:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count += 1
    return count

s = input("Please enter a string here: ")
print("Number of strings: ",vowelCount(s))    


