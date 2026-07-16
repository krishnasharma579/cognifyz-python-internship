import random 

#function to start the guessing game
def guessing_game():
    #generate a random number between 1 and 100
    number = random.randint(1, 100)
    #count the number of valid attempts
    attempts = 0

    #keep asking until the correct number is guessed
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid integer number between 1 and 100.")
            continue

        #verify the user input is within the valid range
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        #compare both numbers display hint and result
        if guess > number:
            print("Too High.")
        elif guess < number:
            print("Too Low.")
        else:
            print("=" * 35)
            print(f"Congratulations!\nYou guessed the correct number: {number}\nYou found it in {attempts} attempts.")
            print("=" * 35)
            break

if __name__ == "__main__":
    guessing_game() 