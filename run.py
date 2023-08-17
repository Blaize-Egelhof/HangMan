# Import the random module for generating random choices
import random
# Import the time module for adding delays
import time
# Import the list of random words from the random_words module
from random_words import random_word_list
# Import the list of visuals for Hangman stages
from hangman_visuals import stages

# Global variable to keep track of the user's guess attempts
user_attempts = 7
hangman_state = 0


def extract_random_word():
    '''
    Extract a random word from the random_words.py file.
    '''
    random_word = random.choice(random_word_list)
    return random_word


def welcome_player():
    '''
    Display a welcome message and prompt the player for their name.
    '''
    print("Welcome to my HangMan game!\n")
    time.sleep(1)
    print("Please enter your name below,\n"
          "Please don't use any numbers or spaces in your name\n")


def check_users_inputted_name():
    '''
    Check and validate the user's inputted name.
    Inspiration from:
    https://www.tutorialspoint.com/How-to-check-if-a-string-contains-only-whitespace-letters-in-Python
    '''
    while True:
        user_name = input("Please enter your name here: ")
        if (
            user_name.isalpha()
            and not any(char.isdigit() for char in user_name)
            and ' ' not in user_name
        ):
            print("Valid answer, proceeding...")
            time.sleep(2)
            print("\n \n")
            break
        else:
            print(
                "-------------------------------------------------------------"
            )
            print(
                "Invalid name, please use only letters "
                "with no spaces or numbers"
            )
            print(f"you entered: {user_name}")
            print(
                "-------------------------------------------------------------"
            )

    return user_name


def check_guess(users_answer, word_to_guess, hidden_word, user_answers_list):
    global user_attempts

    if user_attempts > 0:
        if users_answer in user_answers_list:
            print(
                "-------------------------------------------------------------"
            )
            print(f"You have already used the letter: {users_answer}")
            user_attempts -= 1
            hangman_when_answer_is_wrong()
            print(f'You have {user_attempts} remaining attempts left')
            print(
                "-------------------------------------------------------------"
            )
        else:
            if users_answer in word_to_guess:
                print(f"Correct! {users_answer} is in the word:")
                time.sleep(1)
                for x, y in enumerate(word_to_guess):
                    if y == users_answer:
                        hidden_word[x] = users_answer
            else:
                print(f"Wrong Guess , try again !")
                time.sleep(1)
                print(
                    "---------------------------------------------------------"
                )
                user_attempts -= 1
                print(f"You have {user_attempts} attempts remaining...")
                hangman_when_answer_is_wrong()

            user_answers_list.add(users_answer)

            if "#" not in hidden_word:
                print("Congratulations! You've guessed the word.")
                player_selection = end_screen()
                restart_hangman(player_selection)
    else:
        print("GAME OVER \nWe lost HangMan...\n")
        player_selection = end_screen()
        restart_hangman(player_selection)


def rules_of_the_game(users_name):
    '''
    Display rules to users, and welcomes players using their name
    '''
    print(
        "Here are the Rules of this HangMan Game:\n\n "
        "1)You will get 7 incorrect attempts to guess the word. \n "
        "2)Any correct guesses will not affect your 7 attempts \n "
        "3)Guessing a repeated letter costs an attempt, harming Hangman \n "
        "4)Guessing the word saves Mr. HangMan's life and wins the round!\n "
    )
    print(
        f"Thank you for playing my game {users_name}, please enjoy!"
    )
    time.sleep(2)
    print(
        "---------------------------------------------------------------------"
    )
    print(
        "---------------------------------------------------------------------"
    )
    time.sleep(1)


def main():
    '''
    The main function that orchestrates the game.
    '''
    welcome_player()
    valid_name = check_users_inputted_name()
    print(f"Hello {valid_name}!\n\n")
    time.sleep(2)
    rules_of_the_game(valid_name)

    while True:
        random_word = extract_random_word()
        start_game(random_word)
        player_selection = end_screen()
        restart_hangman(player_selection)


def show_hangman_state():
    '''
    Displays hangman's current state to users.
    '''
    print(stages[hangman_state])


def hangman_when_answer_is_wrong():
    '''
    Increments hangman variable to update hangman's current visual status.
    '''
    global hangman_state
    hangman_state += 1


def start_game(random_word):
    '''
    Start the game with the given random word.
    Display hangman's status and handle the user's input.
    '''
    user_answers_list = set()
    word_place_holder = ["#" for _ in random_word]
    while user_attempts > 0:
        show_hangman_state()
        print(f"The length of this word is, {len(random_word)} characters")
        print(" ".join(word_place_holder))
        validated_answer = check_users_inputted_answers()
        check_guess(
            validated_answer,
            random_word,
            word_place_holder,
            user_answers_list
        )
        if "#" not in word_place_holder:
            global hangman_state
            print("Congratulations! You've guessed the word.")
            print(stages[hangman_state])
            player_selection = end_screen()
            restart_hangman(player_selection)
        else:
            pass
    else:
        print("GAME OVER \nWe lost HangMan...")
        print(stages[hangman_state])
        player_selection = end_screen()
        restart_hangman(player_selection)


def end_screen():
    '''
    Give users an option to replay the quiz app,
    validates users' answers to ensure that users:
    either submit y or n, nothing else!
    '''
    print("Play Again?\n y = yes , n = no")
    while True:
        user_input = input("y/n: ")
        if user_input.lower() == "y" or user_input.lower() == "n":
            print("Valid Answer, proceeding...")
            time.sleep(1)
            break
        else:
            print(
                "-------------------------------------------------------------"
            )
            print("Invalid input, please enter either 'y' or 'n'.")
            print(
                "-------------------------------------------------------------"
            )
    return user_input.lower()


def restart_hangman(player_selection):
    '''
    Restarts HangMan for the current player,
    ignores all introduction functions and throws the user back into the game.
    '''
    if player_selection == "y":
        new_random_word = extract_random_word()
        global user_attempts, hangman_state
        user_attempts = 7
        hangman_state = 0
        start_game(new_random_word)
    else:
        print("EXITING...")
        exit()


def check_users_inputted_answers():
    '''
    Checks users input to ensure they guess 1 alphabetical letter
    '''

    while True:
        users_answer = input("Please input your one-letter answer here:")
        if len(users_answer) != 1 or not users_answer.isalpha():
            print(
                "-------------------------------------------------------------"
            )
            print("Invalid input, please enter a single alphabetic character.")
            print(f"You inputted: {users_answer}")
            print(
                "-------------------------------------------------------------"
            )
        else:
            return users_answer.lower()


main()
