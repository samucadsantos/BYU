"""
    Author: Samuel dos Santos
    Date: 2024-06-10
    Description: This program calculates the volume of a tire based on user input for width, aspect ratio, and wheel diameter.
        It also prompts the user to subscribe for pricing information and saves the results
    Additionally, it saves the calculation results and user information to a text file for future reference.
    and if user wants to subscribe, it will ask for their name and email address and save that information as well.
"""
import math
from datetime import datetime

tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

def total_volume(width, aspect, diameter):
    # Calculate the volume of the tire using the formula
    volume = (math.pi * width ** 2 * aspect * (width * aspect + 2540 * diameter)) / 10000000000
    return volume

def validate_name_email(name, email):
    if name != '':
        name = name.strip()
    if email != '':
        email = email.strip()
        
    if name != '' and email != '':
        return f", {name}, {email}"
    elif name != '' and email == '':
        return f", {name}"
    elif name == '' and email != '':
        return f", {email}"
    else:
        return ""

def prepare_output(width, aspect, diameter, volume, name, email):
    if name != '':
        name = name.strip()
    if email != '':
        email = email.strip()
        
    name_email = validate_name_email(name, email)
    
    # Prepare the output string with the tire specifications
    return f"{current_day.strftime('%Y-%m-%d')}, {width}, {aspect}, {diameter}, {volume:.2f}{name_email}\n"

total_volume = total_volume(tire_width, aspect_ratio, wheel_diameter);

print(f"The approximate volume is {total_volume:.2f} liters")

current_day = datetime.now()

want_subscribe = ''

while want_subscribe not in ['yes', 'no']:
    want_subscribe = input("Would you like to receive pricing information? (yes/no): ").strip().lower()
    
    if want_subscribe not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")

with open("volumes.txt", "at") as file:    
    user_name = ''
    user_email = ''
    
    if want_subscribe == 'yes':      
        while user_name == '':
            user_name = input("Please enter your name: ").strip()
            if user_name == '':
                print("Name cannot be empty. Please enter your name.")
        
        while user_email == '':
            user_email = input("Please enter your email address: ").strip()
            if user_email == '':
                print("Email cannot be empty. Please enter your email address.")
                
    file.write(prepare_output(tire_width, aspect_ratio, wheel_diameter, total_volume, user_name, user_email))
