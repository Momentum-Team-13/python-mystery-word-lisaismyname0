def play_game():
    print("Let's Begin")
    with open("test-word.txt") as test_word:
        guess = test_word.read()
        print(guess)
        for letter in guess:
            print(letter)

        def show_guess_length():
            for letter in guess:
                i = len(guess)
            print("_"*i)
        show_guess_length()


if __name__ == "__main__":
    play_game()
