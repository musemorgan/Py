import random #header file needed for random generation

# Generate a random number between 1 and 100
secret = random.randint(1, 100) #a combination of the headerfile along with the value requirement being int 
attempts = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    try:
    # TODO: Get user input (hint: use input() and int())
        guess = int(input("Enter your guess: ")) # input asks for a prompt string so that it can output something
        attempts += 1
    except ValueError: #predefined debugging oppurtunity 
        print("please enter a valid number!")
        continue

    if guess < secret:
        # TODO: Print a hint
        print("This number is too low.")
    elif guess > secret:
        # TODO: Print a hint
        print("This number is too high")
    else:
        # TODO: Print a win message with attempts
        print(f"Congratulations!! You win {attempts} attempts.") #fstring with embedded int 
        break  # exit the loop
    #python terminal: python your_filename.py then python3 your_filename.py
