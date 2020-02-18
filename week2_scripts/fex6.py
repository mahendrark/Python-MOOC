# GCD of two numbers using recursive

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if min(a,b) == 0:
        return max(a,b)
    else: 
        return gcdRecur(min(a,b), max(a,b) % min(a,b))
print("The answer is: ",gcdRecur(num1, num2))

