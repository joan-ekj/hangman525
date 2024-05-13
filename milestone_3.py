import random

word_list=['strawberry', 'mango', 'kiwi', 'orange', 'peach']
print(word_list)

word = random.choice(word_list)
print(word)

#check whether the guess is in the word
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess!{guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

#check if input is valid
def ask_for_input():
    while True:
            try:
                guess = input('Guess a letter: ')
                if len(guess)==1 and guess.isalpha():
                    break
            except:
                print('Invalid letter. Please, enter a single alphabetical character.')

    check_guess(guess)

ask_for_input()

