# Write a function to calculate a factorial
n = int(input("Enter n: "))
def fact(n):
    fact = 1;
    for i in range(1,n+1):
        fact *= i
    return fact
print(fact(n))

##########################################################################

# function to count vowels in a string
string = "Hello World"
def count_vowels_cons(string):
    vowels = 0
    cons = 0
    for ch in string.lower():
        if ch in "aeiou":
            vowels += 1
        elif ch.isalpha():
            cons += 1
    print(f"Vowels in {string} are: {vowels}")
    print(f"Consonants in {string} are: {cons}")

count_vowels_cons(string)

###########################################################################

# function to return max of three numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

def Larger(a,b,c):
    if b<a>c:
        return a
    elif a<b>c:
        return b
    else:
        return c

print(f"Largest value is : {Larger(a,b,c)}")

#############################################################################

# function to check given number is prime or not

n = int(input("Enter n: "))
def is_prime(n):
    if n<=1:
        return "No"
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return "No"
    return "Yes"
print(is_prime(n))

##################################################################################



