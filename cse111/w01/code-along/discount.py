"""
Work along with your instructor to write a Python program 
that gets a customer’s subtotal as input and gets the current
day of the week from your computer’s operating system. Your 
program must not ask the user to enter the day of the week. 
Instead, it must get the day of the week from your computer’s 
operating system.

If the subtotal is $50 or greater and today is Tuesday or 
Wednesday, your program must subtract 10% from the subtotal. 
Your program must then compute the total amount due by adding 
sales tax of 6% to the subtotal. Your program must print the
discount amount if applicable, the sales tax amount, and the
total amount due.
"""
from datetime import datetime

# The discount rate is 10% and the sales tax rate is 6%.
DISCOUNT_RATE = 0.10
TAX_RATE = 0.06

subtotal = 0

print("Enter the price and quantity for each item.")
price = 1

while price != 0:
    # Get the price from the user.
    price = float(input("Please enter the price: "))  
    
    if price != 0:
         # Get the quantity from the user.
        quantity = int(input("Please enter the quantity: "))
        subtotal += price * quantity
        
    # Print a blank line.
    print()
    
# Round the subtotal to two digits after
# the decimal and print the subtotal.
subtotal = round(subtotal, 2)
print(f"Subtotal: ${subtotal:.2f}")
print()

current_day = datetime.now().strftime("%A")
discount_weekdays = ["Tuesday", "Wednesday", "Friday"]

discount = 0.0
how_much_to_discount = 0.0

# Only apply discount if subtotal is $50 or greater and today is Tuesday or Wednesday
if current_day in discount_weekdays:
    if subtotal < 50:
        lacking = round(50 - subtotal, 2)
        print("To receive the discount, add"
                f" {lacking:.2f} to your order.")
    else:
        discount = round(subtotal * DISCOUNT_RATE, 2)
        print(f"Discount amount: ${discount:.2f}")
        subtotal -= discount

# Compute the sales tax. Notice that we compute the sales tax
# after computing the discount because the customer does not
# pay sales tax on the full price but on the discounted price.
sales_tax = round(subtotal * TAX_RATE, 2)
print(f"Sales tax amount: ${sales_tax:.2f}")

# Compute the total by adding the subtotal and the sales tax.
total = subtotal + sales_tax

# Display the total for the user to see.
print(f"Total: {total:.2f}")