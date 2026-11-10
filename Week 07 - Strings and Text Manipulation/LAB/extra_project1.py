import random

word_list = ["apple", "banana", "computer", "python", "developer"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

placeholder = "_" * word_length
print(f"Word to guess: {placeholder}")

lives = 6
game_over = False
correct_letters = []
guessed_letters = []

while not game_over:
    print(f"\n--------------------------------------------")
    print(f"Lives remaining: {lives}/6")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue
        
    guessed_letters.append(guess)

    display = ""

    if guess in chosen_word:
        print(f"Good job! '{guess}' is in the word.")
        correct_letters.append(guess)
    else:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")

    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"Word: {display}")

    if "_" not in display:
        game_over = True
        print(" You win!")

    if lives == 0:
        game_over = True
        print(f" Game over! The word was '{chosen_word}'.")