#Need to import this Python Random Module , how the functions worked I got from https://www.w3schools.com/python/module_random.asp
import random 
#Pull the list variable containing all my words
from random_words import random_word_list 

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
    Function to check users name inputs , logic is to check if the input answer isnt nothing OR if iterate over the users answer and check if each iteration is either a number or a blank space, if either is encountered , the any() returns true forcing the loop to action all code in the if statement until false is given , allowing the else function to work, inspiration from https://www.tutorialspoint.com/How-to-check-if-a-string-contains-only-whitespace-letters-in-Python
    '''
    while True: 
        user_name = input("Please enter your name here: ")
        if len(user_name) == 0 or any(char.isdigit() or char.isspace() for char in user_name):
            print(f"Invalid name, please re-enter your name without any numbers or blank spaces, you entered: {user_name}")
        else:
            print("Valid name, please proceed.")
            return user_name
            


        










random_word = extract_random_word()
welcome_player()
check_users_inputted_name()
