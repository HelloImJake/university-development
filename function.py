# Define function
def super_looper(n, l):
    for x in l:
        if x > n:
            print(x)

def stupid_function(n, l):
    return l[n]

# List 2 is the one to check, list one is the numbers to loop
def printList(l1, l2):
    for x in l1:
        if len(l2) <= x:
            print(f"Unable to retrieve {x}, out of bounds.")
        else:
            print(l2[x])

# Define Lists
myList = [1, 3, 5, 7]
mySecondList = [2, 4, 6, 8]

# Super looper function
super_looper(6, myList)

# Dynamic search through function
n = 3
print(f"Item number {3} in myList is: {stupid_function(n, myList)}")

# Weird task 3
print("\nSearching variable: mySecondList.")
printList(myList, mySecondList)

print("\nSearching variable:  myList.")
printList(mySecondList, myList)