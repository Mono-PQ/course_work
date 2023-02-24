import re

def loaddata(filename): 
    '''
    Function to load the data into memory excluding the header. 
    Input:
    1. filename - file 
    '''
    with open(filename, "r") as f: 
        next(f)
        data = f.read()
        data = data.split('\n')
        data = data[:24]
    return data

def cleandata(data): 
    '''
    Function to clean the data from singapore_attractions.csv. 
    Input:
    1. data - list 
    '''
    splitdata = []
    for line in data: 
        line = line.split(";")
        splitdata.append(line)
    cleaned_data = []
    for ls in splitdata: 
        ls[1] = float(re.match('\d.\d|\d', ls[1]).group())
        if "minutes" in ls[2]: 
            time = float(re.match('\d+', ls[2]).group())
            time_hour = time/60 
            ls[2] = time_hour
        elif ls[2] == "NA": 
            ls[2] = 24.00
        elif "-" in ls[2]: 
            time = re.match('\d-\d', ls[2]).group()
            time_hour = float(time[-1])
            ls[2] = time_hour
        else: 
            ls[2] = float(ls[2][0]) 
        # Convert cost into float
        ls[3] = float(ls[3][2:len(ls[3])])
        ls = tuple(ls) 
        cleaned_data.append(ls)
    return cleaned_data

def writefile(lst):
    '''
    Function to write attactions data in the list of tuples to a text file. 
    Input: 
    lst - list
    '''
    string_list = [] 
    for item in lst: 
        temp = []
        temp.append(f'{item[0]}\n')
        temp.append(f'Rate: {item[1]} of 5\n')
        temp.append(f'Duration: {item[2]} hours\n')
        temp.append(f'Cost: S${item[3]:.2f}\n\n')
        temp = "".join(temp)
        string_list.append(temp)
    with open("sg_tours.txt", "w") as f: 
        f.writelines(string_list)
    print("File written successfully.")

def search_attraction(cleaned_data): 
    '''
    Function that allows user to search through the cleaned data for the 
    list of attractions and choose whether they would like to print the 
    results and total cost.
    Input:
    1. cleaned_data - list 
    '''
    s = input("Enter a keyword: ")
    found_lst = [] 
    for item in cleaned_data:
        if s.lower() in item[0].lower():
            found_lst.append(item)
    if found_lst != []: 
        total_costs = 0 
        for found_item in found_lst: 
            total_costs += found_item[3]
            print(f'{found_item[0]}, Cost: ${found_item[3]}')
        print(f'Total cost: ${total_costs:.2f}')
    else: 
        print(f'No result is found')
    print_result = input("Would you like to print the result? ")
    print()
    if print_result.lower() == 'y' or print_result.lower() == 'yes':
        for item in found_lst: 
            print(item)
        print()
        return True, found_lst 
    elif print_result.lower() == 'n' or print_result.lower() == 'no':
        return False, None
    else: 
        print("Input is invalid.")

def search_budget(cleaned_data): 
    '''
    Function that allows user to search for the list of attractions that matches the user's budget. 
    Input:
    1. cleaned_data - list 
    '''
    b = float(input("Enter your budget: "))
    found_lst = [] 
    for item in cleaned_data:
        if item[3] <= b:
            found_lst.append(item)
    if found_lst != []: 
        for found_item in found_lst: 
            print(f'{found_item[0]}, Cost: ${found_item[3]}')    
    else: 
        print(f'No result is found')
    print_result = input("Would you like to print the result? ")
    print()
    if print_result.lower() == 'y' or print_result.lower() == 'yes':
        for item in found_lst: 
            print(item)
        print()
        return True, found_lst 
    elif print_result.lower() == 'n' or print_result.lower() == 'no': 
        return False, None
    else: 
        print("Input is invalid.")
    
    
data = loaddata('singapore_attractions.csv')
cleaned_data = cleandata(data)

while True: 
    print("Welcome to Singapore!")
    print("Pick an option to choose your tour package (q to quit): \
            \n1. By keyword search\n2. By budget")
    option = input("Enter an option: ")
    if option == 'q':
        print("Bye,Bye")
        break
    else: 
        if option == "1": 
            prnt, result = search_attraction(cleaned_data)
            if prnt == True:
                writefile(result)
            else: 
                writefile('')
        if option == "2": 
            prnt, result = search_budget(cleaned_data)
            if prnt == True:
                writefile(result)
            else:
                writefile('')