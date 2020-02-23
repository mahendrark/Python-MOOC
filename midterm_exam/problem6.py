"""
 Implement a function that meets the specifications below.

def max_val(t): 
    '''
    t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t
    ''' 
    For example,

    max_val((5, (1,2), [[1],[2]])) returns 5.
    max_val((5, (1,2), [[1],[9]])) returns 9.

Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t 
    """ 
    
    def getList(struc):
        """
        This helper function takes all elements of t and returns a list
        """
        newL = []
        intvar = 0 # variable to compare types
        for char in struc:
            if type(char) == type(intvar):
                newL.append(char)
            else:
                newL.extend(getList(char))
        return newL
    
    maxOfList = getList(t)
    return max(maxOfList)
    
print(max_val((5, (1,2), [[1],[9]])))
