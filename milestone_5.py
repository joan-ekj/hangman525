
import random 


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed =['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = [] 
    

    def check_guess(self, guess):
        '''
        This function checks the letter guessed.
         
        The purpose of this function is to check letter guessed and update the game state accordingly.
        If the guess is correct:
        - if the guess is correct, num_letters left to guess decreases.
        If the guess is incorrect:
        - num_letters left to guess decreases as well as num_lives

        Parameters:
            guess(str): The letter guessed by player.
        
        Return:
            None  
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess!{guess} is in the word")
            for index, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[index] = guess
                self.num_letters -= 1 # Decrease num_letters for each correct guess
        else: 
            self.num_letters -= 1 
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            

    def ask_for_input(self):
         '''
         This function checks if the letter guessed is valid.

         The purpose of this function is to prompt the player to guess a letter and check that it is a valid a single alphabetical character. 
         If the input is not a single alphabetical character, player will be prompted to enter a valid one.
         If they've already guessed the letter, tthe player is informed with a message.
         The loop runs until a valid character is entered after which the guess is passed to the check_guess method and appended to list_of_guesses.

         Parameters:
            None

        Return:
            None
         '''
         while True:
                guess = input('Guess a letter: ')
                if len(guess)!=1 and not guess.isalpha():
                    print('Invalid letter: "{guess}". Please, enter a single alphabetical character.')
                elif guess in self.list_of_guesses:
                    print('You already tried that letter!')
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
                    break


    def play_game(self, word_list):
        '''
        This function creates an instance of the Hangman class.

        The game loop continues until one of the following conditions is met:
        - The player runs out of lives (`num_lives == 0`), in which case the message "You lost!" is printed.
        - The player correctly guesses all letters in the word before running out of lives (`num_lives > 0` and `num_letters == 0`), in which case the message "Congratulations. You have won the game!" is printed.

        Parameter:
            word_list(list): A list of words from which the word to be guessed is randomly selected from. 
        
        Return:
            None
        '''
        num_lives = 5
        game = Hangman(word_list, num_lives)
        while True:
            if game.num_lives == 0:
                print('You lost!')
                break
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print('Congratulations. You have won the game!')
                break

