#Need to import this Python Random Module , how the functions worked I got from https://www.w3schools.com/python/module_random.asp
import random 
#Pull the list variable containing all my words
from random_words import random_word_list 

def extract_random_word(): 
    random_word = random.choice(random_word_list )
    return random_word


random_word = extract_random_word()
