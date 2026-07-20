#function to generate fibonacci sequence
def fibonacci_sequence():
    #get a valid positive integer from the user
    while True:
        try:
            n = int(input("Enter an integer number: "))
        except ValueError:
            print("Please enter a valid integer number.")
            continue
        if n <= 0:
            print("Please enter a positive integer.")
            continue
        break

    #first two fibonacci numbers
    a = 0
    b = 1

    #display fibonacci sequence
    print("\nFibonacci Sequence:")
    for i in range(n):
        print(f"{a}", end=" ")
        c = a + b
        a = b
        b = c
    print()


if __name__ == "__main__":
    fibonacci_sequence()
