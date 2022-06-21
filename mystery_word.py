
def play_game():
    already_guessed = []
    print("Let's Begin")
    with open("test-word.txt") as test_word:
        generated_word = test_word.read()
    word_length = len(generated_word)
    print(generated_word)
    underscore = "_"
    word_dash = underscore*word_length
    print(f"Generated Word is: {word_dash}")

    current_guess = input("Guess a letter:")
    if current_guess in already_guessed:
        print("Don't Double Guess!")
    else:
        already_guessed.append(current_guess)
    print(current_guess)
    if current_guess in generated_word:
        print(generated_word)
        reveal_letters(current_guess, generated_word)
    else:
        print("keep goin")

    print(already_guessed)


play_game()


def reveal_letters(current_guess, generated_word):
    for letter in generated_word:
        if current_guess == letter:
            specific_index = generated_word.index(letter)
            print(specific_index)
            print(f"you correctly guessed letter: {letter}")
            # for dash in word_dash:
            """split = word_dash.split()
                print(split[specific_index])
                needs_replacing = split[specific_index].replace(
                    "_", f"{letter}")
                generated_word = needs_replacing.join("")"""
            # print(type(dash))
            # print(word_dash)
            print(generated_word)


if __name__ == "__main__":
    play_game()
