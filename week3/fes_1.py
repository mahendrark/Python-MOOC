animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals)

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    return sum([len(i) for i in aDict.values()])
    

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    result = None
    biggestOne = 0
    
    for key in aDict.keys():
        if len(aDict[key]) >= biggestOne:
            result = key
            biggestOne = len(aDict[key])
    return result
    
    
