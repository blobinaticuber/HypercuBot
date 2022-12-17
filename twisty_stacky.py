import random

RLmoves = ["R", "R'", "R2", "L", "L'", "L2"] 
FBmoves = ["F", "F'", "F2","B", "B'", "B2"] 
UDmoves = ["U", "U'", "U2", "D", "D'", "D2"]
RLstacks = ["M%"]
FBstacks = ["S%"]
UDstacks = ["E%"]
moveset = [0,1,2]
ignore = []


def scramble(n):
  global moveset
  message_text = ""
  for j in range(int(n)):
    message_text += "\n" + str(j+1) + ". " + genScram()
  return message_text

def genScram():
  global moveset
  scram = ""
  for a in range(2):
    for k in range(random.randrange(3,8)):
        set = random.choice(moveset)
        if set == 0:
          if not 0 in moveset:
            moveset = [0,1,2]
          move = random.choice(RLmoves) 
          moveset = [1,2]
        elif set == 1:
          if not 1 in moveset:
            moveset = [0,1,2]
          move = random.choice(FBmoves)
          moveset = [0,2]
        elif set == 2:
          if not 2 in moveset:
            moveset = [0,1,2]
          move = random.choice(UDmoves)
          moveset = [0,1]
        scram += move + " "
    if set == 0:
      scram += random.choice(FBstacks) + " "
    elif set == 1:
      scram += random.choice(UDstacks) + " "
    elif set == 2:
      scram += random.choice(RLstacks) + " "
  return scram