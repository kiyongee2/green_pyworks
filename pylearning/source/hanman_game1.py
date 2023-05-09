# 행맨 게임
import random

words = ['chicken', 'dog', 'cat', 'mouse', 'frog']
lives_remaining = 6

def pick_a_word():
    return random.choice(words)

print(pick_a_word())

def get_guess(word):
    return 'a'

def process_guess(guess, word):
    global lives_remaining
    lives_remaining -= 1
    return False

def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print("You win! Well done!")
            break
        if lives_remaining == 0:
            print("You are Hung!")
            print("The word was: " + word)
            break

play()
            
        
