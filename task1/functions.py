data_store = "data.txt"

# Open our data file
def openFile(operation):
    f = open(data_store, operation)
    return f

# Line Count of our data file.
def getLineCount():
    f = openFile("r")
    lines = f.readlines()
    lineCount = len(lines)
    f.close()
    return lineCount

# Get array of lines in file
def getLines():
    lines = []
    f = openFile("r")
    for line in f:
        lines.append(line.strip())
    return lines