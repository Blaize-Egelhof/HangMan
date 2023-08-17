#Import the random module for generating random choices
import random 
#Import the time module for adding delays 
import time
#Import the list of random words from the random_words module
from random_words import random_word_list 
#Import the list of visuals for Hangman stages
from hangman_visuals import stages

#Global variable to keep track of the users guess attempts
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
    print("Please enter your Name below , please dont use any numbers and ensure theres no spaces in your name.\n")


def check_users_inputted_name(): 
    '''
    Check and validate the user's inputted name inspiration from https://www.tutorialspoint.com/How-to-check-if-a-string-contains-only-whitespace-letters-in-Python
    '''
    while True:
        user_name = input("Please enter your name here: ")
        if user_name.isalpha() and not any(char.isdigit() for char in user_name) and ' ' not in user_name:
            print("Valid answer, proceeding...")
            time.sleep(2)
            print("\n \n")
            break
        else:
            print(f"Invalid input, please input an alphabetic name without any spaces or numbers, you entered: {user_name}")

    return user_name     
            
def rules_of_the_game(users_name): 
    '''
    Function to display rules to users , takes the users name input as parameter to display welcome text
    '''
    print("Here are the Rules of this HangMan Game:\n\n 1)You will get 7 incorrect attempts to guess the word. \n 2)Any correct guesses will not affect your 7 attemps \n 3)If you have already guessed a letter you will lose an attempt causing Hangman to suffer \n 4)If you sucessfully guessed the word you will have saved Mr HangMans life and won the round!\n")
    print(f"Thank you for playing my game {users_name}, please enjoy!")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")


def main():
    '''
    The main function that orchestrates the game.
    '''
    welcome_player()
    valid_name = check_users_inputted_name()
    print(f"Hello {valid_name}!\n")
    time.sleep(2)
    rules_of_the_game(valid_name)

    while True:
        random_word = extract_random_word()
        start_game(random_word)
        player_selection = end_screen()
        restart_hangman(player_selection)

def show_hangman_state():
    '''
    Displays hangmans current state to users
    '''
    print(stages[hangman_state])

def hangman_when_answer_is_wrong(): 
    '''
    Increments hangman variable to update hangmans current status
    '''
    global hangman_state
    hangman_state +=1 

def start_game(random_word): 
    '''
    Start the game with the given random word.
    Display hangman's status and handle user's input.
    '''
    user_answers_list = set()
    word_place_holder = ["#" for _ in random_word]
    while user_attempts > 0:
        show_hangman_state()
        print(f"The length of this word is, {len(random_word)} characters long")
        print(" ".join(word_place_holder))
        validated_answer = check_users_inputted_answers()
        check_guess(validated_answer, random_word, word_place_holder, user_answers_list)
        if "#" not in word_place_holder:
            global hangman_state
            print("Congratulations! You've guessed the word.")
            print(stages[hangman_state])
            player_selection = end_screen()
            restart_hangman(player_selection)
        else:
            pass
    else:
        print("GAME OVER \n We lost HangMan...")
        print(stages[hangman_state])

def end_screen(): 
    '''
    Function to give users an option to reply the quiz app, validates users answers to ensure that users either submit y or n, nothing else!
    '''
    print("Play Again?\n y = yes , n = no")
    while True:
        user_input = input("y/n: ")
        if user_input.lower() == "y" or user_input.lower() == "n":
            print("Valid Answer, proceeding...")
            time.sleep(1)
            break
        else:
            print("Invalid input, please enter either 'y' or 'n'.")
    return user_input.lower()

def restart_hangman(player_selection): 
    '''
    Restarts HangMan for the current player, ignores all introduction functions and throws the player back into the game.
    '''
    if player_selection == "y" :
        new_random_word = extract_random_word() 
        global user_attempts, hangman_state
        user_attempts = 7 
        hangman_state = 0  
        start_game(new_random_word)  
    else:
        exit()


def check_users_inputted_answers():
    '''
    Check if input is a 1 letter answer, will continue looping if there's 0 or more than 1 letter in the user's answer, and if there are any spaces or digits present. If the input is valid, the loop breaks.
    '''

    while True: 
        users_answer = input("Please input your one letter answer here:")
        if len(users_answer) != 1 or not users_answer.isalpha():
            print(f"Invalid input, please enter a single alphabetic character."")
        else:
            return users_answer.lower()

main()