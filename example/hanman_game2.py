# 행맨 게임
import random

words = ['chicken', 'dog', 'cat', 'mouse', 'frog']
lives_remaining = 10
guessed_letters = ''

def pick_a_word():
    return random.choice(words)

print(pick_a_word())

def print_word_with_blanks(word):
    #print("not done yet")
    display_word = '';
    for letter in word:
        if guessed_letters.find(letter) > -1:
            # 글자를 찾음
            display_word = display_word + letter
        else:
            # 글자를 찾을 수 없음
            display_word = display_word + '-'
    print(display_word)

def get_guess(word):
    print_word_with_blanks(word)
    print('Lives Remaining: ' + str(lives_remaining))
    guess = input(" Guess a letter or whole word?")
    return guess

def process_guess(guess, word):
    global lives_remaining
    global guessed_letters
    lives_remaining = lives_remaining - 1
    guessed_letters = guessed_letters + guess
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
            
        
