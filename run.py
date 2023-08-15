#Need to import this Python Random Module , how the functions worked I got from https://www.w3schools.com/python/module_random.asp
import random 
#Time Module to pause between some functions function 
import time
#Pull the list variable containing all my words
from random_words import random_word_list 
#Pull the list containing the visuals for hangman
from hangman_visuals import stages

#Global variable to keep track of the users guess attempts
user_attempts = 7
hangman_state = 0

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
    print("Welcome to my HangMan game!\n")
    time.sleep(1)
    print("Please enter your Name below , please dont use any numbers and ensure theres no spaces in your name.\n")


def check_users_inputted_name(): 
    '''
    Function to check if theres any digits, blank spaces ,and if the inputted values are alpha numeric , if not then loop iterates until valid answer is given inspiration from https://www.tutorialspoint.com/How-to-check-if-a-string-contains-only-whitespace-letters-in-Python
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
    Function to display rules to users
    '''
    print("Here are the Rules of this HangMan Game:\n\n 1)You will get 7 incorrect attempts to guess the word. \n 2)Any correct guesses will not affect your 7 attemps \n 3)If you have already guessed a letter you will lose an attempt causing Hangman to suffer \n 4)If you sucessfully guessed the word you will have saved Mr HangMans life and won the round!\n")
    print(f"Thank you for playing my game {users_name}, please enjoy!")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")


def main():
    random_word = extract_random_word()
    welcome_player()
    valid_name = check_users_inputted_name()
    print(f"Hello {valid_name}!\n")
    time.sleep(2)
    rules_of_the_game(valid_name)
    show_word(random_word)

def show_hangman_state():
    print(stages[hangman_state])

def hangman_when_answer_is_wrong(): 
    global hangman_state
    hangman_state +=1 

def show_word(random_word): 
    '''
    Function to take the randomly chosen word as a parameter and convert it to a # string to hide the current word from user + display HangMans Status to user. 
    This function also validated and handles users answer and responds accordingly, this all loops until the player either guess's the whole word meaning theres no # left in the string OR they run out of attempts
    Addionally this function stores users 1 letter guess's in a set called user_answers_list , this is checked during the check_guess validation function to ensure users dont answer with the same letter during their playthrough
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
            # Create victory screen!
            print("Congratulations! You've guessed the word.")
            # You might want to break the loop here or take other appropriate actions
        else:
            pass
    else:
        print("GAME OVER \n We lost HangMan...")
        # Create function for end screen

def check_guess(users_answer, word_to_guess, hidden_word, user_answers_list):
    '''
    Check if the users answer is already in their list, if it is, that means they have already guessed the same word and will lose a try, otherwise find the index of the correctly guessed letter and update the hidden word by 1 revealed character.
    '''
    global user_attempts
    while True:
        if users_answer in user_answers_list:
            print(f"You have already used the letter: {users_answer}")
            user_attempts -= 1
            print(f'You have {user_attempts} remaining attempts left')
            print("-----------------------------------------------------------------------------------------------------------------------------")
        else:
            user_answers_list.add(users_answer)
        break

    if users_answer in word_to_guess: 
        print(f"Correct! {users_answer} is in the word:")
        for x, y in enumerate(word_to_guess):
            if y == users_answer:
                hidden_word[x] = users_answer
        
    else:
        print(f"Wrong Guess , try again !")
        user_attempts -= 1
        print(f"You have {user_attempts} attempts remaining...")
        hangman_when_answer_is_wrong()

def check_users_inputted_answers():
    '''
    Checks if users answer is an alpha numeric value , loop finishes if its true.
    '''
    while True:
        users_answer = input("Please input your one letter answer here:")
        if users_answer.isalpha():
            print("Valid answer, proceding...")
            print("-----------------------------------------------------------------------------------------------------------------------------")
            break
        else:
            print(f"Invalid input , please input a one letter answer without any spaces or numbers you entered: {users_answer}")
    return users_answer

main()