# ask the user for the grade
grade = float(input("What is the grade percent? "))

# figure out the letter grade
if grade >= 90:
    letter_grade = "A"
elif grade >= 80:
    letter_grade = "B"
elif grade >= 70:
    letter_grade = "C"
elif grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
    
# add a plus or minus if the grade is not an A or F
if letter_grade not in ["A", "F"]:
    if grade % 10 >= 7:
        letter_grade += "+"
    elif grade % 10 <= 3:
        letter_grade += "-"

# display the letter grade to the user
print(f"The letter grade is: {letter_grade}")