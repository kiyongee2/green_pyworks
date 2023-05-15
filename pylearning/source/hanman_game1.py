# 행맨 게임
import random

words = ['dog', 'cat', 'monkey', 'chicken', 'horse', 'elephant']
lives_remaining = 10 #전역 변수

def pick_a_word():
    return random.choice(words)

print(pick_a_word())

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

def get_guess(word):
    return 'a'  #게이머가 항상 'a'를 추축한다고 가정

def process_guess(guess, word):
    global lives_remaining
    lives_remaining -= 1
    return False # 종료되지 않고 계속 진행

play()
            
        
