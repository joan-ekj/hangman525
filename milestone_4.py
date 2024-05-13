
#define the __init__ method of Hangman
import random 

class Hangman:
    def __init__(self, word_list, num_lives=4):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed =['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = [] 
    
    def check_guess(self, guess):
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
         while True:
                guess = input('Guess a letter: ')
                if len(guess)!=1 and not guess.isalpha():
                    print('Invalid letter. Please, enter a single alphabetical character.')
                elif guess in self.list_of_guesses:
                    print('You already tried that letter!')
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
                    break

Hangman.ask_for_input()




