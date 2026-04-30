import os

FILE_NAME = "data.txt"
os.system("clear")

try:
    with open("data.txt", "x") as file:
        file.write("")
except FileExistsError:
    print("Save file detected!")


# Header
print(r" _      ____  ____          ___ ___   ____  ____    ____   ____    ___ ")
print(r"| |    |    ||    \        |   |   | /    ||    \  /    | /    |  /  _]")
print(r"| |     |  | |  o  ) _____ | _   _ ||  o  ||  _  ||  o  ||   __| /  [_ ")
print(r"| |___  |  | |     ||     ||  \_/  ||     ||  |  ||     ||  |  ||    _]")
print(r"|     | |  | |  O  ||_____||   |   ||  _  ||  |  ||  _  ||  |_ ||   [_ ")
print(r"|     | |  | |     |       |   |   ||  |  ||  |  ||  |  ||     ||     |")
print(r"|_____||____||_____|       |___|___||__|__||__|__||__|__||___,_||_____|")

# Functions (Using append mode)
def add_book(book_title, book_author):
    with open(FILE_NAME, "a") as file:
        file.write(f"{book_title} |by| {book_author}\n")
        print("Book has been saved.")

def display_books():
    with open(FILE_NAME, "r") as file:
        print("\nAll books listed:\n")
        count = 0
        
        file.seek(0)
        for id,line in enumerate(file):
            if line.strip() == "":
                continue

            data = line.split(" |by| ")

            if len(data) != 2:
                continue

            title = data[0]
            author = data[1]
            print(f" [{id}] > {title:<20} | by {author}", end="")
            count += 1
        
        if count <= 0:
            print("-----> Empty list (Add some books!) --?")

def update_book(book_index):
    new_data = []
    prev_book_name = ""

    try:
        # Read the data then store to new_data list
        with open(FILE_NAME, "r") as file:
            new_data = file.readlines()
            temp_data = new_data[book_index].split(" |by| ")
            prev_book_name = temp_data[0]

            book_title = input("Enter new book title: ")
            book_author = input("Enter new book author: ")

            if book_title != "":
                temp_data[0] = book_title

            if book_author != "":
                temp_data[1] = book_author

            new_data[book_index] = " |by| ".join(temp_data) + "\n"

        # Write new_data list
        with open(FILE_NAME, "w") as file:
            file.writelines(new_data)
        
        print(f"Book '{prev_book_name}' has been updated!")
    except IndexError:
        print("Index not found.")

def delete_book(key_id):
    new_data = []
    book_data = []

    # Read the data then store to new_data list
    with open(FILE_NAME, "r") as file:
        for id,line in enumerate(file):
            if id != key_id:
                new_data.append(line)
            else:
                book_data = line.split(" |by| ")

    # Write new_data list
    with open(FILE_NAME, "w") as file:
        for line in new_data:
            file.write(line)
    
    if len(book_data) > 0:
        print(f"Book '{book_data[0]}' has been deleted!")
    else:
        print("Index not found.")

def search_book(key_string):
    with open(FILE_NAME, "r") as file:
        print("\nSearch results:\n")

        for id,line in enumerate(file):
            data = line.split(" |by| ")
            title = data[0]
            author = data[1]

            if (key_string.lower() in title.lower()) or (key_string.lower() in author.lower()):
                print(f" [{id}] > {title:<20} | by {author}", end="")

# Main loop
isRun = True
while isRun:
    # Header-option
    print(f"\n<-- {"Options":^15} -->")
    print("[ 1 ] - Add a book.")
    print("[ 2 ] - List all books.")
    print("[ 3 ] - Update book data.")
    print("[ 4 ] - Delete book.")
    print("[ 5 ] - Search a book.")
    print("[ 6 ] - Exit program.")

    user_in = input("\nEnter an option: ")

    try:
        user_choice = int(user_in)

        if user_choice == 1:
            book_title = input("Enter book title: ")
            book_author = input("Enter book author: ")
            add_book(book_title, book_author)
        elif user_choice == 2:
            display_books()
        elif user_choice == 3:
            key_id = input("Enter index for book to update: ")
            key_int = int(key_id)
            update_book(key_int)
        elif user_choice == 4:
            key_id = input("Enter index for book to delete: ")
            key_int = int(key_id)
            delete_book(key_int)
        elif user_choice == 5:
            key_str = input("Enter name or author of book: ")
            search_book(key_str)
        elif user_choice == 6:
            print("Thanks for using this program..")
            isRun = False
        else:
            print("Invalid option please try again..")
    except ValueError:
        print("Invalid option please try again..")
