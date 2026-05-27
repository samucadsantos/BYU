"""
    Author: Samuel dos Santos
    Purpose: Create a story
    Additional notes: I've added a function to get the article of the word and also a dedicated function to print the story
"""
print("Please enter the following:")

adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")

def get_article(word):
    return "an" if word[0] in "aeiou" else "a"

def print_story():
    print("Your story is:")
    print()
    print(
        f"The other day, I was really in trouble. It all started when I saw {get_article(adjective)} {adjective} {animal} {verb1} down the hallway. "
        f"{exclamation.capitalize()}!"
        f" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, "
        f"but not before it tried to {verb3} right in front of my family."
    )

print_story()