import random

# List of 5 predefined words
words = ["python", "apple", "school", "computer", "hangman"]

# Select a random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Display hidden word
display_word = ["_"] * len(word)

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_guesses and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")

        # Update display word
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# Game result
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)