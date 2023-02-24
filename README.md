# Course Work Repository 

## Table of Content 
- [Course Work Repository](#course-work-repository)
  - [Table of Content](#table-of-content)
    - [Financial Calculator](#financial-calculator)
    - [Singapore Attractions Search Menu](#singapore-attractions-search-menu)

### Financial Calculator
A simple python program to compute simple interest and compound interest based on principal amouunt, annual interest rate, and time period inputted by the user.

To run the program, you can download the `.py` file from 1_financial-calculator folder to your local machine and run the file using `python financial-calculator.py`.

### Singapore Attractions Search Menu
A menu system that allows user to search Singapore's attractions based on keyword or budget from `singapore_attractions.csv` file that contains data scrapped from [tripadvisor](https://www.tripadvisor.com.sg/Attraction_Products-g294265-zfg12131-Singapore.html). User may also print/save the results to a text file if they so wish. 

To run the python
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