import turtle as t
import random

"""
def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)


t.shape('turtle')
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()
"""

# 거북이 대포 게임
"""
def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def fire():
    ang = t.heading()    #현재 거북이가 바라보는 각도를 기억하
    while t.ycor() > 0:  #거북이가 땅 위에 있는 동안 반복
        t.forward(15)
        t.right(5)

    # while문을 빠져나오면 거북이가 땅에 닿은 상태임
    d = t.distance(target, 0)  # 거북이와 목표지점과의 거리를 구함
    t.sety(random.randint(10, 100))  # '성공' 또는 '실패'를 표시할 위치를 지정함
    if d < 25:  # 거리차이가 25보다 작으면 목표 지점에 명중한 것으로 처림함
        t.color('blue')
        t.write('Good!', False, 'center', ('', 15)) # ('', 15) -> 글꼴 크기
    else:
        t.color('red')
        t.write('Bad!', False, 'center', ('', 15))
        t.color('black')
        t.goto(-200, 10)   # 거북이 위치를 처음 발사했던 곳으로 되돌림
        t.setheading(ang)  # 각도를 처음 기억해 둔 각도록 되돌림
    

# main 영역
# 땅 그리기
t.goto(-300, 0)
t.goto(300, 0)

# 목표 지점을 설정하고 그리기
# 목표 지점을 50~150 사이에 있는 임의의 수로 지정함
target = random.randint(50, 150)  
t.pensize(3)
t.color('green')
t.up()
t.goto(target-25, 2)
t.down()
t.goto(target+25, 2)

# 거북이의 색을 검은색으로 지정하고 발사했던 곳으로 되돌림
t.color('black')
t.up()
t.goto(-200, 10)
t.setheading(20)

# 거북이가 동작하는 데 필요한 설정을 함
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")
t.listen()
"""

# 터틀런 쉬운 버전
"""
# 악당 거북이(빨간색)
te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

# 먹이(초록색 동그라미)
tf = t.Turtle()
tf.shape("circle")
tf.color("green")
tf.speed(0)
tf.up()
tf.goto(0, -200)

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def play():       # 게임을 실제로 플레이하는 함수
    t.forward(10)
    ang = te.towards(t.pos())
    te.setheading(ang)   # 악당 거북이가 주인공 거북이를 바라보게함
    te.forward(9)
    if t.distance(tf) < 12:  # 주인공과 먹이의 거리가 12보다 작으면(가까우면)
        start_x = random.randint(-230, 230)
        start_y = random.randint(-230, 230)
        tf.goto(start_x, start_y)
    if t.distance(te) >= 12:  # 주인공과 먹이의 거리가 12보다 크면(멀면)
        t.ontimer(play, 100)  # 0.1초후 play 함수를 실행(게임 계속)

t.setup(500, 500)
t.bgcolor('orange')
t.shape('turtle')
t.color('white')    # 주인공 거북이(흰색)
t.speed(0)
t.up()
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()
play()
"""

# 터틀런 심화 버전
score = 0
playing = False

# 악당 거북이(빨간색)
te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

# 먹이(초록색 동그라미)
tf = t.Turtle()
tf.shape("circle")
tf.color("green")
tf.speed(0)
tf.up()
tf.goto(0, -200)

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

def play():
    global playing
    global score

    t.forward(10)
    ang = te.towards(t.pos())
    te.setheading(ang)
    speed = score + 5

    if speed > 15:
        speed = 15
    te.forward(speed)

    if t.distance(te) < 12:
        text = "Score : " + str(score)
        t.write(text, False, "center", ("", 20))
        playing = False
        score = 0

    if t.distance(tf) < 12:  # 주인공과 먹이의 거리가 12보다 작으면(가까우면)
        score = score + 1
        t.write(score)
        start_x = random.randint(-230, 230)
        start_y = random.randint(-230, 230)
        tf.goto(start_x, start_y)

    if playing:
        t.ontimer(play, 100)

t.title("Turtle Run")
t.setup(500, 500)
t.bgcolor('orange')
t.shape('turtle')
t.color('white')    # 주인공 거북이(흰색)
t.speed(0)
t.up()
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()

t.mainloop()
