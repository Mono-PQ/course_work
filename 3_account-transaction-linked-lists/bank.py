import datetime

class Account: 
    '''Bank account class which process and record any transactions associated with the account'''

    class Transaction: 
        '''Transaction class: Sub-class of Account'''
        def __init__(self, trans_type, amt): 
            '''Constructor for Transaction class'''
            self.trans = {trans_type: amt} # dictionary: key-value pair
            self.dt = datetime.datetime.now()
            self.next = None 
            self.prev = None 
    
    def __init__(self):
        '''Constructor for Account class'''
        self.last = None 
        self.first = None 
        self.size = 0 
        self.balance = 0 

    def __len__(self):
        '''Returns the number of transactions associated with the account'''
        return self.size

    def isEmpty(self): 
        '''Check if there is any record of transaction for the account'''
        if self.size == 0: 
            return True
        else: 
            return False

    @staticmethod
    def isValidAmt(amt):
        '''Static method to check if the input is valid. Only positive numbers are accepted'''
        try:
            amt = float(amt)
        except: 
            return False
        if amt > 0:
            return True
        else: 
            return False
    
    def deposit(self, amt):
        '''Deposit method which takes in an amount and adds to the balance if valid'''
        if self.isValidAmt(amt):
            self.balance += amt
            self.size += 1
            #Creation of a transaction instance
            t = self.Transaction("Deposit", amt)
            if self.first is None:
                self.first = t 
                self.last = t
            else:
                self.last.next = t 
                t.prev = self.last
                self.last = t
            print(f"Success: Deposited ${amt:.2f}")
        else: 
            print("Error: Invalid amount. Please enter an positive integer or float.")

    def withdraw(self, amt):
        '''Withdrawal method which deducts the withdrawn amount from the balance if there is sufficient funds'''
        if self.isValidAmt(amt):
            if amt <= self.balance:
                self.balance -= amt
                self.size += 1
                # Creation of a transaction instance 
                t = self.Transaction("Withdrawal", amt)
                if self.first is None:
                    self.first = t
                    self.last = t
                else: 
                    self.last.next = t
                    t.prev = self.last
                    self.last = t
                print(f"Success: Withdrawn ${amt:.2f}")
            else: 
                print("Error: Insufficient funds for the withdrawal.")
        else: 
            print("Error: Invalid amount. Please enter an positive integer or float.")
    
    def getHistory(self):
        '''Method to print out the list/history of account transactions reflecting the latest transaction first'''
        latest = self.last 
        if self.size == 0:
            print('No transaction records.')
        else:
            print("Transaction History:")
            while latest is not None:
                print(f"{latest.dt.strftime('%Y-%m-%d %H:%M:%S')}: {list(latest.trans.keys())[0]} - ${list(latest.trans.values())[0]:.2f}")
                latest = latest.prev