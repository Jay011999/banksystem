import sys
import time
import random

'''This is to generate random password for account'''
l = "abcdefghijklmnopqrstuvwxyz"
u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = "1234567890"
sym="@#$%"
all=l+u+n+sym
length=8
password="".join(random.sample(all,length))


class Bank:
    balance=10000
    def account_creation(self,name,account_number):
        print("Welcome to new account creation!! ")
        self.name=name
        self.account_number=account_number
        print(name)
        print(account_number)
        print(password)
        print("Congratulions! Your account created succesfully")

    def account_detail(self,name,account_number):
        self.name = name
        self.account_number = account_number
        print("\nYouur account details are: \n")
        print(f"Account Holder: ",self.name )
        print(f"Account Number: ",self.account_number)
        print(f"Available balance: ",self.balance)

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Your current account balance is : ", self.balance)
        if(self.amount>0):
            print("Transaction complete.\nYour amount is deposited.")
        else:
            print("Please enter valid amount to be deposited.")
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Nu.{self.balance} only.")
            print()
        elif(self.balance - self.amount) < 1000:
            print("Minimum balance Rs 1000 is required.")
        else:
            self.balance = self.balance - self.amount
            print("Withdrawal transaction  completed of Rs: ",self.amount)
            print("Current account balance: ", self.balance)
            print()

    def check_balance(self):
        print("\nAvailable balance: ", self.balance)
        print()

    def options(self):
        print("Welcome to our bank ATM \n"
              "Please insert your card")
        print('''
            
            Please select an option:
            
            1.Account details
            2.Balance Enquiry
            3.Deposit
            4.Withdrawal
            5.Exit
            
             ''')

        while True:
            try:
                print("Please select an option :")
                option=int(input(""))
            except:
                print("Please choose from given options only!!\n")
                continue
            else:
                if option ==1:
                    Bank.account_detail(self,name,account_number)
                elif option==2:
                    Bank.check_balance(self)
                elif option==3:
                    print("\nWelcome in deposit menu:")
                    amount=int(input("\nEnter the amount to be deposited: "))
                    Bank.deposit(self,amount)
                elif option == 4:
                    print("\nWelcome in withdrawal menu:")
                    amount = int(input("\nEnter the amount want to withdrawn: "))
                    Bank.withdraw(self,amount)
                elif option==5:
                    time.sleep(3)
                    print('''Transaction completed.\nThanks for choosing our bank ''')
                    sys.exit()


name = input("Enter Account holder name: ")
account_number = int(input("Enter Account number : "))

print("welcome to our Bank."
      "\nplease select an option: \n"
      "1.Account creation\n"
      "2.For transactions \n"
      "3.Exit\n"
      )
while True:
    try:
        value = int(input(""))
    except:
        print("Please choose from given options only!!\n")
        continue
    else:
        obj1=Bank()
        if value==1:
            obj1.account_creation(name,account_number)
        elif value==2:
            obj1.options()
        elif value ==3:
            time.sleep(3)
            print("Thank you for choosing our bank.\n"
                  "Transaction completed")

            sys.exit()






#end of code

