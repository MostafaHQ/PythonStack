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


class User:

    def __init__(self, name, eamil):
        self.name = name
        self.email = eamil
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self):
        self.account.deposit(100)
        return self

    def make_withdrawal(self):
        self.account.withdraw(50)
        return self

    def display_user_balance(self):
        return f"User:{self.name}, Balance:{self.account.account_balance}"

    # # def transfer_money(self, other_user, amount):
    # #     self.account -= amount


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
somebody = User("Somebody", "anybody@codingdojo.com")

guido.make_deposit().make_withdrawal()

print(guido.display_user_balance())
# print(monty.display_user_balance())
# print(somebody.display_user_balance())
