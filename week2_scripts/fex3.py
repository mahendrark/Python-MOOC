# calculating exponential of something using recursion and looping constructs

base_num = int(input("Enter the base"))
power = int(input("Enter the power"))

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    ans = base
    while exp >= 0:
        if exp == 0:
            return 1
        else:
            ans = ans * recurPower(ans, (exp-1))
            return ans
        
print("The answer is: ",recurPower(base_num, power))
