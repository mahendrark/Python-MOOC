# PSET 1.2

givenstr = 'obobopobobbobbobobboboboobbobbbo'
str_len = len(givenstr)
print(str_len)
count = 0

for an in range(0,(str_len - 2)):
    if givenstr[an] == "b" and givenstr[an+1] == "o" and givenstr[an+2] == "b":
        count += 1

print(count)
        

"""
Implementation with function:

def countBobs(wordbob):
    """
    Prints the number of times the string 'bob' occurs in s. 
    For example, if s = 'azcbobobegghakl', then your program should print
    """
    count = 0
    strlen = len(wordbob)

    for i in range(0, strlen-2):
        if wordbob[i] == 'b' and wordbob[i+1] == 'o' and wordbob[i+2] == 'b':
            count += 1
    return count
"""