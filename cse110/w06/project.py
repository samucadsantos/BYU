"""
    Author: Samuel dos Santos
    Purpose: Write a Python program to analyze it to answer the following questions:
        - What is the year and country that has the lowest life expectancy in the dataset?
        - What is the year and country that has the highest life expectancy in the dataset?
        - Allow the user to type in a year, then, find the average life expectancy for that year.
            Then find the country with the minimum and the one with the maximum life expectancies for that year.
    Additional: I've added validation to the selected year input and a conditional render for that information because some years do not have enouth information to be shown
"""

from datetime import datetime

validate_year = False
selected_year = None

while validate_year == False:
    try:
        selected_year = int(input("Enter the year of interest: "))
        current_year = datetime.now().year
    
        if selected_year > current_year:
            validate_year = False
            print("Year cannot be in the future.")
        else:
            validate_year = True
    except ValueError:
        print("Please enter a valid four-digit year (e.g., 1955)")
    
rows_in_selected_year = []

global_min_life = 999999
global_min_country = ""
global_min_year = None

global_max_life = -1
global_max_country = ""
global_max_year = None

with open("life-expectancy.csv") as file:
    next(file)
    
    for line in file:
        clean_line = line.strip()
        parts = clean_line.split(",")
        
        country = parts[0]
        year = int(parts[2])
        expectancy = float(parts[3])
        
        if year == selected_year:
            rows_in_selected_year.append(line)
        
        if expectancy < global_min_life:
            global_min_life = expectancy
            global_min_country = country
            global_min_year = year
            
        if expectancy > global_max_life:
            global_max_life = expectancy
            global_max_country = country
            global_max_year = year
                
print(f"\nThe overall max life expectancy is: {global_max_life} from {global_max_country} in {global_max_year}")
print(f"The overall min life expectancy is: {global_min_life} from {global_min_country} in {global_min_year}")

sum_expectancy = 0

year_min_life = 999999
year_min_country = ""

year_max_life = -1
year_max_country = ""

for row in rows_in_selected_year:
    clean_row = row.strip()
    parts = clean_row.split(",")
    
    country = parts[0]
    expectancy = float(parts[3])
    
    sum_expectancy += expectancy
    
    if expectancy < year_min_life:
        year_min_life = expectancy
        year_min_country = country
        
    if expectancy > year_max_life:
        year_max_life = expectancy
        year_max_country = country
        
len_rows = len(rows_in_selected_year)
cal_average = 0

if len_rows > 0:
    cal_average = sum_expectancy / len_rows

if cal_average > 0:
    print(f"\nFor the year {selected_year}:")
    print(f"The average life expectancy across all countries was {cal_average:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max_life:.2f}")
    print(f"The min life expectancy was in {year_min_country} with {year_min_life:.2f}")
