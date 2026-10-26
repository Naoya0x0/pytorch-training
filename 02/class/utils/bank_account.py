

class BankAccount:

    def __init__(self,name):
        self.name = name # 名前
        self.balance = 0 # 預金
        self.interest_rate = 0.01 #金利

    def deposit(self,money):
        self.balance += money

    def withdraw(self,money):
        self.balance -= money

    def get_balance(self):
        self.balance

    def set_interest_rate(self,rate):
        self.interest_rate = rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        