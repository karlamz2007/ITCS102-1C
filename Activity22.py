def PricelistFunction():
    loan = eval(input("Enter Loan Amount :  \t "))
    loanperiod = eval(input("Enter Loan Period in years :   \t"))
    loanperiod *= 12
    balance = loan 
    principal = loan / loanperiod

    print("LOAN BREAKDOWN")
    for x in range (1,loanperiod,1):
        balance -= principal
        interest = balance * 0.03
        monthly = principal + interest
        print(f"{x}\t\t\t | {round(principal,2)}\t\t\t\t |\t{round(balance,2)}\t\t\t | \t{round(interest,2)}\t\t\t | \t {round(monthly)}\t\t\t |")
