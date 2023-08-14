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
    time.sleep(0)
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")


def main():
    random_word = extract_random_word()
    welcome_player()
    valid_name = check_users_inputted_name()
    print(f"Hello {valid_name}!")
    rules_of_the_game(valid_name)
    show_word(random_word)

def show_hangman_state():
    print(stages[hangman_state])

def hangman_when_answer_is_wrong(): 
    global hangman_state
    hangman_state +=1

def show_word(random_word): 
    '''
    Function to take the randomly chosen word as a parameter and convert it to a # string to hide the current word from user + display HangMans Status to user
    '''
    #INSERT A while LOOP TO CHECK IF THE GLOBAL TRIES VARABLE ISNT != 0 and loop , if it is =0 iTS GAME OVER 
    user_answers_list = set()
    while user_attempts > 0:
        show_hangman_state()
        word_place_holder = ["#" for _ in random_word]
        print(f"The length of this word is, {len(random_word)} characters long")
        print(" ".join(word_place_holder))
        validated_answer = check_users_inputted_answers()
        check_guess(validated_answer, random_word, word_place_holder, user_answers_list)
    else:
        print("GAME OVER \n We lost HangMan...")
        #Create function for end screen

def check_guess(users_answer, word_to_guess, hidden_word, user_answers_list):
    '''
    Check if the users answer is already in their list, if it is ,that means they have already guessed the same word and will lose a ty , otherwise find the index of the correctly guessed letter and update the hidden word by 1 revealed character.
    '''
    if users_answer in user_answers_list:
        print(f"You have already used the letter{users_answer}")
        global user_attempts
        user_attempts -= 1
        #INSERT FUNCTION TO SHOW HANGMAN 
        print(f'You have {user_attempts}remaining')
        return 
    user_answers_list.add(users_answer)

    if users_answer in word_to_guess: 
        print(f"Correct! {users_answer} is in the word")
        for x,y in enumerate(word_to_guess):
            if y == users_answer:
                hidden_word[x] = users_answer
                print(hidden_word)

    else:
        print(f"Bad guess! The letter {users_answer} is not in the word.")
        hangman_when_answer_is_wrong()



def check_users_inputted_answers():
    '''
    Check if input is a 1 letter answer , will continue looping if theres 0 or more than 1 letter in the users answer , and if theres any spaces or digits present , if not then the loop breaks.
    '''

    while True: 
        users_answer = input("Please input your one letter answer here:")
        if (len(users_answer) != 1 ) or any(char.isdigit() or char.isspace() for char in users_answer):
            print(f"Invalid input , please input a one letter answer without any spaces or numbers you entered: {users_answer}")
        else:
            print("Valid answer, proceding...")
            break
    return users_answer



main()