import functions

# Open array
searched_lines = []

# Input for search
search_term = input("Enter Search Term: ")

# Get all lines in file
lines = functions.getLines()

# Search array
for line in lines:
    if search_term in line:
        searched_lines.append(line)

# Output
if not searched_lines:
    print("Search Term Returned Nothing. Sorry!")
else:
    for line in searched_lines:
        print(line)