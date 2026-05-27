"""
Author: Samuel dos Santos
Purpose: Create an ID card
"""

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
email = input("What is your email address? ")
phone_number = input("What is your phone number? ")
job_title = input("What is your job title? ")
id_number = input("What is your ID number? ")

print("The ID Card is:")
print("----------------------------------------")
print(f"{last_name.upper()}, {first_name}")
print(f"{job_title.title()}")
print(f"ID: {id_number}")
print()
print(f"Email: {email.lower()}")
print(f"{phone_number}")
print("----------------------------------------")