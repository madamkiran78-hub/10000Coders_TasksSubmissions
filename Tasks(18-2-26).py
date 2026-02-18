# 1.check if a number is positive,negative or zero
n = int(input("Enter a number : "))
if(n>0):
    print(f"{n} is a Positive number")
elif(n<0):
    print(f"{n} is a Negative number")
else:
    print(f"{n} is Zero")

######################################################

# 2.take two numbers and print the larger one
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if(a>b):
    print(f"{a} is larger than {b}")
elif(b>a):
    print(f"{b} is larger than {a}")
else:
    print(f"{a} and {b} are equal")

############################################################

# 3.take a year and check if it is a leap year or not
year = int(input("Enter an year : "))
if(((year%400==0) or ((year%4==0)) and (year%100!=0))):
    print(f"{year} is a Leap year")
else:
    print(f"{year} is not a Leap year")

###################################################################

# 4. create a list of 5 numbers print sum and average
l = [1,2,3,4,5]
sum = 0
for i in l:
    sum = sum+i
avg = sum/len(l)
print(f"sum: {sum}")
print(f"avg: {avg}")

##############################################################

# 5. Take 3 subjects marks from user append it to the list then find the total and average of marks
marks = []
N = int(input("Enter no.of subjects: "))
for i in range(N):
    marks.append(int(input(f"Enter {i+1}/{N} subject marks: ")))
print(marks)
sum = 0
for i in marks:
    sum += i
avg = sum/len(marks)
print(f"sum: {sum}")
print(f"avg: {avg}")

###########################################################################

# 6. write a program that takes age and prints kids age<13 teen if age13 and 19 adult if is 20 and 59 else senior

age = int(input("Enter your age : "))
if(age<13):
    print("You are a Kid")
elif((age>=13) and (age<=19)):
    print("You are a Teen")
elif 20 <= age <=59 :
    print("You are an Adult")
else:
    print("you are a Senior")

##############################################################################
