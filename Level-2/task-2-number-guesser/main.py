import random
#function to start the number guesser game
def number_guesser():
    #get a valid range from the user
    while True:
        try:
            min_num = int(input("Enter minimum number: "))
            max_num = int(input("Enter maximum number: "))
        except ValueError:
            print("Please enter a valid integer number.")
            continue

        if max_num <= min_num:
            print("Maximum number must be greater than minimum number.")
            continue
        break

    #generate a random number within the given range
    number = random.randint(min_num, max_num)
    #count valid attempts
    attempts = 0

    #keep asking untill the correct number is guessed
    while True:
        try:
            guess = int(input(f"Guess a number between {min_num} and {max_num}: "))
        except ValueError:
            print(f"Please enter a valid number between {min_num} and {max_num}.")
            continue

        if guess < min_num or guess > max_num:
            print(f"Please enter a number between {min_num} and {max_num}.")
            continue

        attempts += 1

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("=" * 35)
            print(f"Congratulations!\nYou guessed the correct number: {number}\nYou found it in {attempts} attempts.")
            print("=" * 35)
            break

if __name__ == "__main__":
    number_guesser()