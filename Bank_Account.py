





# Bank Account Management System 
# Develop a simple Bank Account Management System using Python OOP concepts. 
# Requirements 
# 1. Create an abstract class named BankAccount. 
# ○ Include an abstract method named calculate_interest(). 
# ○ Include a method named display_balance(). 
# 2. Encapsulate the account balance using a private attribute. 
# ○ Provide methods to deposit and withdraw money. 
# ○ Do not allow withdrawals greater than the available balance. 
# 3. Create two child classes: 
# ○ SavingsAccount 
# ○ CurrentAccount 
# 4. Implement the calculate_interest() method differently: 
# ○ Savings Account: Calculate 5% interest on the balance. 
# ○ Current Account: No interest (0%). 
# 5. Create objects of both account types and demonstrate: 
# ○ Depositing money. 
# ○ Withdrawing money. 
# ○ Displaying account balances. 
# ○ Calculating interest. 

from abc import ABC,abstractmethod

class BankAccount(ABC):
    #constructor of the class
    def __init__(self):
        self.__account_balance = 0
     #    self.__account_balance = account_balance      #Encapsulate the account balance using a private attribute. 

# this method must be inherited by abstract classes
    @abstractmethod
    def calculate_interest(self):
        pass
#We are displaying
    def display_balance(self):
         print(f'The account balance is : {self.__account_balance}')

# TO RETURN THE BALANCE AMOUNT.
    def get_balance(self):
         return self.__account_balance
          
         


    def deposit_amount(self,amount):
         if amount <= 0:
            # raise ValueError("amount must be intiger value")
            print("Deposite amount must be greater than zero")
            return
         self.__account_balance = self.__account_balance + amount
         print("Deposited amount:",amount)


    def withdraw(self,amount):
         if amount <= 0:
              print("Withdrawal amount must be greater than zero")
         elif amount > self.__account_balance:
              print("insufficent balance")
         else:
              self.__account_balance -= amount
              print("withdrawal amount",self.__account_balance)


         

