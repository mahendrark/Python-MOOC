# PSET 1.2

givenstr = 'obobopobobbobbobobboboboobbobbbo'
str_len = len(givenstr)
print(str_len)
count = 0

for an in range(0,(str_len - 2)):
    if givenstr[an] == "b" and givenstr[an+1] == "o" and givenstr[an+2] == "b":
        count += 1

print(count)
        


