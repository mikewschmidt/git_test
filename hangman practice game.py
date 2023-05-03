from random import randrange
word_list = ["Python", "Java", "JavaScript", "PHP",
             "R", "TypeScript", "Go", "Swift", "Cobol"]
word = word_list[randrange(len(word_list))]
word = 'R'
# word = 'EVAPORATE'
print("_ " * len(word))

wrong_ans = 0
guess_list = []


def show_word():
    for letter in word.lower():
        if letter in guess_list:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")


while True:
    if wrong_ans > 6:
        print("You got HANGED!!")
        break
    else:
        guess = input("Please enter a letter: ").lower()
        if len(guess) > 1:
            print("You clearly dont know games")
            continue
        elif guess in guess_list:
            print("You silly goose you already guessed that")
            continue
        elif guess in word.lower():
            guess_list.append(guess)
            show_word()
            if all( in word for guess_list in word):
                print("you win")
            if set(guess_list).union(list(word)):
                print("you win")
        else:
            wrong_ans += 1
            guess_list.append(guess)
            print("You chose wrong buddy. You have {} more guesses".format(
                6 - wrong_ans))
