# Take a string countn how many Vowels and consonants in it have
s = "Hello World"
vowels = 0
cons = 0
for ch in s.lower():
    if ch in ['a','e','i','o','u',]:
        vowels += 1
    else:
        cons += 1

print(f"vowels in {s} : {vowels}")
print(f"consonants in {s} : {cons}") 

###############################################################################

# Reverse a string without using slicing
s  = "Hello"
s1 = "".join(reversed(s))
print(s1)

################################################################################

# Take a string replace every space with underscore
s = "Hello world"
s1 = s.replace(" ","_")
print(s1)

###############################################################################

# Take a comma seperated string convert it into a list
a = "1,kiran,30000"
l = a.split(",")
print(l)

##############################################################################

# create a list of five favourite movies and print second one
movies = ['Rajasaab','Bhaahubali','Rachcha','Pushpa','Spirit']
print(movies[1])

##############################################################################

# add one movie using append() and remove() one movie using remove()
movies.append("Toxic")
print(movies)
movies.remove('Pushpa')
print(movies)

#################################################################################

# Sort a list of numbers in ascending and descending 
l = [1,2,6,3,4,5]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

##################################################################################

# Take 5 integers from user store them in list and print their sum
l = []
for i in range(5):
    l.append(int(input(f"Enter vlaue for {i+1}")))
sum = 0
for i in l:
    sum += i
print(sum)
    

######################################################################################

# create a nested list try to traverse access elements from nested list
nested_list = [[1,2],[2,3,52],[6,4,2,4]]
print(nested_list[1][2])

#################################################################################
