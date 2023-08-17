'''
Visually show current HangMan status based on users attempts,
These image examples was taken from Kiteco ,then modifed, credits below:
https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py
'''
stages = [
        """
          +---+
              |
              |
              |
              |
              |
        ==========
        """,
        """
          +---+
          |   |
              |
              |
              |
              |
        ==========
        """,
        """
          +---+
          |   |
          O   |
              |
              |
              |
        ==========
        """,
        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        ==========
        """,
        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        ==========
        """,
        """
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        ==========
        """,
        """
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        ==========
        """,
        """
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        ==========
        """
    ]