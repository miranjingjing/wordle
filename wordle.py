import random
from re import A
from words import words
import string

def get_valid_word(): # retrieve valid word from work bank
    word = random.choice(words)
    while '-' in word or ' ' in word or len(word) != 5: # word has '-' or ' ' or not 5 letters
        word = random.choice(words)

    return word.upper()

def colored(r, g, b, text): # prints color
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def wordle():
    word = get_valid_word()
    lives = 6
    alphabet = set(string.ascii_uppercase) # letters in alphabet

    while lives > 0:
        word_letters = set(word) # letters in word
        guess = input("Enter a 5-letter word: ").upper()
        output = []
        invalid = 0
        correct = 1
        if (len(guess) != 5): # length is not 5
            print('Incorrect number of letters. ')
            invalid = 1

        for index in range(0, 5): # contains non-letter char
            if (ord(guess[index]) < 65 or ord(guess[index]) > 90):
                print('Word contains invalid character. ')
                invalid = 1
                break
        
        for index in range(0, 5): # print word
            if (guess[index] == word[index]): # green
                word_letters.remove(guess[index])
                output.append(colored(0, 255, 0, guess[index]))
            elif (guess[index] in word_letters): # yellow
                word_letters.remove(guess[index])
                output.append(colored(255, 255, 0, guess[index]))
                correct = 0
            else: # white
                output.append(guess[index])
                correct = 0

        if (invalid):
            continue

        print(*output)
        if (correct):
            break
        lives = lives - 1 # lose a life

        
    if lives == 0: # run out of lives
        print('You have failed to guess the word. The word was', word)
    else: # still have lives
        print('Congrats! You guessed the word ', word, '!')

    return

wordle()