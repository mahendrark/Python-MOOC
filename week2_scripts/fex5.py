# Program to find the GCD of two numbers iteratively

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test = min(a,b)
    while test >=0:
        if (a % test == 0) and (b % test == 0):
            break;
        else:
            test = test - 1
    return test  
    
print("The GCD of " + str(num1) + " and " + str(num2) + " is "+ str(gcdIter(num1, num2)))


