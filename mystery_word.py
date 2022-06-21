with open("test-word.txt") as test_word:
    generated_word = test_word.read()
    list_word = []
    list_word[:0] = generated_word


def start_game():
    word_length = len(list_word)
    underscore = "_"
    word_dash = []
    word_dash[:0] = underscore * word_length
    print(f"Generated Word is: {underscore*word_length}")


def play_game():
    start_game()
    already_guessed = []
    current_guess = input("Guess a letter:")
    if current_guess in list_word:
        reveal_letters(current_guess, list_word)
    else:
        print("Nope! Keep Goin")

    if current_guess in already_guessed:
        print("No Double Guesses!")
    else:
        already_guessed.append(current_guess)
    print(already_guessed)


def reveal_letters(current_guess, word_dash):
    print(word_dash)
    for letter in list_word:
        if current_guess == letter:
            print(f"you correctly guessed letter: {letter}")
            specific_index = word_dash.index(letter)
            print(specific_index)
            word_dash[specific_index].replace("_", letter)
    print(f"this is {word_dash}")


# add while loop to establish conditions of play_game() repeating (user runs out of guesses or user guesses word)
if __name__ == "__main__":
    play_game()
