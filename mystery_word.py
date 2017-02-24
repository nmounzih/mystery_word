import random


def get_range(user_input):
    if user_input == "e":
        len_range = 4, 6
    elif user_input == "m":
        len_range = 6, 8
    elif user_input == "h":
        len_range = 8, 46
    return len_range


def get_word(user_input):
    word_list = []
    secret_range = get_range(user_input)
    with open("/usr/share/dict/words", "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) in range(secret_range[0], secret_range[1]):
                    word_list.append(word)
    computer_choice = random.choice(word_list)
    return computer_choice.lower()


def board(secret_word, good_guesses, user_guess):
    for letter in secret_word:
        if letter in good_guesses or letter == user_guess:
            print(letter, end='')
        else:
            print('_ ', end='')
    print('')


def guessed_all(secret_word, good_guesses):
    if sorted(set(list(secret_word))) == sorted(good_guesses):
        return True


def main():
    count = 1
    guesses_left = 8
    good_guesses = []
    bad_guesses = []
    user_input = input("[E]asy, [M]edium, or [H]ard? ").lower()
    secret_word = get_word(user_input)
    print("My word has {} letters in it.".format(len(secret_word)))
    while count in range(1, 9):
        user_guess = input("Guess a letter: ").lower()
        board(secret_word, good_guesses, user_guess)
        if len(user_guess) > 1 or user_guess == "":
            print("Invalid guess. Try again.")
        else:
            if user_guess in good_guesses or user_guess in bad_guesses:
                print("Already guessed that!")
            elif user_guess in secret_word:
                print("Good one!")
                print("You have {} guesses left.".format(guesses_left))
                good_guesses.append(user_guess)
                if guessed_all(secret_word, good_guesses):
                    print("You won!")
                    break
            elif user_guess not in secret_word:
                print("Nope!")
                bad_guesses.append(user_guess)
                count += 1
                guesses_left -= 1
                print("You have {} guesses left.".format(guesses_left))
    else:
        print("You lose! The secret word was {}.".format(secret_word.upper()))
    play_again = input("Play again? Y/n ")
    if play_again == 'y'.lower():
        main()



if __name__ == '__main__':
    main()
