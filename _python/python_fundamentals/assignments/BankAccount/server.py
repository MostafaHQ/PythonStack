class BankAccount:
    def __init__(self, balance, int_rate):
        self.account_balance = balance
        self.interest_rate = int_rate

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if self.account_balance != 0:
            self.account_balance -= amount

        elif self.account_balance == 0:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        
        return self


    def display_account_info(self):
        return f"Balance: ${self.account_balance}"

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance = self.account_balance * self.interest_rate
        return self



account1 = BankAccount(0, 0.01)
account2 = BankAccount(100, 0.02)

account1.deposit(100).deposit(50).deposit(200).withdraw(250).yield_interest()
account2.deposit(350).deposit(100).withdraw(70).withdraw(50).withdraw(100).withdraw(150).yield_interest()


print(account1.display_account_info())
print(account2.display_account_info())

