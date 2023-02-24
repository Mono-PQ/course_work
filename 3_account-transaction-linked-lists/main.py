# Name: Tan Pei Quin 
# Email: peiquin.tan@digipen.edu

from bank import Account
import random, time

class bcolors:
    HEADER = '\033[95m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'


a1 = Account() 
a2 = Account() 
a3 = Account()

#1 - Check __len__ method. Expected output to be zero for both a1 and a2.
print(bcolors.HEADER + "Test case #1: __len__ method." + bcolors.ENDC)
print("No. of transactions for Account 1: ", len(a1))
print("No. of transactions for Account 2: ", len(a2))
print(bcolors.GREEN + "Expected output: 0 for both account 1 and 2" + bcolors.ENDC)
print()

#2 - Check isEmpty() method. Expected output to be True for a1 and a2.
print(bcolors.HEADER + "Test case #2: isEmpty() method." + bcolors.ENDC)
print("Is Account 1 void of transactions? ", a1.isEmpty())
print("Is Account 2 void of transactions? ", a2.isEmpty())
print(bcolors.GREEN + "Expected output: True for both accounts 1 and 2." + bcolors.ENDC)
print()

#3 - Check deposit() method. 
print(bcolors.HEADER + "Test case #3: deposit() method." + bcolors.ENDC)
a1.deposit(-30) # Expected output: Invalid amount error 
a1.deposit("Hello") # Expected output: Invalid amount error 
for i in range(10):
    a1.deposit(1000)
print(f"Balance of Account 1: ${a1.balance:.2f}") # Expected output: 10000
print(bcolors.GREEN + "Expected output: 2 lines of invalid inputs as negative number and strings were used. Loop is used to deposit $1000 for 10 times. Expected balance of account 1 is $10000." + bcolors.ENDC)
print()

#4 - Check withdraw() method.
print(bcolors.HEADER + "Test case #4: withdraw() method." + bcolors.ENDC)
a1.withdraw(-60) # Expected output: Invalid amount error  
a1.withdraw("String") # Expected output: Invalid amount error 
for i in range(3):
    a1.withdraw(550)
print(f"Balance of Account 1: ${a1.balance:.2f}") # Expected output: 8350
a1.withdraw(10000) # Expected output: Insufficient funds error
print(bcolors.GREEN + "Expected output: 2 lines of invalid inputs as negative number and strings were used. Loop is used to withdraw $550 for 3 times. Expected balance of account 1 is $8530. Attempt to withdraw $10000 will result in an insufficient fund error." + bcolors.ENDC)
print()

#5 - Check getHistory() method.
print(bcolors.HEADER + "Test case #5: getHistory() method." + bcolors.ENDC)
print(f"No. of transactions for Account1: {len(a1)}") # Expected output: 13
print(f"Is Account 1 void of transactions? {a1.isEmpty()}") # Expected output: False
print(bcolors.GREEN + "Expected output: Based on the previous tests, 13 transactions were made and number of transactions is no longer zero." + bcolors.ENDC)
print()
a1.getHistory()
print(bcolors.GREEN + "Expected output: 3 withdrawal transactions of $550 followed by 10 deposit transactions of $1000" + bcolors.ENDC)
print()

#6 - Check deposit() and withdraw() methods for another account instance
print(bcolors.HEADER + "Test case #6: deposit() and withdraw() methods for another account instance." + bcolors.ENDC)
a2.deposit(1000.23)
a2.deposit(150.70)
a2.deposit(5000)
a2.deposit(1000)
a2.withdraw(500)
a2.withdraw(20.90)
print(f"Balance of Account2: ${a2.balance:.2f}") # Expected output: 6630.03
print(bcolors.GREEN + "Expected output: 3 withdraw() methods for another account instance." + bcolors.ENDC)
print()

#7 - Check getHistory() method for another account instance
print(bcolors.HEADER + "Test case #7: getHistory() method for another account instance." + bcolors.ENDC)
print(f"No. of transactions for Account1: {len(a2)}") #Expected ouput: 6
print(f"Is Account 1 void of transactions? {a2.isEmpty()}") #Expect output: False
print(bcolors.GREEN + "Expected output: Based on the test case 6, 6 transactions were made and number of transactions is no longer zero." + bcolors.ENDC)
print()
a2.getHistory()
print(bcolors.GREEN + "Expected output: 2 withdrawal transactions of $500 and $20.90 followed by 4 deposit transactions of $1000, $5000, $150.70 and $1000.23" + bcolors.ENDC)
