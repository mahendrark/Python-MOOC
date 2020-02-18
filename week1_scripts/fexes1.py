# Prints the sum of the natural numbers from 1 to n, including n
# Finger exercise (fex)

num = 1
add = 0
fromuser = input("Please enter a # until while all the # are to be summed: ")
end = int(fromuser)
while num<=end:
    add = add + num
    num += 1
print(add)

