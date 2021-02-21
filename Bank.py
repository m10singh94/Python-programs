class Bank():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'{amount} added to your balance. Your present balance is {self.balance}')
    def withdrawal(self, amount):
        if(amount <= self.balance):
            self.balance = self.balance - amount
            print(f'{amount} deducted from your account. Your present balance is {self.balance}')
        else:
            print('Withdrawal unseccessful. Not enough funds.')
    def __str__(self):
        return "Owner's name : " + self.owner + "\nBalance : " + f"{self.balance}"
account = Bank('Maitreyi', 5000)
account.deposit(100)
account.withdrawal(3600)
print(account)
# account.withdrawal(1400)
# account.withdrawal(101)