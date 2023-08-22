# HangMan

![Responsive screenshot](/img-for-readme/amiresponsive-title.png)

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

This application is ment for:

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

Dad Jokes is a console based application. For that reason no work was put in to graphical design. Instead focus was put on creating a diagram of the entire application and use that as the base for the code. The diagram also include the Google Sheet used for data storage.


This is the initial diagram:

![Intial diagram](/docs/readme-images/p3-diagram-screen.png)

During the development process a few things were changed in the diagram. The main reason for this was that I had done a flaw in the design of the Google Sheet. I had placed the calculation formula for average score on jokes inside the sheet. I never got this to work properly so that column was eventually removed and the calculation is done in the application instead.

After the final alterations the final application diagram looks like this:

![Final diagram](/docs/readme-images/p3-diagram-final-screen.png)

[Back to top](#HangMan)

## Features 

HangMan's features:

 - Submit a Name and receive feedback according to the name provided.
 - Submit a One letter guess each round and receive visual feedback if the answer is correct or not.
 - Action user guess'd letter if the user guess's the same letter again within a round.
 - Present a winning or losing screen to users after completing the gussing round.
 - Replay HangMan indefinitly if the user chooses to.

### Existing Features

#### Submit a Name to use during gameplay:

The user is presented with an input box asking the user to input their names in a specific format.

![User Name Input](/img-for-readme/welcomescreen-user-name-input.png)

After a user has inputted a name in the specified format , users are greeted by a list of rules and the game begins.

![User Greeting and Rules](/img-for-readme/welcomescreen-welcome-and-rules.png)

After the users have revised over the rules , they can immediatly begin playing HangMan , users are greeted with a visual of hangman and the random word to guess for the round in "#" format to hide the word, users can guess a 1 character letter each attempt.

#### Submit a one-letter answer per round:

![HangMan and Random Word Starting Screen](/img-for-readme/startgame-screen.png)

If a user guess's a 1 character letter correctly , the user is informed and the random word is updated and the guess'd letter is filled in accordingly, the user doesnt lose an attempt and HangMan is unaffected.

![Starting Screen when answer is correct](/img-for-readme/startgame-correct-guess.png)

If the user guess's incorrectly , the user is informed and loses an attempt, affecting HangMan and displaying his current status to users.

![Starting Screen when answer is incorrect](/img-for-readme/startgame-incorrect-guess.png)

If the user guess's the same 1 letter answer they already guess'd the user loses and attempt and HangMan is affected and displayed, addionally the repeated guess'd word is displayed to the user to notify them that the letter is repeated. 

![Starting Screen when user guess's same letter again](../img-for-readme/startgame-winning-screen.png)

#### End Screen Decisions:

If the user succesfully guess's the word , they are congratulated and given the option to either restart the game or quit entirly.

![Winning Screen](/img-for-readme/startgame-winning-screen.png)

If the user chooses to play the game again , a new word is imported, players regain their 7 attempts and Hangman is reset to his default state.

![Winning Screen if user restarts](/img-for-readme/startgame-winning-screen-restart.png)

Similarly if the users lose the game they are informed and presented with the option to restart the game.

![Losing Screen](/img-for-readme/losing-screen.png)

If the user chooses to restart the game from the losing screen, they regain 7 attempts and Hangman is reset to his default state.

![Losing Screen restart](https://github.com/Blaize-Egelhof/HangMan/blob/main/readme-images/losing-screen-restart.png)

## Features Left to Implement

Future versions of this application will store the users sign-in information via a database to allow for users to login and play the game, this will be implemented soley to have a leaderboard in place for my players to compete with eachother.

[Back to top](#HangMan)

## Technologies and libraries used

Main languages

- [Python](https://en.wikipedia.org/wiki/Python_programming_language)
- [MarkDown](https://en.wikipedia.org/wiki/Markdown) - Provided in the Code Institute ReadMe template

Python libraries used:

- [Time](https://docs.python.org/3/library/time.html)
- [Random](https://docs.python.org/3/library/random.html)

### Data storage

-N/A

## Testing 

Testing has been conducted continuously during the development process. Manual testing has been conducted by my mentor [Lauren-Nicole Popich](https://www.linkedin.com/in/lauren-nicole-popich-1ab87539/). Read more about bugs during development and unfixed bugs for more information.


### Bugs during development
RECORD BUGS HERE 

### Validator Testing 

The code has also been tested by using PEP8 Online http://pep8online.com/.

All 3 python files present were tested , no errors reported, find results below:

- [run.py](/readme-images/pep8-validation-run.py.png)
- [random-words.py](/readme-images/pep8-validation-random-words.py.png)
- [hangman-visuals.py](/readme-images/pep8-validation-hangman-visuals.png)

### Unfixed Bugs

Currently working to solve the bugs in this list. They will be moved to the Bugs during development section when they are solved.

- No known bugs at this point

 [Back to top](#HangMan)

## Development and Deployment

The development environment used for this project was CodeAnyWhere. To track the development stage and handle version control regular commits and pushes to GitHub has been conducted. The CodeAnyWhere environment was created using a template provided by Code Institute.

The live version of the project is deployed using Heroku(https://heroku.com)

This is how this project was deployed using Heroku:

To prepare for deployment on Heroku a requirements.txt needs to be created in the same folder as the .py file in CodeAnyWhere. This file needs to contain a list of all libraries the project needs to run as a Heroku App.

Then follow these steps:

 - Login to Heroku (Create an account if necessary)
 - Click on New in the Heroku dashboard and select ”Create new app”
 - Write a name for the app and choose your region and click ”Create App”
 - In the settings tab for the new application I created two Config vars.
   - One is named CREDS and contains the credentials key for Google Drive API
   - One is name PORT and has the value of 8000
 - Two buildpack scripts were added: Python and Nodejs (in that order)

Heroku CLI was used to deploy the project. The following steps were taken in the terminal in GitPod

Deploying your app to heroku
1. Login to heroku and enter your details.
 - command: heroku login -i
2. Get your app name from heroku.
 - command: heroku apps
3. Set the heroku remote. (Replace <i>app_name</i> with your actual app name)
 - command: heroku git:remote -a <i>app_name</i>
4. Add, commit and push to github
 - command: git add . && git commit -m "Deploy to Heroku via CLI"
5. Push to both github and heroku
 - command: git push origin main
 - command: git push heroku main

After those steps were taken the application was deployed at the following link: https://blaizeegelhof--hangman--p3-4273e3ce0a2b.herokuapp.com/

## Content 

- All text content in the application is created by the author of the project.
- The HangMan visuals on hangman_visuals.py was inspired by Kiteco then modified [Kiteco](https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py)

## Credits 

### For code inspiration, design inputs, help and advice.

I have consulted numerous websites, individuals and slack channels to get support for the code. No code block is directly copied but some generates from information I gathered from other developers and sites:


### Acknowledgment
 - [Lauren-Nicole Popich](https://www.linkedin.com/in/lauren-nicole-popich-1ab87539/) Thank you for all the amazing advise during the course of this project.
 - [Student Care at Code Insitute](https://learn.codeinstitute.net/login?next=/ci_support/diplomainfullstacksoftwarecommoncurriculum/studentcare) Thank you for assisting with any small issues encountered during development of HangMan

 - [Kiteco](https://github.com/kiteco) Thank you for giving me inspiration for starting this project

 [Am I Responsive](http://ami.responsivedesign.is/) was used to create the image on top of this ReadMe

[Back to top](#HangMan)