def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0

    for key in questions:
        print("-------------------------------------")
        print(key)

        for i in options[question_num]:
            print(i)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)

        correct_guesses += check(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)
    play_again()

# -------------------------------------


def check(answer, guess):
    if answer == guess:
        print("CORRECT!!")
        return 1
    else:
        print("WRONG!!")
        return 0
# -------------------------------------


def display_score(correct_guesses, guesses):
    print()
    print("-------------------------------------")
    print("RESULTS")
    print("-------------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    print("Your final score is "+str(int((correct_guesses/len(questions))*100))+"%")
    if correct_guesses == 4:
        print("ALL CORRECT. WELL DONE!!!!")
    elif correct_guesses == 0:
        print("you dumb.")
    else:
        print("Nice!")

    print("-------------------------------------")
# -------------------------------------


def play_again():
    response = input("Do you want to play again? (yes/no): ").lower()
    if response == "no":
        print("Thanks for playing!!")
    elif response == "yes":
        print("Playing again!!")
        new_game()
    else:
        print("Unknown response, quitting the game. \nThanks for playing!!")
    print("-------------------------------------")
    print("\n\n")

# -------------------------------------


questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]
]

new_game()
