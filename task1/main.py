from wsgiref.validate import validator
import functions


def input_file():
    # Open Files
    writable_file = functions.openFile("a")
    readable_file = functions.openFile("r")

    # Take our three inputs.
    name = input("Enter a name: ")
    age = input("Enter this persons age: ")
    color = input("Enter this person's favourite color: ")

    # Get ID by getting line count and adding one.
    lineID = functions.getLineCount() + 1

    # Write to file.
    writable_file.write(f"{lineID} - {name} - {age} - {color}\n")

    # User message, written to file, then close files.
    print("Written to file!")
    writable_file.close()
    readable_file.close()


def search_file():
    # Open array
    searched_lines = []

    # Input for search
    search_term = input("Enter Search Term: ")

    # Get all lines in file
    lines = functions.getLines()

    # Search array
    for line in lines:
        if search_term.lower() in line.lower():
            searched_lines.append(line)

    # Output
    if not searched_lines:
        print("Search Term Returned Nothing. Sorry!")
    else:
        for line in searched_lines:
            print(line)


action = input("Enter action ")
if action == "input":
    input_file()
elif action == "search":
    search_file()