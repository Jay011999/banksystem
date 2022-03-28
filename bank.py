import sys
import time
import random

'''This is to generate random passord for account'''
l = "abcdefghijklmnopqrstuvwxyz"
u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = "1234567890"
sym = "@#$%"
all = l + u + n + sym
length = 8
password = "".join(random.sample(all, length))


class Bank:
    balance = 10000

    def account_creation(self):
        self.name = input("Enter Account holder name: ")
        self.account_number = int(input("Enter Account number : "))
        self.password=password
        print("Congratulions! Your account created succesfully")
        print('Your Name is ',self.name)
        print('Your account Number is',self.account_number)
        print('Your Password is',self.password)

    def account_detail(self):
        print("\nYour account details are: \n")
        print(f"Account Holder: ", self.name)
        print(f"Account Number: ", self.account_number)
        print(f"Available balance: ", self.balance)

    def deposit(self, amount):
        if (amount > 0):
            self.balance = self.balance + amount
            print("Your current account balance is : ", self.balance)
            print("Transaction complete.\nYour amount is deposited.")
        else:
            print("Please enter valid amount to be deposited.")
        print()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Rs. {self.balance} only.")
            print()
        elif (self.balance - amount) < 1000:
            print("Minimum balance Rs 1000 is required.")
        else:
            self.balance = self.balance - amount
            print("Withdrawal transaction  completed of Rs: ", amount)
            print("Current account balance: ", self.balance)
            print()

    def check_balance(self):
        print("\nAvailable balance: ", self.balance)
        print()

    def options(self):
        while True:
            try:
                option = int(input('''
                Please select an option:
                1. Account details
                2. Balance Enquiry
                3. Deposit
                4. Withdrawal
                5. Exit
                 '''))
            except:
                print("Please choose from given options only!!\n")
                continue
            else:
                if option == 1:
                    obj1.account_detail()
                elif option == 2:
                    obj1.check_balance()
                elif option == 3:
                    amount = int(input("\nEnter the amount to be deposited: "))
                    obj1.deposit(amount)
                elif option == 4:
                    amount = int(input("\nEnter the amount want to withdrawn: "))
                    obj1.withdraw(amount)
                elif option == 5:
                    time.sleep(3)
                    print('''Transaction completed.\nThanks for choosing our bank ''')
                    sys.exit()

print("welcome to our Bank.")
obj1 = Bank()
while True:
    try:
        value = int(input("\nplease select an option: \n"
      "1.Account creation\n"
      "2.For transactions \n"
      "3.Exit\n"))
    except:
        print("Please choose from given options only!!\n")
        continue
    else:
        if value == 1:
            obj1.account_creation()
        elif value == 2:
            obj1.options()
        elif value == 3:
            time.sleep(3)
            print("Thank you for choosing our bank.\n"
                  "Transaction completed")
            sys.exit()
