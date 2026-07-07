def display_regular(message):
    return message
    
def display_uppercase(message):
    return message.upper()
    
def display_lowercase(message):
    return message.lower()

message = input("What is your message? ")
    
print(f"{display_regular(message)}")
print(f"{display_uppercase(message)}")
print(f"{display_lowercase(message)}")