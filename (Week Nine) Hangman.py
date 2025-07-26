import random

# word guesses
word_list = ["Sonic", "Mario", "Weaver", "Silverhand", "Cloud", "Aerith", "Difficult"]
word_to_guess = random.choice(word_list).lower()

# progress tracking variables
guessed_letters = []
tries = 6
display_word = ["_"] * len(word_to_guess)

print("Welcome to Hanging Men!")

while tries > 0 and "_" in display_word:
    print("\nWord: " + " ".join(display_word))
    print(f"Tries left: {tries}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print(f"Good job. '{guess}' is in the word.")
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[i] = guess
    else:
        print(f"Nope, '{guess}' is not in the word.")
        tries -= 1

# Game Over You survived 2 rounds
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word_to_guess)
else:
    print("\nYou messed up. The word was:", word_to_guess)
