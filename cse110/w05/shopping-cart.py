"""
    CSE 110     : Introduction to Programming
    Assignment   : Shopping Cart
    Author       : Samuel dos Santos
    Description  : This program simulates a shopping cart where users can add items, view the cart, remove items, and compute the total price. The program provides a menu-driven interface for user interaction.
    Additional Notes: The program includes input validation to ensure that users enter valid options and prices. 
        The shopping cart is implemented as a list of dictionaries, where each dictionary represents an item with its name and price. 
        The program continues to run until the user chooses to quit.
"""

print("\n------------------------------------------------\n      Welcome to the Shopping Cart Program!      \n------------------------------------------------")

# Initialize an empty shopping cart
cart = []

# Selected menu option
action = None

def cart_content(items = []):
    total_items = len(items)
    
    if total_items == 0:
        print("\n------------------------------------------------\n          The shopping cart is empty.          \n------------------------------------------------")
    else:
        print("\n------------------------------------------------\nThe contents of the shopping cart are:\n------------------------------------------------")
        for i, item in enumerate(items):
            index = i + 1
            print(f"{index}. {item['item']} - ${item['price']:.2f}")
            
def add_items_to_cart(cart = []):
    item = input("What item would you like to add?(Cancel to back to the list.) ")
    
    if item == "Cancel":
        return
    
    validate_price = validate_input(input(f"What is the price of the '{item}'? "), float)
    
    if validate_price is not None:
        cart.append({
            "item": item,
            "price": validate_price
        })
    
        print(f"{item} has been added to the cart.")
    else:
        print("\n------------------------------------------------\n        Invalid price, please try again.        \n------------------------------------------------")
        return
    
def remove_items_from_cart(cart = []):
    # Ask user for the item to remove
    item_to_remove = int(input("\nWhich item would you like to remove? "))
    
    # Convert index to zero-based value
    zero_based_index = item_to_remove - 1      
    
    # Check if index is valid against the cart content
    if zero_based_index in range(len(cart)):
        removed_item = cart.pop(zero_based_index)
        print(f"{removed_item['item']} has been removed from the cart.")
        
        # Display the cart content updated
        cart_content(cart)
    else:
        print("\n------------------------------------------------\n        Invalid item number, please try again.        \n------------------------------------------------")
    
def initial_menu():
    print("\nPlease select one of the following: ")
    print("\n1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
def validate_input(input: str, type = int):
    while True:
        try:
            return type(input)
        except ValueError:
            initial_menu()
            return None

# Show the menu options
while action != 5:
    # Show the menu options 
    initial_menu()
    
    # Ask the user to select a menu option
    validate = validate_input(input("\nPlease enter an action: "))
    
    if validate in range(1, 6):
        action = validate
    
    if (action == 1):
        # Add items to the cart
        add_items_to_cart(cart)
    elif(action == 2):
        # Display the cart content
        cart_content(cart)
    elif(action == 3):
        # Display the cart content
        cart_content(cart)
        
        # Remove items from the cart
        remove_items_from_cart(cart)
    elif(action == 4):
        print(f"\nThe total price of the items in the shopping cart is ${sum(item['price'] for item in cart):.2f}")
    elif(action == 5):
        print("Thank you. Goodbye.")
    else:
        print("\n------------------------------------------------\n        Invalid option, please try again.        \n------------------------------------------------")