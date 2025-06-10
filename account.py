class Account:
    def __init__(self, acc_num, name, pin, balance=0):
        self.acc_num = acc_num
        self.name = name
        self.pin = pin
        self.balance = balance
    
    def Deposit(self, amount):
        if amount > 0:
            self.balance+= amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance-= amount
            return True
        return False
    
    def check_balance(self):
        return self.balance
    
    def to_dict(self):
        return {
            'name': self.name,
            'account_number': self.acc_num,
            'pin': self.pin,
            'balance': self.balance
        }
    
    @staticmethod
    def from_dict(data):
        return Account(data['name'], data['account_number'], data['balance'], data['pin'])

    def __str__(self):
        return f'Account: [{self.acc_num}], Name: {self.name}, Balance: {self.balance}'

# CReate instance of the the Account class
acc1 = Account(101,'Saad',123)
print(acc1.__str__())