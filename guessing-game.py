import random

def play_game():
    print("Welcome to the Guessing Game!")
    print("Choose your difficulty:")
    print("1. Easy (1-5)")
    print("2. Medium (1-10)")
    print("3. Hard (1-25)")
    print("4. Expert (1-50)")
    print("5. Extreme (1-100)")

    difficulty = int(input("Enter your choice (1-5): "))
    ranges = {1: 5, 2: 10, 3: 25, 4: 50, 5: 100}
    max_num = ranges.get(difficulty, 100)

    number = random.randint(1, max_num)
    attempts = 0

    print(f"Guess a number between 1 and {max_num}!")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Computer: Correct! You took {attempts} attempts.")
            break

play_game()
