# calculating exponential of something using recursion

base_num = int(input("Enter the base"))
power = int(input("Enter the power"))

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, (exp-1))
    
print("The answer is: ",recurPower(base_num, power))

