# Problem 4
# 15/15 points (graded)
# Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters. 
# For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

#This function takes in a list of strings and returns a list of strings. Your function should not modify aList.
# https://github.com/FlashPilot/MITx-6.00.1x/blob/master/Midterm%20Problem%204.py

def lessThan4(aList):
    subL = []

    for i in aList:
        if len(i)<4:
            subL.append(i)
    return subL

bList = ["apple", "cat", "dog", "banana"]
print(lessThan4(bList))

