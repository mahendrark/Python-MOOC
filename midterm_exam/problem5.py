# Write a Python function that returns a list of keys in aDict with the value target.
# The list of keys you return should be sorted in increasing order.
# The keys and values in aDict are both integers.
# If aDict does not contain the value target, you should return an empty list.)

"""
This function takes in a dictionary and an integer and returns a list.

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here  
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    keyList = []
    for x in aDict:
        if aDict[x] == target:
            keyList.append(x)
    keyList.sort()
    return keyList

dic = {2:3, 4:3, 5:3, 7:0, 6:5, 9:0, 1:0}
aim = 2

print(keysWithValue(dic, aim))
        
