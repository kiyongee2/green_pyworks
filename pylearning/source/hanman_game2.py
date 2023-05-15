# 행맨 게임
import random

words = ['dog', 'cat', 'monkey', 'chicken', 'horse', 'elephant']
lives_remaining = 10
guessed_letters = ''

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

def pick_a_word():
    return random.choice(words)

# print(pick_a_word())

def get_guess(word):
    print_word_with_blanks(word)
    print('Lives Remaining:' + str(lives_remaining))
    guess = input(" Guess a letter or whole word? ")
    return guess

def print_word_with_blanks(word):
    # print('아직 작성하지 않음')
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1: # 글자를 찾음
            display_word = display_word + letter
        else: # 글자를 찾지 못함
            display_word = display_word + '-'
    print(display_word)

def process_guess(guess, word):
    global lives_remaining
    global guessed_letters
    lives_remaining -= 1
    guessed_letters += guess  #글자가 출력됨
    if guess == word:  #전체 글자가 일치하면 바로 프로그램 종료
        return True
    return False  # 종료되지 않고 계속 진행

play()
            
        
