
from Bank_Account import BankAccount
class SavingsAccount(BankAccount):
    def dummy(self):
        pass
    def calculate_interest(self):
        interest = (self.get_balance() * 5/100)
        return interest