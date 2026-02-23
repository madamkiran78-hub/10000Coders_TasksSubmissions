# Create a tuple of your five favourite colors and print the third one
colors = ('red','blue','orange','pink','yellow')
print(colors[2])

##########################################################################

# Try to change a value
colors = list(colors)
colors[2] = 'White'
colors = tuple(colors)
print(colors)

###########################################################################

# create two sets of numbers show the union and difference
A = {7,8,9,4,5}
B = {4,5,6,1,2}
print(A | B)
print(A - B)

###########################################################################

# Find unique words from a list of repeated words using set
l = [4,2,5,4,6,8,2,2,]
unique = set()
for x in l:
    if l.count(x)==1:
        unique.add(x)
Repeated = set()
for x in l:
    if l.count(x)>1:
        Repeated.add(x)

print(unique)
print(Repeated)

############################################################################

# combine two tuples and count how many times a specific value appeard
t1 = (1,2,3,4,5,6)
t2 = (2,4,6,8,3,1)
t3 = t1+t2
print(t3)
s = set(t3)
print(s)
for x in s:
    print(f"{x} is appeared as: {t3.count(x)} times")

##############################################################################

