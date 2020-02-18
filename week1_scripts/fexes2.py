# Program counts the number of vowels in a user-entered word

userword = input("Please enter a word here: ")
vowelcount = 0
for alphabet in userword:
    if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u':
        vowelcount += 1
print("The # of vowels in the word you entered is: ",vowelcount)
