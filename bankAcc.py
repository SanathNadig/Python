class Account():
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        print ('Amount has successfully been credited into your account.\nCurrent balance is {}'.format(self.balance))
        
    def withdraw(self,amount):
        if amount>=self.balance:
            print ('Withdrawal amount cannot be greater than the balance.')
        else:
            self.balance -= amount
            print ('Amount has successfully been debited from your account.\nCurrent balance is {}'.format(self.balance))
            
    def __str__(self):
        details = 'Account Owner: ' + self.owner + '\n' + 'account balance: ' + str(self.balance)
        return details
    
acct1 = Account('Sanath',5000)

print (acct1.owner)

print (acct1.balance)

print (acct1)

acct1.deposit(500)

acct1.withdraw(1000)

acct1.withdraw(5000)