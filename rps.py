import random
comp= 0;
player_s = 0;
print(":)Welcome, Play Rock Paper Scissors with the computer,\n Pick 0 for rock, 1 for paper, 2 for scissors \n if you want to quit, pick 8");
a = True
while(a == True):
  x = int(input('Pick:'))
  if (x == 8):
    a = False
    print("Thanks for playing")
    break
  player = x;
  
  if((x<0) or (x>=3)):
    print('Please choose a number between 0 and 2')
    
  # player.append(x);
  y = random.randrange(0,2);
  comp = y;
  print('The computer chose ', y);
  # comp.append(y)
  if(player == 0 and comp == 0):
    print("It is a tie")
  elif(player == 0 and comp == 1):
    print("Computer won")
    comp = comp + 1
  elif(player == 0 and comp == 2):
    print("Player won")
    player_s = player_s + 1
  elif(player == 1 and comp == 0):
    print("Player won")
    player_s = player_s + 1
  elif(player == 1 and comp == 1):
    print("It is a tie")
  elif(player == 1 and comp == 2):
    print("Computer won")
    comp = comp + 1
  elif(player == 2 and comp == 0):
    print("Computer won")
    comp = comp + 1
  elif(player == 2 and comp == 1):
    print("Computer won")
    comp = comp + 1
  elif(player == 2 and comp == 2):
    print("It is a tie")
    

print("Player scored = "+ str(player_s))
print("Computer scored = "+ str(comp))

