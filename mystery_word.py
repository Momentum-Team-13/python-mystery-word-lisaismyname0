def play_game():
    print("Let's Begin")
    with open("test-word.txt") as test_word:
        generated_word = test_word.read()
        print(generated_word)

        for letter in generated_word:
            i = len(generated_word)
            underscore = "_"
            word_dash = underscore*i
        print(f"Generated Word is: {word_dash}")

        current_guess = input("Guess a letter:")
        print(current_guess)
        if current_guess in generated_word:
            def reveal_letters(generated_word):
                for letter in generated_word:
                    if current_guess == letter:
                        print(f"you correctly guessed letter: {letter}")
                    for dash in word_dash:
                        if current_guess == letter:
                            generated_word = word_dash.replace(
                                "_", f"{letter}")
                print(generated_word)
            reveal_letters(generated_word)
        else:
            print("keep goin")


"""            def reveal_letters():
                for letter in guess:
                    if current_guess in word_dash:
                        guess = word_dash.replace("_", f"{letter}")
                        print(guess)
            reveal_letters()"""


if __name__ == "__main__":
    play_game()
