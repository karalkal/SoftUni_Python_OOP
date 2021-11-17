class Account:
    def __init__(self, id: int, name: str, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, top_up):
        self.balance += top_up
        return self.balance

    def debit(self, withdraw):
        if withdraw > self.balance:
            return "Amount exceeded balance"
        else:
            self.balance -= withdraw
            return self.balance

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())
account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
