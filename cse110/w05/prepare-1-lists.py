friends = []

ask = ""

while ask != "end":
    ask = input("Type the name of a friend: ")
    friends.append(ask)
    
print("")

print("Your friends are:")

for friend in friends:
    print(friend)