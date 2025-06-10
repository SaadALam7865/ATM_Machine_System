from account import Account
import json
import os

class BankSystem:
    def __init__(self,filename='account.json'):
        self.balance = []
        self.filename = filename
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try:
                    data = json.load(f)
                    self.balance = [Account.from_dict(item) for item in data]
                except json.JSONDecodeError:
                    self.balance = []
    
    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump([Account.to_dict(acc) for acc in self.balance], f, indent=4)
                    

    def create_account(self, acc_num, name,pin):
        if self.find_account(acc_num):
            return None # already account exists
        acc = Account(acc_num,name,pin)
        self.balance.append(acc)
        self.save_data()
        return acc
    
    def authenticate(self,acc_num, pin):
        for acc in self.balance:
            if acc.acc_num == acc_num and acc.pin == pin:
                return acc
        return None
    
    def find_account(self,acc_num):
        for acc in self.balance:
            if acc.acc_num == acc_num:
                return acc
            return None
    
    def save_data(self):
        with open('accounts.json', 'w') as f:
            json.dump([
                {
                   'acc_number': acc.acc_num,
                   'name': acc.name,
                   'pin': acc.pin,
                   'balance': acc.balance

                } for acc in self.balance
            ],f, indent=4)
    
    def load_data(self):
        if os.path.exists('accounts.json'):
            with open('accounts.json', 'r') as f:
                try:
                    data = json.load(f)
                    for item in data:
                        acc = Account(item['acc_number'], item['name'],item['pin'],item['balance'])
                        self.balance.append(acc)
                except json.JSONDecodeError:
                    self.balance = []

    
     
    
    