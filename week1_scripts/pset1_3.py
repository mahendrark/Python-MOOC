# PSET 1_3

strg = "azcbobobegghakl"
strlen = len(strg)
substr = ""
longest = ""

for n in range(strlen):
    if strg[n] >= strg[n-1]:
        substr += strg[n]
    else:
        substr = strg[n]
        
    if len(substr) > len(longest):
        longest = substr
print(longest)




