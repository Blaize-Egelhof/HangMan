# HangMan

![Responsive screenshot](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/amiresponsive-title.png)

## Purpose of the Project

HangMan is a simple terminal-based game designed to provide entertainment as well as mental stimulation to players.

The application allows users to play the game indefinitely without having to re-run the code.

Target Audience: Individuals seeking thought-inducing temporary entertainment in the form of a game.

This project is the third of five milestone projects required to receive a diploma in Software Development from The Code Institute: https://codeinstitute.net/

Required Technologies for this Project: Python

A live version of this project can be found at the following URL: https://blaizeegelhof--hangman--p3-4273e3ce0a2b.herokuapp.com/


# Table of Content

+ [UX](#ux "UX")
  + [User Demographic](#user-demographic "User Demographic")
  + [User Stories](#user-stories "User Stories")
  + [User Goals](#user-goals "User goals")
  + [Project Requirements](#project-requirements "Project Requirements")
  + [Design diagram](#design-diagram "Design diagram")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
    + [Submit a Name to use during gameplay](#Submit-a-Name-to-use-during-gameplay "Submit a Name to use during gameplay")
    + [Submit a one-letter answer per round](#Submit-a-one-letter-answer-per-round "Submit a one-letter answer per round")
    + [Decide on an outcome on each end-screen](#End-Screen-Decisions "End-screen decisions")
  + [Features Left to Implement](#features-left-to-implement "Features Left to Implement")
+ [Technologies and libraries used](#Technologies-and-libraries-used "Technologies and libraries used")
  + [Data storage](#data-storage "Data Storage")
+ [Testing](#testing "Testing")
  + [Bugs during development](#bugs-during-development "Bugs during development")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Development and Deployment](#development-and-deployment "Development and Deployment")
+ [Content](#content "Content")
+ [Credits](#credits "Credits")

## UX

### User Demographic

This application is meant for:

 - All individuals who enjoy playing Hangman and solving word-based puzzles.
 - People looking for a simple and entertaining game to play in their free time.

### User Stories

User stories for this Hangman application can be categorized into two sections: Gameplay and User Interaction.

#### Gameplay
- As a player, I want to be able to enter my name before starting the game, so that I have a personalized experience.
- As a player, I want the game to be engaging and easy to understand, so that I can enjoy playing it without confusion.

#### User Interaction

- As a user, I want to be able to guess letters and solve the word puzzle.
- As a user, I want to receive feedback on my guesses, indicating whether they were correct or not.
- As a user, I want the game to display the Hangman's progress visually to make it more immersive.


### User Goals

- To challenge themselves and have fun by solving word puzzles.
- To enjoy a classic game that exercises their vocabulary and critical thinking skills.

### Project Requirements

- Python application to be deployed in Heroku.

### Design diagram

Hangman is a console based application. For that reason no work was put in to graphical design. Instead focus was put on creating a diagram of the entire application and use that as the base for the code.

This is the initial diagram:

![Intial diagram](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/initial-flow-chart.png)

During the development process a few things were changed in the diagram. The main reason for this was that  during the devlopement process I realised my flow-chart logic is flawed and as such doesnt behave how a regular HangMan game should, I altered the games looping logic to constantly check if users have remaining attempts to ensure correct game logic.

[Back to top](#HangMan)

## Features 

HangMan's features:

 - Submit a Name and receive feedback according to the name provided.
 - Submit a One letter guess each round and receive visual feedback if the answer is correct or not.
 - Action user guessed letter if the user guess's the same letter again within a round.
 - Present a winning or losing screen to users after completing the gussing round.
 - Replay HangMan indefinitly if the user chooses to.

### Existing Features

#### Submit a Name to use during gameplay:

The user is presented with an input box asking the user to input their names in a specific format.

![User Name Input](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/welcomescreen-user-name-input.png)

After a user has inputted a name in the specified format , users are greeted by a list of rules and the game begins.

![User Greeting and Rules](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/welcomescreen-welcome-and-rules.png)


#### Submit a one-letter answer per round:

After the users have revised over the rules , they can immediatly begin playing HangMan , users are greeted with a visual of hangman and the random word to guess for the round in "#" format to hide the word, users can guess a 1 character letter each attempt.

![HangMan and Random Word Starting Screen](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/startgame-screen.png)

If a user guesses a 1 character letter correctly , the user is informed and the random word is updated and the guessed letter is filled in accordingly, the user doesnt lose an attempt and HangMan is unaffected.

![Starting Screen when answer is correct](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/startgame-correct-guess.png)

If the user guesses incorrectly , the user is informed and loses an attempt, affecting HangMan and displaying his current status to users.

![Starting Screen when answer is incorrect](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/startgame-incorrect-guess.png)

If the user guess's the same 1 letter answer they already guess'd the user loses and attempt and HangMan is affected and displayed, addionally the repeated guess'd word is displayed to the user to notify them that the letter is repeated. 

![Starting Screen when user guess's same letter again](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/startgame-guessed-answer-is-the-same.png)

#### End Screen Decisions:

If the user succesfully guess's the word , they are congratulated and given the option to either restart the game or quit entirly.

![Winning Screen](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/startgame-winning-screen.png)

If the user chooses to play the game again , a new word is imported, players regain their 7 attempts and Hangman is reset to his default state.

![Winning Screen if user restarts](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/startgame-winning-screen-restart.png)

Similarly if the users lose the game they are informed and presented with the option to restart the game.

![Losing Screen](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/losing-screen.png)

If the user chooses to restart the game from the losing screen, they regain 7 attempts and Hangman is reset to his default state.

![Losing Screen restart](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/losing-screen-restart.png)

## Features Left to Implement

Future versions of this application will store users sign-in information via a database to allow for users to login and play the game, this will be implemented soley to have a leaderboard in place for my players to compete with eachother.
In addition to the above , upon succesfully guessing a word and winning a round , I want to introduce a new stage with increasing difficulty, with each stage getting harder, in these stages the word to guess decreases in characters , increasing the likelyhood of guessing wrong.

[Back to top](#HangMan)

## Technologies and libraries used

Main Languages:

- [Python](https://en.wikipedia.org/wiki/Python_programming_language)
- [MarkDown](https://en.wikipedia.org/wiki/Markdown) - Provided in the Code Institute ReadMe template
- [Git](https://git-scm.com/)

Python libraries used:

- [Time](https://docs.python.org/3/library/time.html)

The integration of the time library introduces short pauses between specific function executions. Its primary purpose is to enhance the overall gameplay experience, particularly when there is a sequence of crucial information for players to absorb before engaging. Without the implementation of the time library, players might inadvertently overlook vital details, resulting in a less polished gaming experience.

- [Random](https://docs.python.org/3/library/random.html)

The random library is crucial for selecting a word from the random_word array in the random_words.py file. It ensures that players encounter a completely different word with each attempt or round. This dynamic element adds a fresh challenge to every round, making the game more engaging, this also acts as my games "hooking" method , IE:The main way to keep users playing my game.

### Data storage

-N/A

## Testing 

Testing has been conducted continuously during the development process. Manual testing has been conducted by my mentor [Lauren-Nicole Popich](https://www.linkedin.com/in/lauren-nicole-popich-1ab87539/). Read more about bugs during development and unfixed bugs for more information.

Please refer to the below table for testing: 

**TEST** | **ACTION** | **EXPECTATION** | **RESULT** 
----------|----------|----------|----------
Input - Name | tried entering in numbers, symbols, enter, spaces	| program prompts user to enter valid input | Works as expected
Input - Name | tried entering in a name | game progresses | Works as expected
Input - Letter guesses | tried entering in numbers, symbols, enter, spaces or any string longer than 1 character| program prompts user to enter valid input | Works as expected
Input - Letter guesses | tried entering in a single letter | game progresses | Works as expected
Input - Letter guesses | tried entering in a single guessed letter again | game prompted user that the letter was guessed already | Works as expected
Input - Losing Screen Prompt to try again | tried entering in numbers, symbols, enter, spaces	| program prompts user to enter valid input | Works as expected
Input - Losing Screen Prompt to try again | tried entering Y/y or N/n  | game either restarted if Y/y or exited if N/n | Works as expected
Input - Winning Screen Prompt to try again | tried entering in numbers, symbols, enter, spaces	| program prompts user to enter valid input | Works as expected
Input - Winning Screen Prompt to try again | tried entering Y/y or N/n  | game either restarted if Y/y or exited if N/n | Works as expected


### Bugs during development
When developing the functions for validating users inputs, the use of multiple OR statements never worked the way I was expecting: 
- My solution to this was using "And Not" or "And" statements together in order to achieve the desired logic. 

The same winning screen was displayed both after the user guessed the word correctly and after the user lost the game. Additionally, the same losing screen was displayed after the user guessed the word correctly.
- Adjust the code to display the correct winning and losing screens in their respective conditions. The losing screen should only be displayed when the user actually loses the game.

The code in the check_guess function included a nested while loop that checked the user's input for each guess. This was redundant.
- Removed the nested loop and simplified the logic for checking user input, focusing on validating the user's answer and handling it accordingly

The initial version of the check_users_inputted_answers function allowed users to input a word with spaces and digits, as long as it was only one character long.
- Modified the logic to ensure that the input is exactly one alphabetic character without spaces or digits.

When a user guessed the same 1 letter answer again within the same round the check_guess function wouldnt correctly deduct a players attempt and adjust Hangmans state
- Modifed the logic to correctly access the global variable used to update Hangman and the players attempts , and then display those values to users. 

When a user choose to restart hangman , they appropriate global variables were not being updated which resulted in the 2nd round of Hangman either being cut short due to lack of attempts (which where carries over from the previous round instead of resetting) or the Hangman variable exceeding the index number of 8 , which broke Hangman as there isnt an index 9 on Hangman-visuals list. 
- Modifed game logic to correctly access and update the global variables to ensure players start a new round correctly.


### Validator Testing 

The code has also been tested by using PEP8 Online https://pep8ci.herokuapp.com/.

All 3 python files present were tested , no errors reported, find results below:
I am aware of the warnings given for my hangman-visuals.py file, I am unable to resolve them as of yet. 

- [run.py](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/pep8-validation-run.py.png)
- [random-words.py](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/pep8-validation-random-words.py.png)
- [hangman-visuals.py](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme_images/pep8-validation-hangman-visuals.py.png)

### Unfixed Bugs

Currently working to solve the bugs in this list. They will be moved to the Bugs during development section when they are solved.

- No known bugs at this point

 [Back to top](#HangMan)

## Development and Deployment

The development environment used for this project was CodeAnyWhere. To track the development stage and handle version control regular commits and pushes to GitHub has been conducted. The CodeAnyWhere environment was created using a template provided by Code Institute.

The live version of the project is deployed using Heroku(https://heroku.com)

This is how this project was deployed using Heroku:

To prepare for deployment on Heroku a requirements.txt needs to be created in the same folder as the .py file in CodeAnyWhere/Any IDE. This file needs to contain a list of all libraries the project needs to run as a Heroku App, however this application doesnt require any contents for requirments.py.

Then follow these steps:
 - Fork the repository on GitHub.
 - Launch it in your IDE. ( [CodeAnyWhere](https://app.codeanywhere.com/) and [GitPod](https://www.gitpod.io/) were used during   the development of this project. )
 - Perform the initial git add, commit, and push back to GitHub.
 - Login to Heroku (Create an account if necessary)
 - Click on New in the Heroku dashboard and select ”Create new app”
 - Write a name for the app and choose your region and click ”Create App”
 - Two buildpack scripts were added: Python and Nodejs (in that order)
 - Connect your GitHub account to Heroku and select the repository containing this application. 
 - Enable automatic deployment to allow Heroku to re-build your application with each git push to the above mentioned repository.

After those steps were taken the application was deployed at the following link: https://blaizeegelhof--hangman--p3-4273e3ce0a2b.herokuapp.com/

## Content 

- All text content in the application is created by the author of the project.
- The HangMan visuals on hangman_visuals.py was inspired by Kiteco then modified [Kiteco](https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py)

## Credits 

### For code inspiration, design inputs, help and advice.

I have consulted numerous websites. No code block is directly copied but some generates from information I gathered from other developers and sites.

### Acknowledgment
 - [Lauren-Nicole Popich](https://www.linkedin.com/in/lauren-nicole-popich-1ab87539/) Thank you for all the amazing advise during the course of this project.
 - [Student Care at Code Insitute](https://learn.codeinstitute.net/login?next=/ci_support/diplomainfullstacksoftwarecommoncurriculum/studentcare) Thank you for assisting with any small issues encountered during development of HangMan

 - [Kiteco](https://github.com/kiteco) Thank you for giving me inspiration for starting this project

 - [Am I Responsive](http://ami.responsivedesign.is/) was used to create the image on top of this ReadMe

[Back to top](#HangMan)