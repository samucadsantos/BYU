print("Enter a list of numbers, type 0 when finished.")

user_input = -1
numbers = []
numbers_sum = 0
numbers_avarage = 0
numbers_largest = 0
numbers_smallest = 0

while user_input != 0:
    user_input = int(input("Enter a number: "))
    
    if user_input != 0:
        numbers.append(user_input)
        
print()
print(f"The sum is {sum(numbers)}")
print(f"The average is {sum(numbers) / len(numbers) if numbers else 0}")
print(f"The largest number is {max(numbers) if numbers else 0}")
print(f"The smallest number is {min(numbers) if numbers else 0}")
        
# highest = 1
# for number in numbers:
#     if number > highest:
#         highest = number