class Bank:
    def __init__(self):
        self.customers = {
            1 : {"name" : "Vin" , "balance":5000},
            2 : {"name" : "John" , "balance":10000},
            3 : {"name" : "Sam" , "balance":2000},
            4 : {"name" : "Rin" , "balance":8000},
            5 : {"name" : "Tin" , "balance":15000}  }

    def deposit(self,cust_id,amount):
        if cust_id in self.customers:
            customer = self.customers[cust_id]
            customer["balance"] += amount
            print(f"{customer["name"]} is deposited {amount}. New Balance is: {customer["balance"]}")

        else:
            print("Customer not Found")

    def Withdraw(self,cust_id,amount):
        if cust_id in self.customers:
            customer = self.customers[cust_id]
            if customer["balance"] >= amount:
                customer["balance"] -= amount
                print(f"{customer["name"]} is Withdraw {amount}. New Balance is: {customer["balance"]}")
            else:
                print(f"Insufficient Balance. Current balance is: {customer["balance"]}")
        else:
            print("Customer not Found")

    def check_balance(self,cust_id):
        if cust_id in self.customers:
            customer = self.customers[cust_id]
            print(f"{customer["name"]}'s Balance is: {customer["balance"]}")
        else:
            print("Customer not Found.")

bank=Bank()


print(" -- Available Services -- ")
print("1.Deposit")
print("2.Withdraw")
print("3.check Balance")
print("4.Exit")
while True:

    choice = int(input("Enter your choice: "))

    if choice==1:
        cust_id = int(input("Enter your Customer_id: "))
        amount = int(input("Enter Amount to Deposit: "))
        bank.deposit(cust_id,amount)

    elif choice==2:
        cust_id = int(input("Enter your Customer_id: "))
        amount = int(input("Enter Amount to Withdraw: "))
        bank.Withdraw(cust_id,amount)

    elif choice==3:
        cust_id = int(input("Enter your Customer_id: "))
        bank.check_balance(cust_id)

    elif choice==4:
        print("Exit...... Thank You....")
        break
    else:
        print("Choose the Services Between 1 - 4 Only.")

                 
