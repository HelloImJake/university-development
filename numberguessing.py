import random
from pprint import pprint
user_guesses = []

# Generate random number, give a little message to the user.
print("Welcome to the random number game! Generating number... ")
random_number = random.randint(0, 9)

# Make while loop
guesses = 1
while guesses <= 10:

    # Ask for user input
    print("\nGuess #" + str(guesses))
    user_input = int(input("Enter a number: "))
    user_guesses.append(user_input)

    # If the user is correct, end loop and give success message
    if user_input == random_number:
        print(f"You beat the game! Congrats! It took you {guesses} guesses.")
        print(f"Your guesses were: {user_guesses}")
        break
    # If the guess is higher
    elif user_input > random_number:
        pprint(f"Your guess ({user_input}) is higher than the number!")
    # If the guess is lower
    else:
        print(f"Your guess ({user_input}) is lower than the number!")
    guesses = guesses + 1
    