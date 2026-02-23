# hotel management:
menu = {"idly":40,"dosa":60,"tea":10,"coffee":20}
print("Welcome, this is Out Today's Menu: ")
for key,value in menu.items():
    print(key,"  ",value)
n = int(input("Enter no of Orders: "))
order = []
for i in range(n):
    a = input(f"Enter order {i+1}: ")
    order.append(a.lower())

amount = 0
for i in range(len(order)):
     amount += menu.get(order[i])

print(f"Total Bill to Pay ${amount}")


#################################################################

# Write a program that stores 3 student details in a dictionary and list of marks for ecah student find avg marks
students = {
           "name" : ["A","B","C"],
           "marks" : [[60,70,80],[70,85,60],[90,75,81]]
}
for i in range(len(students["name"])):
     name = students["name"][i]
     marks = students["marks"][i]
     avg = sum(marks)/len(marks)
     print(f"Student {name} has average marks: {avg:.2f}")


###############################################################################
           
