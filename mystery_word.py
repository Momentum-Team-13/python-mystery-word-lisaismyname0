import random


def pick_a_word(file):
    word_bank = open(file, "r")
    random_word = random.choice(word_bank.read().split())
    word_bank.close()
    return random_word


def start_game():
    print("Let's play a word guessing game.")
    generated_word = pick_a_word("words.txt")
    list_word = []
    word_dash = []
    underscore = "_"
    for letter in generated_word:
        list_word.append(letter)
        word_dash.append(underscore)
    return list_word, word_dash


def play_game():
    already_guessed = []
    list_word, display_word = start_game()
    while len(already_guessed) < 9 and "_" in display_word:
        print("Your computer generated word is: " + " ".join(display_word))
        current_guess = input("Guess a letter: ").lower()
        print(f"You have {8 -len(already_guessed)} guesses remaining.")

        if len(current_guess) > 1:
            print("Only one letter at a time!")
        if current_guess.isnumeric():
            print("No numbers in this game!")
        elif current_guess in list_word:
            reveal_letters(current_guess, list_word, display_word)
        elif current_guess in already_guessed:
            print("You already guessed that letter!")
        else:
            already_guessed.append(current_guess)
            print("Sorry, that goes in the wrong letter bank: " +
                  " ".join(already_guessed))
    if len(already_guessed) == 9:
        print("Sorry, you ran out of guesses :(")
        print("Your word was: " + "".join(list_word))
    elif "_" not in display_word:
        print("You correctly guessed" + "".join(list_word) +
              " and won Wheel of Fortune!")


def reveal_letters(current_guess, list_word, display_word):
    for index, letter in enumerate(list_word):
        if letter == current_guess:
            display_word[index] = current_guess
    print(f"Good job! {current_guess} is in the mystery word!")


if __name__ == "__main__":
    play_game()
