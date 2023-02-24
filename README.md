# Course Work Repository 

## Table of Content 
- [Course Work Repository](#course-work-repository)
  - [Table of Content](#table-of-content)
    - [Financial Calculator](#financial-calculator)
    - [Singapore Attractions Search Menu](#singapore-attractions-search-menu)
    - [Account Transaction](#account-transaction)

### Financial Calculator
A simple python program to compute simple interest and compound interest based on principal amouunt, annual interest rate, and time period inputted by the user.

To run the program, you can download the `.py` file from 1_financial-calculator folder to your local machine and run the file using `python financial-calculator.py`.


### Singapore Attractions Search Menu
A menu system that allows user to search Singapore's attractions based on keyword or budget from `singapore_attractions.csv` file that contains data scrapped from [tripadvisor](https://www.tripadvisor.com.sg/Attraction_Products-g294265-zfg12131-Singapore.html). User may also print/save the results to a text file if they so wish. 

To run the program:
```python 
python3 singapore-attraction-search-menu.py
```

Sample program running in terminal
```
Welcome to Singapore!
Pick an option to choose your tour package (q to quit):             
1. By keyword search
2. By budget
Enter an option: 1
Enter a keyword: bike
Lion City Bike Tour of Singapore, Cost: $80.0
Scenic Bike Tour: Enchantment Of Marina Bay, Cost: $51.35
Total cost: $131.35
Would you like to print the result? y

('Lion City Bike Tour of Singapore', 5.0, 4.0, 80.0)
('Scenic Bike Tour: Enchantment Of Marina Bay', 5.0, 3.0, 51.35)

File written successfully.
Welcome to Singapore!
Pick an option to choose your tour package (q to quit):             
1. By keyword search
2. By budget
Enter an option: q
Bye,Bye
```

To run the program, you need to download the `Singapore Attactions Search Menu` folder and run the python script via your terminal window.


### Account Transaction
An account transaction program that tracks and records each transaction associated with the account. Transactions are only limited to deposit and withdrawal. Doubly-linked list is used to represent the transaction in each node. 

To run the program:
```python 
python3 main.py
```

The main class and methods can be found in `bank.py`. The benefits of using a doubly linked list is the ability to traverse through all nodes in both directions, forward and backward. This allows more flexibility for `getHistory()` method where the transactions are arranged from the latest to oldest. Time complexity is `O(n)`. 

The time complexity for inserting a node at the end of a doubly linked list is `O(1)`. This is more suitable for transaction management given that the latest transaction are usually ordered based on time. The latest deposit or withdrawal transactions can be added to the last node more efficiently.

Doubly linked list is more flexible in terms of memory usage where references to data are stored as part of their own element. Thus, modifications (such as inserting or deleting memory references to the data) is more efficient by updating the references of the nodes of the affected insert or deletion. 


