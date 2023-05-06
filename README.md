# Course Work Repository 

## Table of Content 
- [Course Work Repository](#course-work-repository)
  - [Table of Content](#table-of-content)
    - [Financial Calculator](#financial-calculator)
    - [Singapore Attractions Search Menu](#singapore-attractions-search-menu)
    - [Account Transaction](#account-transaction)
    - [K Nearest Neighours Function](#k-nearest-neighours-function)
    - [Linear Regression Function](#linear-regression-function)
    - [Logistic Regression](#logistic-regression)
    - [Get Tweets Using Twitter API](#get-tweets-using-twitter-api)
    - [Predict Baseball Player Salaries](#predict-baseball-player-salaries)
    - [Bike Ride Analysis](#bike-ride-analysis)

### Financial Calculator
A simple python program to compute simple interest and compound interest based on principal amouunt, annual interest rate, and time period inputted by the user.

To run the program, you can download the `.py` file from 1_financial-calculator folder to your local machine and run the file using `python financial-calculator.py` under *1_financial-calculator* folder.

<hr />

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

To run the program, you need to download the *2_singapore-attraction-search-menu* folder and run the python script via your terminal window.

<hr />

### Account Transaction
An account transaction program that tracks and records each transaction associated with the account. Transactions are only limited to deposit and withdrawal. Doubly-linked list is used to represent the transaction in each node. 

To run the program:
```python 
python3 main.py
```

The main class and methods can be found in `bank.py` under *3_account-transaction* folder. The benefits of using a doubly linked list is the ability to traverse through all nodes in both directions, forward and backward. This allows more flexibility for `getHistory()` method where the transactions are arranged from the latest to oldest. Time complexity is `O(n)`. 

The time complexity for inserting a node at the end of a doubly linked list is `O(1)`. This is more suitable for transaction management given that the latest transaction are usually ordered based on time. The latest deposit or withdrawal transactions can be added to the last node more efficiently.

Doubly linked list is more flexible in terms of memory usage where references to data are stored as part of their own element. Thus, modifications (such as inserting or deleting memory references to the data) is more efficient by updating the references of the nodes of the affected insert or deletion. 

<hr />

### K Nearest Neighours Function 
Implementation of K-Nearest Neighours algorithm to classify the age of abalone. Dataset originates from [UCI Machine Learning repository](https://archive.ics.uci.edu/ml/datasets/Abalone). Refer to `knn.py` for codes and implementation. A summary of the classification results can be found in `knn.ipynb` under *4_k-nearest_neighbour* folder. 

<hr />

### Linear Regression Function 
Implementation of linear regression and gradient descent algorithm from scratch to predict housing prices in Boston. Dataset originates from [UCI Machine Learning repository](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/). Refer to `lin_reg.ipynb` for codes and implementation. A summary of the results can be found in `technical_report.pdf` under *5_linear-regression* folder. 

<hr />

### Logistic Regression
Using logistic regression algorithm from scikit-learn library to classify bank notes as genuine or forged using dataset from [UCI Machine Learning repository](https://archive.ics.uci.edu/ml/datasets/banknote+authentication#). Regularization (i.e., Ridge regression, Lasso regression and Elastic Network) is explored to constrain the weights of the model. 

Ridge regression minimizes the weights of non-significant features while Lasso regression eliminates the weights of least important features (i.e., setting them to zero). Lasso regression automatically performs feature selection and outputs a sparse model.

Refer the `log_reg.ipynb` for the codes and implementation. A summmary of the results can be found in `technical_report` under *6_logistic-regression* folder. 

<hr />

### Get Tweets Using Twitter API
Fetch live tweets from Twitter and saved them in text file. Clean the text file by removing URL, converting letters to lower case, removing retweets and removing punctuation. Create a Hadoop mapper logic `mapper.py` and `reducer.py` to generate the word count of each word in the text file.

Refer to the `getTweets.ipynb`, `mapper.py` and `reducer.py` for the codes under *7_TweeterAPI* folder.

<hr />

### Predict Baseball Player Salaries
Mini speed hackathon for predicting baseball players' salaries using regression techniques within 3 hours. The data contains major league from 1986 and 1987 seasons with 322 observations. The objective of the hackathon is to obtain the best possible ${R^2}$ score. 

Refer to `baseball_regression.ipynb` for codes and results of various regression techniques such as `LinearRegressor`, `DecisionTreeRegressor`, `RandomForestRegressor` and `KNeighborsRegressor` under *8_baseball_salary_prediction* folder. Additionally, `RandomizedSearchCV` as opposed to `GridSearchCV` was also used to find an optimal parameter in view of time contraints. 

<hr />

### Bike Ride Analysis 
A capstone project for understanding the customer behaviours of a bike rental company to support the marketing campaign and strategy of converting casual riders to annual members. Some of the key questions that the analysis aims to cover include:
- What are the differences between an annual member and a casual rider?
- Why would a casual rider buy an annual membership?
- How does digital media affect the company's marketing tactices. 

Refer to `Google Analytics Capstone Track 1 Case Study.pdf` for the full report on the analysis. Detailed code and documentation of data preprocessing and visualisation can be found in `cyclistic_cleaned.ipynb` and `cyclistic_analysis.ipynb` respectively. Additionally, `Analysis.html` is a pandas-profiling report that provides a basic statistical summary of the cleaned data set. 

The website to download the data providede by Motivate International Inc can be reached using this [link](https://divvy-tripdata.s3.amazonaws.com/index.html). 

<hr />