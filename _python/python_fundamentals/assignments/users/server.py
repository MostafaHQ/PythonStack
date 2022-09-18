from unicodedata import name


class User:

    def __init__(self, name, eamil):
        self.name = name
        self.email = eamil
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        return f"User:{self.name}, Balance:{self.account_balance}"

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
somebody = User("Somebody", "anybody@codingdojo.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(300)
guido.make_withdrawal(200)

monty.make_deposit(100)
monty.make_deposit(200)
monty.make_withdrawal(50)
monty.make_withdrawal(70)

somebody.make_deposit(500)
somebody.make_withdrawal(200)
somebody.make_withdrawal(100)
somebody.make_withdrawal(50)


print(guido.display_user_balance())
print(monty.display_user_balance())
print(somebody.display_user_balance())
