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
print(r"|_____||____||_____|       |___|___||__|__||__|__||__|__||___,_||_____|\n")

# Functions (Using append mode)
def add_book(book_title, book_author):
    with open(FILE_NAME, "a") as file:
        file.write(f"{book_title} |by| {book_author}\n")
        print("Book has been saved.")

def display_books():
    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.split(" |by| ")
            title = data[0]
            author = data[1]
            print(f"    > {title:<20} | by {author}", end="")

# Main loop
isRun = True
while isRun:
    # Header-option
    print(f"\n<-- {"Options":^15} -->")
    print("[ 1 ] - Add a book.")
    print("[ 2 ] - List all books.")
    print("[ 5 ] - Exit program.")

    user_in = input("\nEnter an option: ")

    try:
        user_choice = int(user_in)

        if user_choice == 1:
            book_title = input("Enter book title: ")
            book_author = input("Enter book author: ")
            add_book(book_title, book_author)
        elif user_choice == 2:
            print("\nAll books listed:\n")
            display_books()
        elif user_choice == 5:
            print("Thanks for using this program..")
            isRun = False
        else:
            print("Invalid option please try again..")
    except ValueError:
        print("Invalid option please try again..")
