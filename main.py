import discord
import os
import random
import requests
from PIL import Image
from keep_alive import keep_alive

randomfacts = ["The 3x3x3x3 has 216 stickers", "The 4D Rubik's Cube has 8 sides", "In 4D, an edge piece has 3 colours, and can be twisted in 6 ways instead of 2", "In 4D, a corner piece has 4 colours, and can be twisted in 12 ways instead of 3", "In 4D, twisting a side is like rotating a whole cube instead of just turning a square", "The formula to calculate the number of states for the 3x3x3x3 is (24!x32!)/2 x 16!/2 x 2^23 x (3!)^31 x 3 x (4!/2)^15 x 4", "To write 3x3x3x3 shorter, you can use an exponent like 3^4", "MC4D is a program that lets you play with 4-dimensional twisty puzzles", "The 3x3x3x3 has 8 1-coloured pieces, 18 2-coloured pieces, 32 3-coloured pieces, and 16 4-coloured pieces", "The speedsolving world record for the 3x3x3x3 is 10:11 by Tetrian22", "The FMC world record for the 3x3x3x3 is 211 twists with no computer help, by Charles Doan", "Melinda's Physical 2x2x2x2 is a real puzzle that you can play with that works just like a 2x2x2x2", "The 4th dimension in MC4D is represented as inwards vs outwards due to the projection", "Many  standard 3x3x3 methods can be scaled up and used on the 3x3x3x3"]

physmoves = ["y", "y'", "y2", "x2", "x2,y2", "x2,y", "x2,y'", "x", "x,y", "x,y'", "x,y2", "x'", "x',y", "x',y'", "x',y2", "z", "z,y", "z,y'", "z,y2", "z'", "z',y", "z',y'", "z',y2"]
physscram = []
# 1-4 = both L and R. 5 = no R. 6 = no L.
randumb = [1, 2, 3, 4, 5, 6]
lenght = [8, 10, 12]
lastmove = ""

# generates a phys 2^4 scramble by calling random moves
def generatephysscram():
  lastmove = ""
  physscram = []
  for i in range(random.choice(lenght)):
    dumb = random.choice(randumb)
    if dumb < 5:
      rand = random.choice(physmoves)
      physscram.append(rand)
      lastmove = lastmove + "L" + rand + " "
      rand = random.choice(physmoves)
      physscram.append(rand)
      lastmove = lastmove + "R" + rand + " "
    elif dumb == 5:
      rand = random.choice(physmoves)
      physscram.append(rand)
      lastmove = lastmove + "L" + rand + " "
    elif dumb == 6:
      rand = random.choice(physmoves)
      physscram.append(rand)
      lastmove = lastmove + "R" + rand + " "
    rand = "#"
    physscram.append(rand)
    lastmove = lastmove + rand + " "


# begin virtual 2^4 variables definition:


# initializes the different cells to be solved
cells = ["U", "T", "D", "K", "L", "R", "F", "B"]
Ucell = ["w"]*24
Tcell = ["m"]*24
Dcell = ["y"]*24
Kcell = ["p"]*24
Lcell = ["o"]*24
Rcell = ["r"]*24
Fcell = ["g"]*24
Bcell = ["b"]*24
temporary = []
# the list of lists that contain the stickers colours
listlist = [Ucell, Tcell, Dcell, Kcell, Lcell, Rcell, Fcell, Bcell]
pos = []
# coordinates for where to paste the visualcube pics on the board
xcoords = [350, 350, 350, 350, 75, 625, 75, 625]
ycoords = [100, 400, 700, 1000, 255, 600, 600, 255]
# temporary debug function that prints which colours should be where in each cell
def debugprint():
  print("U cell is " + str(Ucell))
  print("T cell is " + str(Tcell))
  print("D cell is " + str(Dcell))
  print("K cell is " + str(Kcell))
  print("F cell is " + str(Fcell))
  print("L cell is " + str(Lcell))
  print("B cell is " + str(Bcell))
  print("R cell is " + str(Rcell))

#the function that happens when a message is sent
client = discord.Client()
@client.event
async def on_ready():
    print('{0.user}'.format(client)+' has logged in')
@client.event
async def on_message(message):
  global boardImage
  global physscram
  global Ucell
  global Tcell
  global Dcell
  global Kcell
  global Rcell
  global Fcell
  global Lcell
  global Bcell
  # if the message starts with & (the bot's command)
  if message.content.startswith("&"):
    # displays the list of commands
    if message.content.startswith("&commands"):
      await message.channel.send("List of commands:\n**&randomfact** - Tells you a random fact about hypercubes\n**&2^4** - makes an image of a not (yet) functional 2^4\n**&help** - shows how to use the 2^4 simulator\n**&s** - generates a physical 2^4 scramble. The # means to do a U2, then stack the left endcap to the right")
    # generates a random fact and sends that as a message
    elif message.content.startswith("&randomfact"):
      rand = random.choice(randomfacts)
      await message.channel.send(rand)
    # explains how to use the 2^4 simulator
    elif message.content.startswith("&help"):
      await message.channel.send(file=discord.File("help.jpg"))
      await message.channel.send("The 2x2x2x2 Rubik's Cube is represented here by its 3-dimensional net. A way to control it is being worked on...")
    # shows the current state of the 2^4 simulator
    elif message.content.startswith("&2^4"):
      await message.channel.send(file=discord.File(drawboard()))
    # resets the puzzle to the solved state
    elif message.content.startswith("&reset"):
      Ucell = ["d"]*24
      Tcell = ["d"]*24
      Dcell = ["d"]*24
      Kcell = ["d"]*24
      Lcell = ["d"]*24
      Rcell = ["d"]*24
      Fcell = ["d"]*24
      Bcell = ["d"]*24
      await message.channel.send(file=discord.File(drawboard()))
      await message.channel.send("Puzzle has been reset!")
    # temporary command that applies a y rotation to the simulator
    elif message.content.startswith("&yrotation"):
      yrotation()
      await message.channel.send(file=discord.File(drawboard()))
    # sends a physical 2^4 scramble
    elif message.content.startswith("&showr"):
      showRcell()
      await message.channel.send(file=discord.File("board.jpg"))
    elif message.content.startswith("&s"):
      generatephysscram()
      await message.channel.send(lastmove)
    # if none of the above statements were true, do this
    else:
      await message.channel.send("Unrecognized command, please try again :grin:")


# draws the 2^4 board with images
def drawboard():
  # boardImage is set to the empty canvas.jpg image
  boardImage = Image.open("canvas.jpg")
  boardImage.save("board.jpg")
  # do this 8 times
  for i in range(len(cells)):
    # resets the url each time
    image_url = "http://cube.rider.biz/visualcube.php?fmt=png&size=300&pzl=2&fc="
    # combined = list of colours of that cell
    combined = "".join(listlist[i])
    # combines the url with the colours
    image_url += combined
    # downloads the image and saves it
    response = requests.get(image_url)
    file = open("cell.png", "wb")
    file.write(response.content)
    boardImage = Image.open("board.jpg")
    cellImage = Image.open("cell.png")
    # puts the cellImage on the boardImage
    coords = xcoords[i], ycoords[i]
    boardImage.paste(cellImage, coords)
    boardImage.save("board.jpg")
  #print("printing stuff in the drawboard() function")
  # debugprint()
  return "board.jpg"


# rotations for the virtual 2^4:

def yrotation():
  global cellImage
  global Fcell
  global Lcell
  global Bcell
  global Rcell
  temporary = Fcell.copy()
  Fcell = []
  Fcell = Lcell.copy()
  Lcell = []
  Lcell = Bcell.copy()
  Bcell = []
  Bcell = Rcell.copy()
  Rcell = []
  Rcell = temporary.copy()
  #print("printing stuff in the yrotation() function")
  # debugprint()

def showRcell():
  global Rcell
  image_url = "http://cube.rider.biz/visualcube.php?fmt=png&size=300&pzl=2&fc="
  for i in Rcell:
    #image_url += string(Rcell[i])
    teporor = "".join(Rcell[i])
    image_url += teporor
  response = requests.get(image_url)
  file = open("cell.png", "wb")
  file.write(response.content)
  boardImage2 = Image.open("canvas.jpg")
  cellImage = Image.open("cell.png")
  boardImage2.paste(cellImage, 0,0)
  boardImage2.save("board.jpg")

  



# connects this code to the bot by using the bot's token
keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)