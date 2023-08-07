#Need to import this Python Random Module , how the functions worked I got from https://www.w3schools.com/python/module_random.asp
import random 
#Time Module to pause between some functions function 
import time
#Pull the list variable containing all my words
from random_words import random_word_list 
#Pull the list containing the visuals for hangman
from hangman_visuals import stages

#Global variable to keep track of the users guess attempts
user_attempts = 6

def extract_random_word(): 
    '''
    Extract a random word out of the random_words.py file , specifically the random_word_list list
    '''
    random_word = random.choice(random_word_list)
    return random_word

def welcome_player():
    '''
    Simple function to welcome the player
    '''
    print("Welcome to my HangMan game!")
    print("Please enter your Name below , please dont use any numbers and ensure theres no spaces in your name.")


def check_users_inputted_name(): 
    '''
    Function to check users name inputs , logic is to check if the input answers length isnt nothing OR if iterate over the users answer and check if each iteration is either a number or a blank space, if either is encountered , the any() returns true forcing the loop to action all code in the if statement until false is given , allowing the else function to work, inspiration from https://www.tutorialspoint.com/How-to-check-if-a-string-contains-only-whitespace-letters-in-Python
    '''
    while True: 
        user_name = input("Please enter your name here: ")
        if len(user_name) == 0 or any(char.isdigit() or char.isspace() for char in user_name):
            print(f"Invalid name, please re-enter your name without any numbers or blank spaces, you entered: {user_name}")
        else:
            print("Valid name, proceding...")
            return user_name
            
def rules_of_the_game(users_name): 
    '''
    Function to display rules to users
    '''
    print(f"Some Rules of this HangMan Game:\n 1)You will Get 6 attempts to guess the word. \n 2)If you fail to guess the word within 7 tries you have caused Mr Hangmans death and will have to try again \n 3)If you sucessfully guessed the word you will have saved Mr HangMans life and won the round! \n Thank you for playing my game,{users_name} please enjoy!")
    time.sleep(3)
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")


def main():
    random_word = extract_random_word()
    welcome_player()
    valid_name = check_users_inputted_name()
    print(f"Hello {valid_name}!")
    rules_of_the_game(valid_name)
    show_word_and_hangman(random_word)



def show_word_and_hangman(random_word): 
    '''
    Function to take the randomly chosen word as a parameter and convert it to a # string to hide the current word from user + display HangMans Status to user
    '''
    print(stages[0])
    word_place_holder = ["#" for _ in random_word]
    print(f"The length of this word is:{len(random_word)}")
    print(word_place_holder)
    check_users_inputted_answers()
    



def check_users_inputted_answers():

    while True: 
    user_name = input("Please enter your name here: ")
    if len(user_name) == 0 or any(char.isdigit() or char.isspace() for char in user_name):
        print(f"Invalid name, please re-enter your name without any numbers or blank spaces, you entered: {user_name}")
    else:
        print("Valid name, proceding...")
        return user_name





main()