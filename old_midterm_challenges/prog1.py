# Problem 3
# 10/10 points (graded)
# Implement a function called closest_power that meets the specifications below.
# https://github.com/OllieGitHub1/MITx-6.00.1x-/blob/master/Midterm_Exam/Problem_4.py
# https://github.com/anarayanan86/MITx-6.00.1x/blob/master/Midterm_Exam/Problem_4.py
# https://github.com/dlujHub/MITx-6.00.1x-Introduction-to-Computer-Science-and-Programming-Using-Python/blob/master/Midterm_Exam/Problem_4.py

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here