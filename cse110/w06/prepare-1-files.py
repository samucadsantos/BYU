books = open("books.txt")

with books as names:
    for name in names:
        stripped_name = name.strip()
        print(name)