age = int(input("How old are you? "))

next_age = f"On your next birthday, you will be {age + 1}"

print(next_age)

eggs = int(input("How many egg cartons do you have? "))

computed_eggs = eggs * 12

plural = "s" if computed_eggs > 1 else ""

print(f"You have {computed_eggs} egg{plural}")

cookies = int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))

divide_cookies_by_people = cookies / people
plural = "s" if divide_cookies_by_people > 1 else ""

print(f"Each person may have {divide_cookies_by_people} cookie{plural}")