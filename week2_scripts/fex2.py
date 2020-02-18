# calculating exponential of something using iteration 
 
base_num = int(input("Enter the base"))
power = int(input("Enter the power"))

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    ans = base
    if exp>1:
        while exp>1:
            ans = ans * base
            exp = exp - 1
        return ans
    elif exp == 1:
        return ans
    else:
        return 1

print("The answer is: ",+iterPower(base_num, power))
