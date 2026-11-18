from Current_Account import CurrentAccount
from SimpleAccount import SimpleAccount
from Bank_Account import BankAccount
from SavingsAccount import SavingsAccount
#Create an abject of current account


# s1 = SimpleAccount()
# s1.method1()


# bnkacc= BankAccount()             # not posible because we cannot  create an object of an abstract 
# bnkacc.deposit_amount()

currentAcc = CurrentAccount()
currentAcc.dummymethod()                 #method is defined in the class
currentAcc.deposit_amount(1000)           # method is defined in the parent class
 
# print(f'balance amount is :{currentAcc.__account_balance}') #cannot be done because variable is proteected from being accesed outside 
# currentAcc.display_balance()

# currentAcc.display_balance()
currentAcc.deposit_amount(-1700)
currentAcc.display_balance()

currentAcc.deposit_amount(800)
currentAcc.display_balance()



print("**********************************************************************")
savingsAcc = SavingsAccount()
savingsAcc.dummy()

savingsAcc.deposit_amount(100)
savingsAcc.display_balance()

savingsAcc.withdraw(50)
savingsAcc.display_balance()

savingsAcc.withdraw(100)
savingsAcc.display_balance()


savingsAcc.calculate_interest()
print(f'interest amount is: {savingsAcc.calculate_interest()}')



print("helloooooooooo")
