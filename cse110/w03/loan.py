"""
Program Specification
    Write a program to determine whether to loan money based on the following rules.

    First, ask for a rating from 1–10 on the following:
    How large is the loan?
    How good is your credit history?
    How high is your income?
    How large is your down payment?
    
    Then, you will create a boolean variable for whether you should loan the money that will be set to either True or False. 
    Set up a series of if statements to decide if your decision to loan is "yes" or "no" according to the following rules:
"""
loan_size = int(input("How large is the loan? (1-10) "))
credit_history = int(input("How good is your credit history? (1-10) "))
income = int(input("How high is your income? (1-10) "))
down_payment = int(input("How large is your down payment? (1-10) "))
should_loan = False

if (loan_size >= 5):
    good_credit_and_income = credit_history >= 7 and income >= 7
    good_credit_or_income = credit_history >= 7 or income >= 7
    good_down_payment = down_payment >= 5
    
    should_loan = good_credit_and_income or (good_credit_or_income and good_down_payment)
else:
    if (credit_history < 4):
        should_loan = False
    else:
        good_income_or_down_payment = income >= 7 or down_payment >= 7
        good_income_and_down_payment = income >= 4 and down_payment >= 4
        
        should_loan = good_income_or_down_payment or good_income_and_down_payment
            
if should_loan:
    print("Loan approved.")
else:
    print("Loan denied.")