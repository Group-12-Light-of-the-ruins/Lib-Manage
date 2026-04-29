import os

FILE_NAME = "data.txt"
os.system("clear")

try:
    with open("data.txt", "x") as file:
        file.write("")
except FileExistsError:
    print("Save file detected!")


# Header
print(" _      ____  ____          ___ ___   ____  ____    ____   ____    ___ ")
print("| |    |    ||    \        |   |   | /    ||    \  /    | /    |  /  _]")
print("| |     |  | |  o  ) _____ | _   _ ||  o  ||  _  ||  o  ||   __| /  [_ ")
print("| |___  |  | |     ||     ||  \_/  ||     ||  |  ||     ||  |  ||    _]")
print("|     | |  | |  O  ||_____||   |   ||  _  ||  |  ||  _  ||  |_ ||   [_ ")
print("|     | |  | |     |       |   |   ||  |  ||  |  ||  |  ||     ||     |")
print("|_____||____||_____|       |___|___||__|__||__|__||__|__||___,_||_____|\n")

# Functions (Using append mode)
def add_book(book_title, book_author):
    with open(FILE_NAME, "a") as file:
        file.write(f"{book_title} |by| {book_author}")
        print("Book has been saved.")

isRun = True
while isRun:
    # Header-option
    print("\n<-- Options -->\n")
    print("[ 1 ] - Add a book.")
    print("[ 5 ] - Exit program.")

    user_in = input("\nEnter an option: ")

    try:
        user_choice = int(user_in)

        if user_choice == 1:
            book_title = input("Enter book title: ")
            book_author = input("Enter book author: ")
            add_book(book_title, book_author)
        elif user_choice == 5:
            print("Thanks for using this program..")
            isRun = False
        else:
            print("Invalid option please try again..")
    except ValueError:
        print("Invalid option please try again..")