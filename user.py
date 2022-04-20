class User:

    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount



    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

Sanoma = User("Sanoma")
Trinity = User("Trinity")
Alexander = User("Alexander")

Sanoma.make_deposit(1000)
Sanoma.make_deposit(2000)
Sanoma.make_deposit(5000)
Sanoma.make_withdrawal(3000)
Sanoma.display_user_balance()

Trinity.make_deposit(600)
Trinity.make_deposit(200)
Trinity.make_withdrawal(100)
Trinity.make_withdrawal(300)
Trinity.display_user_balance()

Alexander.make_deposit(300)
Alexander.make_withdrawal(20)
Alexander.make_withdrawal(50)
Alexander.make_withdrawal(30)
Alexander.display_user_balance()