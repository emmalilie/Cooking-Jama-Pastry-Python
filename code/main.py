import turtle as trtl
import random as r
import leaderboard as lb
import time as t

#setup
leaderboard_file_name = "leaderboard.txt"
player_name = input("Please enter your name: ")

wn = trtl.Screen()
wn.setup(700, 600)

score = 0

font_setup = ("Courier", 20, "normal")

timer = 20
counter_interval = 1000  #1000 represents 1 second
timer_up = False

wn.bgpic("start.png")


#initializing score turtle
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(180, 170)
score_writer.color("white")

#initializing timer turtle
counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-150, 150)
counter.color("white")

#set game title on start screen - Jackie Le (drew asset)
title = ("start_title.gif")
wn.addshape(title)
Title = trtl.Turtle()
Title.hideturtle()
Title.shape(title)
Title.pu()
Title.goto(-30, 150)
Title.showturtle()

#startbutton turtle - Jackie Le (drew asset)
strt_btn = ("start_button.gif")
wn.addshape(strt_btn)
startButton = trtl.Turtle()
startButton.hideturtle()
startButton.shape(strt_btn)
startButton.pu()
startButton.goto(10, 0)
startButton.showturtle()

#1st slide of instruc - Jackie Le (drew assets for instruction)
shocked_trtl = trtl.Turtle()
shocked_trtl.hideturtle()
shock_text = ("shock.gif")
wn.addshape(shock_text)
shocked_trtl.shape(shock_text)

#2nd slide of instruc
happy_trtl = trtl.Turtle()
happy_trtl.hideturtle()
happy_text = ("happy.gif")
wn.addshape(happy_text)
happy_trtl.shape(happy_text)

#3rd slide of instruc | Provides instructions to play game
ready_trtl = trtl.Turtle()
ready_trtl.hideturtle()
ready_text = ("ready.gif")
wn.addshape(ready_text)
ready_trtl.shape(ready_text)

#falling food turtle set up
food_list = ["sushi.gif", "dumpling.gif", "boba.gif", "bingqilin.gif"]

#food1 falling - assets found on google for food images
food1_trtl = trtl.Turtle()
food1_trtl.hideturtle()
food1_trtl.penup()
food1_trtl.goto((r.randint(0, 350)), 300)
food1_trtl.speed(2)

#food2 falling
food2_trtl = trtl.Turtle()
food2_trtl.hideturtle()
food2_trtl.penup()
food2_trtl.goto((r.randint(-350, 0)), 300)
food2_trtl.speed(3)

#catch food turtle - asset self-made
player_trtl = trtl.Turtle()
player_trtl.pu()
player_trtl.hideturtle()
wn.addshape("playerR.gif")
wn.addshape("playerL.gif")
player_trtl.shape("playerR.gif")
player_trtl.goto(0, -120)


#function for falling food1 - Emma Li
def falling_food1():
  global score, timer_up
  food1_text = (food_list[r.randint(0, 3)])
  food1_trtl.goto((r.randint(0, 350)), 300)
  wn.addshape(food1_text)
  food1_trtl.shape(food1_text)
  food1_trtl.showturtle()
  for x in range(12):
    food1_trtl.goto(food1_trtl.xcor(), 300 - (50 * x))
    if abs(food1_trtl.xcor() - player_trtl.xcor()) < 100 and abs(
        food1_trtl.ycor() - player_trtl.ycor()) < 100:
      update_score()
      food1_trtl.hideturtle()
      break
  food1_trtl.hideturtle()


#function for falling food2 - Emma Li
def falling_food2():
  global score, timer_up
  food2_text = (food_list[r.randint(0, 3)])
  food2_trtl.goto((r.randint(-350, 0)), 300)
  wn.addshape(food2_text)
  food2_trtl.shape(food2_text)
  food2_trtl.showturtle()
  for x in range(12):
    food2_trtl.goto(food2_trtl.xcor(), 300 - (50 * x))
    if abs(food2_trtl.xcor() - player_trtl.xcor()) < 100 and abs(
        food2_trtl.ycor() - player_trtl.ycor()) < 100:
      update_score()
      food2_trtl.hideturtle()
      break
  food2_trtl.hideturtle()


#keyboard movement - Emma Li, Jackie Le (Borders)
def move_right():
  xc = player_trtl.xcor()
  player_trtl.shape("playerR.gif")
  player_trtl.forward(10)

  if xc >= 350:
    player_trtl.goto(350, player_trtl.ycor())


def move_left():
  player_trtl.shape("playerL.gif")
  player_trtl.back(10)
  xc = player_trtl.xcor()

  if xc <= -350:
    player_trtl.goto(-350, player_trtl.ycor())


#calling 1st slide
def shocked_instruc():
  shocked_trtl.showturtle()


#calling 2nd slide
def happy_instruc(x, y):
  shocked_trtl.hideturtle()
  happy_trtl.showturtle()


#calling 3rd slide
def ready_instruc(x, y):
  happy_trtl.hideturtle()
  ready_trtl.showturtle()


#function calling on game screen - Emma Li
def game(x, y):
  ready_trtl.hideturtle()
  player_trtl.showturtle()
  countdown()
  while timer_up == False:
    score_writer.showturtle()
    falling_food1()
    falling_food2()


#game functions - Emma Li
def startScreen(x, y):
  Title.hideturtle()
  startButton.hideturtle()
  wn.bgpic("loading.png")
  loading()
  wn.bgpic("main.png")
  shocked_instruc()


#loading screen - Emma Li
def loading():
  loading_trtl = trtl.Turtle()
  loading_trtl.color("white")
  loading_trtl.speed(12)
  loading_trtl.shape("circle")
  for x in range(3):
    xpos = -100
    for x in range(3):
      loading_trtl.penup()
      loading_trtl.hideturtle()
      loading_trtl.setx(xpos + (100 * x))
      loading_trtl.sety(-75)
      loading_trtl.showturtle()
      loading_trtl.stamp()
      x += 1
      t.sleep(.5)
    loading_trtl.clear()
    loading_trtl.hideturtle()


#function to update score - Jackie Le
def update_score():
  global score
  score_writer.showturtle()
  score += 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)


#define function that creates and updates leaderboard - Jackie Le
def manage_leaderboard():
  global score
  global player_trtl

  player_trtl.hideturtle()
  score_writer.hideturtle()
  counter.hideturtle()
  wn.bgpic("leader.gif")  #asset self-made

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list,
                          leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list,
                        player_trtl, score)
  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list,
                        player_trtl, score)


#defines countdown function, set if time is up, changes the counter turtle text - Emma Li
def countdown():
  global timer, timer_up
  counter.showturtle()
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    food1_trtl.hideturtle()
    food2_trtl.hideturtle()
    manage_leaderboard()

  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)


#calling functions - Emma Li
wn.listen()

startButton.onclick(startScreen)
shocked_trtl.onclick(happy_instruc)
happy_trtl.onclick(ready_instruc)
ready_trtl.onclick(game)

#player_trtl movements with key presses
wn.onkey(move_right, "Right")
wn.onkey(move_left, "Left")

wn.mainloop()

loading_trtl = trtl.shape("circle")
