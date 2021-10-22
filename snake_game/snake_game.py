import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
screen = turtle.Screen()
screen.setup(width=450, height=300)
screen.bgcolor("green")
screen.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.goto(-110, 130)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 12, "normal"))
pen.hideturtle()

# Functions
def go_up():
  if head.direction != "down":
    head.direction = "up"
def go_down():
  if head.direction != "up":
    head.direction = "down"
def go_left():
  if head.direction != "right":
    head.direction = "left"
def go_right():
  if head.direction != "left":
    head.direction = "right"
def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y + 10)
  if head.direction == "down":
    y = head.ycor()
    head.sety(y - 10)
  if head.direction == "left":
    x = head.xcor()
    head.setx(x - 10)
  if head.direction == "right":
    x = head.xcor()
    head.setx(x + 10)

screen.listen()
screen.onkey(go_up, "up")
screen.onkey(go_down, "down")
screen.onkey(go_left, "left")
screen.onkey(go_right, "right")

# Main game loop
while True:
  screen.update()
  if int(head.xcor()) > 220 or int(head.xcor()) < -220 or int(head.ycor()) > 145 or int(head.ycor()) < -145 :
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"
    # create addade food cordinate 
    for segment in segments:
      segment.goto(1000, 1000)
    screen.clear()
    delay = 0.1
    score = high_score
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 12, "normal"))
    break
  
  #check fod get
  if head.distance(food) < 10:
    x = random.randint(-220, 220)
    y = random.randint(-145, 145)
    food.goto(x,y)
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    new_segment.clear()
    segments.append(new_segment)
    delay -= 0.001
    score += 10
    high_score = score
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 12, "normal"))
  for i in range(len(segments)-1, 0, -1):
    x = segments[i-1].xcor()
    y = segments[i-1].ycor()
    segments[i].goto(x,y)
  if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x,y)
  move()
  for seg in segments :
    if seg.distance(head) < 10:
      time.sleep(1)
      head.goto(0,0)
      head.direction = "stop"
      # create addade food cordinate 
      for segment in segments:
        segment.goto(1000, 1000)
      screen.clear()
      delay = 0.1
      score = high_score
      pen.clear()
      pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 12, "normal"))
      break
      
  time.sleep(delay)
  
