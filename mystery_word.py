from re import L


def play_game():
    already_guessed = [input()]
    print("Let's Begin")
    with open("test-word.txt") as test_word:
        generated_word = test_word.read()
        i = len(generated_word)
        print(generated_word)

        for letter in generated_word:
            underscore = " _ "
            word_dash = underscore*i
        print(f"Generated Word is: {word_dash}")

        current_guess = input("Guess a letter:")
        if current_guess in already_guessed:
            print("Don't Double Guess!")
        else:
            already_guessed.append(input)
        print(current_guess)
        if current_guess in generated_word:
            def reveal_letters(generated_word):
                for letter in generated_word:
                    if current_guess == letter:
                        specific_index = generated_word.index(letter)
                        print(specific_index)
                        print(f"you correctly guessed letter: {letter}")
                        for dash in word_dash:
                            generated_word = word_dash.replace(
                                "_"[specific_index], f"{letter}")
                        print(word_dash)
                        print(generated_word)
                print(generated_word)
            reveal_letters(generated_word)
        else:
            print("keep goin")
        already_guessed.append(current_guess)
    print(already_guessed)
    play_game()


if __name__ == "__main__":
    play_game()
