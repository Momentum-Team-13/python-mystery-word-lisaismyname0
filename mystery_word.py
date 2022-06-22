def start_game():
    with open("test-word.txt") as test_word:
        generated_word = test_word.read()
        list_word = []
        list_word[:0] = generated_word
    word_length = len(list_word)
    underscore = "_"
    word_dash = []
    word_dash[:0] = underscore * word_length
    return list_word, word_dash


def play_game():
    already_guessed = []
    list_word, display_word = start_game()
    print(f"Your word is {display_word}")
    while len(already_guessed) < 8 and "_" in display_word:
        current_guess = input("Guess a letter:")
        print(f"You have {8 -len(already_guessed)} guesses remaining.")
        if current_guess in list_word:
            reveal_letters(current_guess, list_word, display_word)
        else:
            print("Nope! Keep Goin")
            already_guessed.append(current_guess)
            print(already_guessed)


def reveal_letters(current_guess, list_word, display_word):
    for letter in list_word:
        if current_guess == letter:
            specific_index = list_word.index(letter)
            print(specific_index)
            display_word[specific_index] = letter
            print(f"you correctly guessed letter: {letter}")
            print(f"Your word is: {display_word}")


# add while loop to establish conditions of play_game() repeating (user runs out of guesses or user guesses word)
if __name__ == "__main__":
    play_game()
