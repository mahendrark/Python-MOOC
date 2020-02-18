# This program guesses the number that a user has thought in their mind,
# using the bisection search algorithm

print("Please think of a number between 0 and 100!")

low = 0
up = 100
n = int((low+up)/2)
user_ip = ""

#print("Is your secret number "+str(n)+"?")

while True:
    
    print("Is your secret number "+str(n)+"?") 
    
    print("Enter 'h' to indicate the guess is too high.", end=' ')
    print("Enter 'l' to indicate the guess is too low.", end=' ')
    print("Enter 'c' to indicate I guessed correctly.", end=' ')
    
    user_ip = input("")
    
    if user_ip == "c":
        print("Game over. Your secret number was: "+str(n))
        break;
    elif user_ip == "h":
        up = n
        n = int((low+up)/2)
    elif user_ip == "l":
        low = n
        n = int((low+up)/2)
    else:
        print("Sorry, I did not understand your input.")
