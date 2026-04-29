
FILE_NAME = "data.txt"

try:
    with open("data.txt", "x") as file:
        file.write("")
except FileExistsError:
    print("Save file detected!")
