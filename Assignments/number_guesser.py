import random

low = 1
high = 50


def choose_random_number(l, h):
    return random.randint(l, h)


def restart():
    user_input = str(input("Press r to restart the game and other key to exit: "))
    if user_input == 'r':
        play_game()

def get_user_input():
    valid = False
    while not valid:
        try:
            user_input = int(input("Please enter a number between 1 to 50: "))
            if 50 >= user_input >= 1:
                return user_input
            else:
                print("The Number must be between 1 to 50!")
        except ValueError:
            print("Please only input digits")


def play_game():
    print("\n\nGuess the Number!")
    correct_answer = choose_random_number(low, high)
    print(correct_answer)
    chances_left = 5
    while chances_left:
        chances_left -= 1
        user_input = get_user_input()
        if user_input > correct_answer:
            print("Correct answer is smaller!")
        elif user_input < correct_answer:
            print("Correct answer is greater!")
        else:
            print("You win")
            break
        print("Chances left: " + str(chances_left))

    if chances_left == 0:
        print("You lose!")

    restart()


play_game()
