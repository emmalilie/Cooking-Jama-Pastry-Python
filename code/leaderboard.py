#set the levels of scoring - 
bronze_score = 2
silver_score = 3
gold_score = 5

#return names in the leaderboard file
def get_names(file_name):
    leaderboard_file = open(file_name, "r")  # be sure you have created this

  #use a for loop to iterate through the content of the file, one line at a time
    names = []
    for line in leaderboard_file:
      leader_name = ""
      index = 0

    #use a while loop to read the leader name from the line (format is "leader_name,leader_score")
      while line[index] != ",":
        leader_name = leader_name + line[index]
        index = index + 1
    #add the player name to the names list
    
      names.append(leader_name)

    
    leaderboard_file.close()

  #return the names list in place of the empty list
    return names

  
#return scores from the leaderboard file
def get_scores(file_name):
  leaderboard_file = open(file_name, "r")  # be sure you have created this

  scores = []
  for line in leaderboard_file:
    leader_score = ""    
    index = 0

    #use a while loop to index beyond the comma, skipping the player's name
    while line[index] != ",":
      index = index + 1
    #use a while loop to get the score
    while index < len(line) - 1:
      index = index + 1
      leader_score = leader_score + line[index]
    #add the player score to the scores list
    scores.append(int(leader_score))
  leaderboard_file.close()

  #return the scores in place of the empty list
  return scores


#update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores,  player_name, player_score):

  index = 0
  #loop through all the scores in the existing leaderboard list

  for index in range (len(leader_scores)):
    #check if this is the position to insert new score at
    if player_score > leader_scores[index]:
      break
    else:
      index = index + 1
  
  #insert new player and score
  leader_names.insert(index, player_name)
  leader_scores.insert(index, player_score)

  #keep both lists at 5 elements only (top 5 players)
  if len(leader_names) > 5:
    leader_names.pop()
    leader_scores.pop()
  #store the latest leaderboard back in the file
  leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
 
  #loop through all the leaderboard elements and write them to the the file
  for index in range (len(leader_names)):
    leaderboard_file.write(leader_names[index] + "," + str(leader_scores[index]) + "\n")

  leaderboard_file.close()
   
  

# draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):

  font_setup = ("Courier", 16, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-200,70)
  turtle_object.hideturtle()
  turtle_object.down()

  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  for index in range(len(leader_names)):
    turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-200,int(turtle_object.ycor())-50)
    turtle_object.down()
  
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-200,int(turtle_object.ycor())-50)
  turtle_object.pendown()

  # display message about player making/not making leaderboard
  if high_scorer:
    turtle_object.write("Congratulations!\nYou made the leaderboard!", font=font_setup)
  else:
    turtle_object.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=font_setup)


  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-200,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  #Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal
  if player_score >= gold_score:
    turtle_object.write("You earned a gold medal!", font=font_setup)
  elif player_score >= silver_score and player_score < gold_score:
    turtle_object.write("You earned a silver medal!", font=font_setup)
  elif player_score >= bronze_score and player_score < silver_score:
    turtle_object.write("You earned a bronze medal!", font=font_setup)
