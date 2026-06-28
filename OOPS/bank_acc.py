# Topic: Bank Account Class
# Concept: Object-Oriented Programming (OOP)

class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.account = acc_no

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited") # print the amount debited
        print("Total balance =", self.get_balance()) # print the total balance after debiting

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited") # print the amount credited
        print("Total balance =", self.get_balance()) # print the total balance after crediting

    def get_balance(self):
        return self.balance

#EXAMPLE:
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
