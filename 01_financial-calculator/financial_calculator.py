def simple(P, r, t):
    '''
    Function that compute simple interest with the following argument:
    P: Principal Amount - Float 
    r: Annual interest rate - Float
    t: Time period (in years) - Integer
    A: Final amount - Float
    '''
    r = r / 100
    A = P*(1+(r*t))
    return A


def compound(P, r, t, n):
    '''
    Function that compute compound interest with the following argument:
    P: Principal Amount - Float 
    r: Annual interest rate - Float
    t: Time period (in years) - Integer
    n: No. of times interest is applied per year
    A: Final amount - Float
    '''
    r = r / 100
    A = P*((1+(r/n))**(n*t))
    return A

while True: 
    print("Welcome to Simple Financial Calculator!")
    print("Select the number of the type of interest to calculate (q to quit): \n 1. Simple interest \n 2. Compound interest")
    selection = input("Enter your option: ")
    # When user enters "q", print "Bye bye!" and quit the menu options. 
    if selection == "q":
        print("Bye bye!")
        break
    # When user enters the menu options apart from "q", check user's input as follows:
    # 1: Inform user that simple interest calculator is selected. Prompt users for the principal, annual interest  
    #    rate and time period to calculate the simple interest. Then, inform user of the final amount.
    # 2: Inform user that compound interest calculator is selected. Prompt users for the principal, annual interest  
    #    rate, time period and no. of times interest is applied per year to calculate the compound interest. Then, 
    #.   inform user of the final amount.
    # 3: Inform user that the option is invalid.
    else: 
        if selection == "1":
            print("You have chosen the simple interest calculator.")
            P = float(input("Enter principal: "))
            r = float(input("Enter annual interest rate: "))
            t = int(input("Enter time period in years: "))
            A = simple(P, r, t)
            print("Final amount is ${:.2f}".format(A))
        elif selection == "2":
            print("You have chosen the compound interest calculator.")
            P = float(input("Enter principal: "))
            r = float(input("Enter annual interest rate: "))
            t = int(input("Enter time period in years: "))
            n = int(input("Enter the number of times interest is applied per year: "))
            A = compound(P, r, t, n)
            print("Final amount is ${:.2f}".format(A))
        else:
            print("You have chosen an invalid option.")
    print()