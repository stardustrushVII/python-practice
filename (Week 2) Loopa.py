import random

def guessing_game():
    sec_num = random.randint(1, 100)
    print(f"(Debug) The secret number is: {sec_num}")
    attempts = 0
    previous_guess = None

    print("Guess the secret number between 1 and 100 and get out the crazy place!")

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        # attempt count if new guess
        if guess != previous_guess:
            attempts += 1
        previous_guess = guess

        if guess < sec_num:
            print("Too low!")
        elif guess > sec_num:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} tries! Now you're free to enjoy dying 24/7 in Monster Hunter!")
            break

guessing_game()
