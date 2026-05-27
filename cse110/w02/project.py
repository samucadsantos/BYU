"""
    Author: Samuel dos Santos
    Purpose: A program to calculate the total cost of a meal, including sales tax, and determine the change to be given back to the customer after payment.
    Additional: Use loop to ensure that the payment amount is sufficient to cover the total cost of the meal. If the payment amount is insufficient, prompt the user to enter a new payment amount until a sufficient amount is provided.
        also include a function to calculate the change to be given back to the customer after payment, and use it in the loop to determine the change after a sufficient payment amount is entered.
        
    Prompt example:
        What is the price of a child's meal?10
        What is the price of an adult's meal? 20
        How many children are there? 1
        How many adults are there? 1
        Subtotal: $30.00

        What is the sales tax rate? 10
        Sales tax: $3.00
        Total: $33.00

        What is the payment amount? 40
        Change: $7.00
"""
child_meal_price = float(input("What is the price of a child's meal?"))
adult_meal_price = float(input("What is the price of an adult's meal? "))
how_many_children = int(input("How many children are there? "))
how_many_adults = int(input("How many adults are there? "))

def calculate_change(payment_amount, total):
    if payment_amount < total:
        print(f"The payment amount is insufficient. The total is ${total:.2f}.")
        return None
    else:
        return payment_amount - total

subtotal = (child_meal_price * how_many_children) + (adult_meal_price * how_many_adults)

print(f"Subtotal: ${subtotal:.2f}")
print()

sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax_percentage = subtotal * (sales_tax_rate / 100)
total = subtotal + sales_tax_percentage

print(f"Sales tax: ${sales_tax_percentage:.2f}")
print(f"Total: ${total:.2f}")
print()

while True:
    payment_amount = float(input("What is the payment amount? "))
    
    change = calculate_change(payment_amount, total)

    if change is not None:
        print(f"Change: ${change:.2f}")
        break

