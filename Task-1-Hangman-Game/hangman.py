import random

words = ["python", "ready", "intern", "india", "happy"]

word = random.choice(words)

guessed_word = ["_"] * len(word)

attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("Wrong guess!")

if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)