import functions

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