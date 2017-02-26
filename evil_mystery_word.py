import random
from itertools import groupby

#   got groupby idea from StackOverflow
def get_family(user_input, user_guess):
    word_list = []
    with open("/usr/share/dict/words", "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) == user_input:
                    word_list.append(word)
    families = sorted(([c == user_guess for c in w], i) for i, w in enumerate(word_list))
    result = [[word_list[i] for x, i in g] for k, g in groupby(families, lambda x: x[0])]
    return max(result, key=len)


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
    user_input = int(input("How many letters do you want your word to be? "))
    while count in range(1, 9):
        user_guess = input("Guess a letter: ").lower()
        secret_word = random.choice(get_family(user_input, user_guess)).lower()
        board(secret_word, good_guesses, user_guess)
        print(secret_word)
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
