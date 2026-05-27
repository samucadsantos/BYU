"""
    Author: Samuel dos Santos
    Purpose: This program prompts the user to enter their level of experience (JUNIOR, PLENO, SENIOR) and provides feedback based on their input. 
        It also asks for additional information such as years of experience, whether they have been mentored or lead projects, and provides further guidance based on their responses.
    Additional: The program includes input validation to ensure that the user enters valid options and handles invalid inputs gracefully.
        It also encourages users to seek mentorship and leadership opportunities to further develop their skills and contribute to the growth of the community.
"""
OPTIONS = {
    "JUNIOR",
    "PLENO",
    "SENIOR",   
}

user_input = input("Please enter your level of experience (JUNIOR, PLENO, SENIOR): ").upper()

def validate_input(user_input):
    if user_input in OPTIONS:
        return True
    else:
        return False
    
def get_years_of_experience():
    while True:
        try:
            years_of_experience = int(input("Please enter your years of experience in months: "))
            return years_of_experience
        except ValueError:
            print("Invalid input. Please enter a valid number for years of experience.")
            
def print_message(message):
    print(message)

# should have  at least three level of answers
if validate_input(user_input):
    if user_input == "JUNIOR":
        years_of_experience = get_years_of_experience()
        
        if years_of_experience <= 6:
            print_message("You need to find a mentor to guide you through your early career.")
            
            already_mentored = input("Have you already been mentored? (yes/no): ").lower()  
            
            while already_mentored not in ["yes", "no"]:
                already_mentored = input("Invalid input. Please enter 'yes' or 'no': ").lower()
            
            if already_mentored == "yes":
                print_message("That's great! Keep learning and growing.")
            else:
                print_message("Consider finding a mentor to help you develop your skills and navigate your career path.")
        elif years_of_experience > 6 and years_of_experience <= 24:
             print_message("You are on the right track. Keep gaining experience and learning new skills.")
        else:
             print_message("You have a good amount of experience. Consider taking on more challenging projects to further develop your skills.")
    elif user_input == "PLENO":
        print_message("You are a PLENO developer. Keep honing your skills and consider taking on leadership roles in projects.")
        
        do_you_lead = input("Do you currently lead any projects? (yes/no): ").lower()
        
        while do_you_lead not in ["yes", "no"]:
            do_you_lead = input("Invalid input. Please enter 'yes' or 'no': ").lower()
            
        if do_you_lead == "yes":
            print_message("That's fantastic! Leading projects is a great way to develop your leadership skills and gain valuable experience.")
            
            how_many_projects = int(input("How many projects do you currently lead? "))
            
            if how_many_projects >= 2:
                print_message("Impressive! Leading multiple projects is a great way to further develop your skills and gain valuable experience.")
            else:
                print_message("Consider taking on more leadership roles in projects to further develop your skills and gain valuable experience.")
        else:
            print_message("Consider taking on leadership roles in projects to further develop your skills and gain valuable experience.")
    elif user_input == "SENIOR":
        print_message("You are a SENIOR developer. Keep up the great work and consider mentoring junior developers to help them grow.")
        
        do_you_mentor = input("Do you currently mentor any junior developers? (yes/no): ").lower()
        
        while do_you_mentor not in ["yes", "no"]:
            do_you_mentor = input("Invalid input. Please enter 'yes' or 'no': ").lower()
            
        if do_you_mentor == "yes":
            print_message("That's wonderful! Mentoring junior developers is a great way to give back to the community and help others grow.")
            
            how_many_mentees = int(input("How many junior developers do you currently mentor? "))
            
            if how_many_mentees >= 2:
                print_message("Impressive! Mentoring multiple junior developers is a great way to make a significant impact on their careers and the industry as a whole.")
            else:
                print_message("Consider mentoring more junior developers to further contribute to the growth of the community and help others succeed.")
        else:
            print_message("Consider mentoring junior developers to further contribute to the growth of the community and help others succeed.")     
else:
    Error_message = "Invalid input. Please enter one of the following options: JUNIOR, PLENO, SENIOR."
    print_message(Error_message)
