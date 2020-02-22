# Write a recursive Python function, given a non-negative integer N, 
# to count and return the number of occurrences of the digit 7 in N.
#
# For example:
# count7(717) -> 2
# count7(1237123) -> 1
# count7(8989) -> 0
#
# Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), 
# while doing integer division by 10 removes the rightmost digit (126 / 10 is 12).
#
# This function has to be recursive; you may not use loops! 
# This function takes in one integer and returns one integer.
# https://github.com/VasuGoel/mitx-6.00.1x/blob/master/Exams/Midterm%20Exam/problem3.py

def count7(num):
    """
    input: a non-negative integer
    output: count of the # of times 7 appears among the digits of the number
    """
    if num == 0:
        return 0
    elif num%10 != 7:
        return count7(num//10)
    else:
        return 1 + count7(num//10)

print(count7(7777777))
