# Find second largest number in array
arr = [1,2,8,6,8,3,9,9]
fl = arr[0]
sl = arr[1]

if arr[1]>arr[0]:
    temp = arr[0]
    fl = arr[1]
    sl = temp

for i in range(len(arr)):
    if fl<arr[i]:
        sl = fl
        fl = arr[i]
    if sl<arr[i]<fl:
        sl = arr[i]
        
print(f" The second largest number in arr in: {sl}")

################################################################################

# Remove duplicates from array
arr = [1,2,8,6,8,3,9,9]
new_arr = []
for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print(new_arr)

##############################################################################

# check if a string is palindrome
s = "hello"
rev_s = s[::-1]
if (s==rev_s):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")

################################################################################

# # find missing number from 1 to N
arr = [1,2,3,4,6,7,8]
n = len(arr)+1
sum = n*(n+1)/2
arr_sum = 0
for i in arr:
    arr_sum += i

res = int(sum-arr_sum)
print(f"missing number is: {res}")

###################################################################################

# Reverse ecah word in a sentence
sen = "Hello this is kiran"
words = sen.split(" ")
rev_words = []
for i in words:
    rev = i[::-1]
    rev_words.append(rev)

new_s = " ".join(rev_words)
print(new_s)

###################################################################################

for i in range(5):
    for j in range(i+1):
        print(i+1,end="")
    print()

#####################################################################################

for i in range(5):
    for j in range(5,i,-1):
        print(5-j+1,end="")
    print()

######################################################################################

for i in range(5):
    for j in range(i+1):
        print(chr(65+i),end="")
    print()

######################################################################################
