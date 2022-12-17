import random
import discord

from PIL import Image

virtMovesList = ["Ix", "Ix'", "Ix2", "Iy", "Iy'", "Iy2", "Iz", "Iz'", "Iz2", "Rx", "Rx'", "Rx2", "Ry", "Ry'", "Ry2", "Rz", "Rz'", "Rz2", "Dx", "Dx'", "Dx2", "Dy", "Dy'", "Dy2", "Dz", "Dz'", "Dz2", "Fx", "Fx'", "Fx2", "Fy", "Fy'", "Fy2", "Fz", "Fz'", "Fz2", "Ux", "Ux'", "Ux2", "Uy", "Uy'", "Uy2", "Uz", "Uz'", "Uz2", "Bx", "Bx'", "Bx2", "By", "By'", "By2", "Bz", "Bz'", "Bz2", "Lx", "Lx'", "Lx2", "Ly", "Ly'", "Ly2", "Lz", "Lz'", "Lz2", "Ox", "Ox'", "Ox2", "Oy", "Oy'", "Oy2", "Oz", "Oz'", "Oz2" ]


# lists of stickers on each cell
Dcell = ["stickers/yellow.png"]*8
Icell = ["stickers/purple.png"]*8
Ucell = ["stickers/white.png"]*8
Lcell = ["stickers/orange.png"]*8
Bcell = ["stickers/blue.png"]*8
Fcell = ["stickers/green.png"]*8
Rcell = ["stickers/red.png"]*8
Ocell = ["stickers/pink.png"]*8

# returns the current state of the cells to main.py
def get_cells():
  return [Dcell, Icell, Ucell, Lcell, Bcell, Fcell, Rcell, Ocell]

# returns if the cube is soolved
def solved():
  return get_cells() == [
    ["stickers/yellow.png"]*8,
    ["stickers/purple.png"]*8,
    ["stickers/white.png"]*8,
    ["stickers/orange.png"]*8,
    ["stickers/blue.png"]*8,
    ["stickers/green.png"]*8,
    ["stickers/red.png"]*8,
    ["stickers/pink.png"]*8
  ]

# function that resets the lists of stickers
def reset():
  global Ucell
  global Icell
  global Dcell
  global Ocell
  global Lcell
  global Rcell
  global Fcell
  global Bcell
  Dcell = ["stickers/yellow.png"]*8
  Icell = ["stickers/purple.png"]*8
  Ucell = ["stickers/white.png"]*8
  Lcell = ["stickers/orange.png"]*8
  Bcell = ["stickers/blue.png"]*8
  Fcell = ["stickers/green.png"]*8
  Rcell = ["stickers/red.png"]*8
  Ocell = ["stickers/pink.png"]*8

  # list of cells
cells = ["U", "I", "D", "O", "L", "R", "F", "B"]
# coordinates for the cells
cell_x_coords = [150, 280, 150, 280, 20, 150, 20, 150]
cell_y_coords = [0, 75, 150, 225, 75, 150, 225, 300]
# currently D I U L B F R O
cell_x_offsets = [400, 400, 400, 0, 800, 0, 800, 1200]
cell_y_offsets = [800, 400, 0, 200, 200, 600, 600, 800]

stickerX = [0]
stickerY = [0]
cellxOffset = [500]
cellyOffset = [700]


# the new version of the simulator, using the embed
async def sticker_board(message, move):
  #embed_message = message
  cellList = get_cells()
  background = Image.open("sticker_background.jpeg")
  for i in range(8):
    # gets the sticker of the current sticker
    xoffset = cell_x_offsets[i]
    yoffset = cell_y_offsets[i]
    listicker = cellList[i]
    for i in range(8):
      sticker = Image.open(listicker[i])
      if i <= 3:
        sticker_small = sticker.resize((100,115))
      else:
        sticker_small = sticker.resize((106,122))
      coords = (cell_x_coords[i] + xoffset), (cell_y_coords[i] + yoffset)
      background.paste(sticker_small, coords, sticker_small)
      background.save("back.jpg")
  # EMBED TIME :D
  sticker_embed=discord.Embed(title="2x2x2x2", color=0xff0000)
  sticker_embed.set_image(url="back.jpg")
  file = discord.File("back.jpg", filename="image.png")
  sticker_embed.set_image(url="attachment://image.png")
  sticker_embed.add_field(name="Moves:", value=move)
  
  await message.channel.send(file=file, embed=sticker_embed)


# 4d rotations:

#rotates the U cell to the I cell's position
def UtoI():
  global Ucell
  global Icell
  global Dcell
  global Ocell
  global Lcell
  global Rcell
  global Fcell
  global Bcell
  #copies the Y-W axis of cells to the correct positions
  cellZ(Ocell)
  cellZ(Ocell)
  temporary = Icell.copy()
  Icell = []
  Icell = Ucell.copy()
  Ucell = []
  Ucell = Ocell.copy()
  Ocell = []
  cellZ(Dcell)
  cellZ(Dcell)
  Ocell = Dcell.copy()
  Dcell = []
  Dcell = temporary.copy()
  #does the appropriate rotations of the cells
  cellX(Fcell)
  cellXprime(Bcell)
  cellZprime(Rcell)
  cellZ(Lcell)

def UtoI2():
  UtoI()
  UtoI()
  
def DtoI():
  UtoI()
  UtoI()
  UtoI()

def yrotation():
  Iy()
  FtoI()
  FtoI()
  Iyprime()
  FtoI()
  FtoI()

def y2rotation():
  yrotation()
  yrotation()

def yprimerotation():
  y2rotation()
  yrotation()

def xrotation():
  FtoI()
  DtoI()
  BtoI()

def x2rotation():
  xrotation()
  xrotation()

def xprimerotation():
  x2rotation()
  xrotation()

def zrotation():
  xrotation()
  yrotation()
  xprimerotation()

def zprimerotation():
  xrotation()
  yprimerotation()
  xprimerotation()

def z2rotation():
  zrotation()
  zrotation()

def FtoI():
  global Ucell
  global Icell
  global Dcell
  global Ocell
  global Lcell
  global Rcell
  global Fcell
  global Bcell
  #copies the Y-W axis of cells to the correct positions
  temporary = Icell.copy()
  Icell = []
  Icell = Fcell.copy()
  Fcell = []
  Fcell = Ocell.copy()
  Ocell = []
  Ocell = Bcell.copy()
  Bcell = []
  Bcell = temporary.copy()
  cellX(Fcell)
  cellX(Fcell)
  cellY(Ocell)
  cellY(Ocell)
  cellX(Dcell)
  cellXprime(Ucell)
  cellYprime(Lcell)
  cellY(Rcell)

def FtoI2():
  FtoI()
  FtoI()


def BtoI():
  FtoI()
  FtoI()
  FtoI()

def RtoI():
  yrotation()
  FtoI()
  yprimerotation()

def RtoI2():
  RtoI()
  RtoI()

def LtoI():
  yrotation()
  BtoI()
  yprimerotation()




# code for the moves:

def Iy():
  global Ucell
  global Icell
  global Dcell
  global Ocell
  global Lcell
  global Rcell
  global Fcell
  global Bcell
  global undoList
  #rotates all the stickers on the I cell
  cellY(Icell)
  #rotates the U stickers
  Ucell[2], Ucell[3], Ucell[6], Ucell[7] = Ucell[6], Ucell[2], Ucell[7], Ucell[3]
  #rotates the D stickers
  Dcell[0], Dcell[1], Dcell[4], Dcell[5] = Dcell[4], Dcell[0], Dcell[5], Dcell[1]
  #rotates these stickers
  Lcell[1], Bcell[5], Rcell[4], Fcell[0] = Fcell[0], Lcell[1], Bcell[5], Rcell[4]
  #rotates these other stickers
  Lcell[3], Bcell[7], Rcell[6], Fcell[2] = Fcell[2], Lcell[3], Bcell[7], Rcell[6]
  #rotates yet some more stickers lmao
  Lcell[7], Bcell[6], Rcell[2], Fcell[3] = Fcell[3], Lcell[7], Bcell[6], Rcell[2]
  #rotates the final stickers lol
  Lcell[5], Bcell[4], Rcell[0], Fcell[1] = Fcell[1], Lcell[5], Bcell[4], Rcell[0]



def Iy2():
  Iy()
  Iy()

def Iyprime():
  Iy2()
  Iy()

def Ix():
  global Ucell
  global Icell
  global Dcell
  global Ocell
  global Lcell
  global Rcell
  global Fcell
  global Bcell
  #rotates all the stickers on the I cell
  cellX(Icell)
  #rotates the L stickers
  Lcell[1], Lcell[3], Lcell[7], Lcell[5] = Lcell[5], Lcell[1], Lcell[3], Lcell[7]
  #rotates the R stickers
  Rcell[0], Rcell[2], Rcell[6], Rcell[4] = Rcell[4], Rcell[0], Rcell[2], Rcell[6]
  #rotates the stickers 
  Ucell[6], Bcell[4], Dcell[0], Fcell[2] = Fcell[2], Ucell[6], Bcell[4], Dcell[0]
  #another one 
  Ucell[2], Bcell[6], Dcell[4], Fcell[0] = Fcell[0], Ucell[2], Bcell[6], Dcell[4]
  #comment three electric pee
  Ucell[3], Bcell[7], Dcell[5], Fcell[1] = Fcell[1], Ucell[3], Bcell[7], Dcell[5]
  #last one finally omg 
  Ucell[7], Bcell[5], Dcell[1], Fcell[3] = Fcell[3], Ucell[7], Bcell[5], Dcell[1]
  
  
def Ix2():
  Ix()
  Ix()

def Ixprime():
  Ix2()
  Ix()

def Iz():
  Ix()
  Iy()
  Ixprime()

def Iz2():
  Iz()
  Iz()

def Izprime():
  Ix()
  Iyprime()
  Ixprime()

def Rx():
  RtoI()
  Ix()
  LtoI()

def Rx2():
  Rx()
  Rx()

def Rxprime():
  Rx2()
  Rx()

def Ry():
  RtoI()
  Iy()
  LtoI()

def Ry2():
  Ry()
  Ry()

def Ryprime():
  Ry2()
  Ry()
  
def Rz():
  RtoI()
  Iz()
  LtoI()

def Rz2():
  RtoI()
  Iz2()
  LtoI()

def Rzprime():
  RtoI()
  Izprime()
  LtoI()

def Uy():
  UtoI()
  Iy()
  DtoI()

def Uy2():
  UtoI()
  Iy2()
  DtoI()

def Uyprime():
  UtoI()
  Iyprime()
  DtoI()

def Ux():
  UtoI()
  Ix()
  DtoI()

def Ux2():
  UtoI()
  Ix2()
  DtoI()

def Uxprime():
  UtoI()
  Ixprime()
  DtoI()

def Uz():
  UtoI()
  Iz()
  DtoI()

def Uz2():
  UtoI()
  Iz2()
  DtoI()

def Uzprime():
  UtoI()
  Izprime()
  DtoI()

def Fy():
  FtoI()
  Iy()
  BtoI()

def Fy2():
  FtoI()
  Iy2()
  BtoI()

def Fyprime():
  FtoI()
  Iyprime()
  BtoI()

def Fx():
  FtoI()
  Ix()
  BtoI()

def Fx2():
  FtoI()
  Ix2()
  BtoI()

def Fxprime():
  FtoI()
  Ixprime()
  BtoI()

def Fz():
  FtoI()
  Iz()
  BtoI()

def Fz2():
  FtoI()
  Iz2()
  BtoI()

def Fzprime():
  FtoI()
  Izprime()
  BtoI()

def Dy():
  DtoI()
  Iy()
  UtoI()

def Dy2():
  DtoI()
  Iy2()
  UtoI()

def Dyprime():
  DtoI()
  Iyprime()
  UtoI()

def Dx():
  DtoI()
  Ix()
  UtoI()

def Dx2():
  DtoI()
  Ix2()
  UtoI()

def Dxprime():
  DtoI()
  Ixprime()
  UtoI()

def Dz():
  DtoI()
  Iz()
  UtoI()

def Dz2():
  DtoI()
  Iz2()
  UtoI()

def Dzprime():
  DtoI()
  Izprime()
  UtoI()

def Lx():
  LtoI()
  Ix()
  RtoI()

def Lx2():
  LtoI()
  Ix2()
  RtoI()

def Lxprime():
  LtoI()
  Ixprime()
  RtoI()

def Ly():
  LtoI()
  Iy()
  RtoI()

def Ly2():
  LtoI()
  Iy2()
  RtoI()

def Lyprime():
  LtoI()
  Iyprime()
  RtoI()

def Lz():
  LtoI()
  Iz()
  RtoI()

def Lz2():
  LtoI()
  Iz2()
  RtoI()

def Lzprime():
  LtoI()
  Izprime()
  RtoI()

def Ox():
  DtoI()
  DtoI()
  Ix()
  UtoI()
  UtoI()

def Ox2():
  DtoI()
  DtoI()
  Ix2()
  UtoI()
  UtoI()

def Oxprime():
  DtoI()
  DtoI()
  Ixprime()
  UtoI()
  UtoI()

def Oy():
  DtoI()
  DtoI()
  Iy()
  UtoI()
  UtoI()

def Oy2():
  DtoI()
  DtoI()
  Iy2()
  UtoI()
  UtoI()

def Oyprime():
  DtoI()
  DtoI()
  Iyprime()
  UtoI()
  UtoI()

def Oz():
  DtoI()
  DtoI()
  Iz()
  UtoI()
  UtoI()

def Oz2():
  DtoI()
  DtoI()
  Iz2()
  UtoI()
  UtoI()

def Ozprime():
  DtoI()
  DtoI()
  Izprime()
  UtoI()
  UtoI()

def Bx():
  BtoI()
  Ix()
  FtoI()

def Bx2():
  BtoI()
  Ix2()
  FtoI()

def Bxprime():
  BtoI()
  Ixprime()
  FtoI()

def By():
  BtoI()
  Iy()
  FtoI()

def By2():
  BtoI()
  Iy2()
  FtoI()

def Byprime():
  BtoI()
  Iyprime()
  FtoI()

def Bz():
  BtoI()
  Iz()
  FtoI()

def Bz2():
  BtoI()
  Iz2()
  FtoI()

def Bzprime():
  BtoI()
  Izprime()
  FtoI()




# functions to rotate just the stickers of a certain cell

def cellX(a):
  a[0], a[4], a[6], a[2] = a[4], a[6], a[2], a[0]
  a[1], a[5], a[7], a[3] = a[5], a[7], a[3], a[1]
  return a

def cellXprime(a):
  cellX(a)
  cellX(a)
  cellX(a)
  return a

def cellY(a):
  a[0], a[1], a[4], a[5] = a[4], a[0], a[5], a[1]
  a[2], a[3], a[6], a[7] = a[6], a[2], a[7], a[3]
  return a

def cellYprime(a):
  cellY(a)
  cellY(a)
  cellY(a)
  return a

def cellZ(a):
  cellX(a)
  cellY(a)
  cellXprime(a)
  return a

def cellZprime(a):
  cellX(a)
  cellYprime(a)
  cellXprime(a)
  return a



# code for the scrambling function

def virtScram():
  reset()
  for i in range(50):
    m = random.choice(virtMovesList)
    if m == "Ix":
      Ix()
    elif m == "Ix'":
      Ixprime()
    elif m == "Ix2":
      Ix2()
    elif m == "Iy":
      Iy()
    elif m == "Iy'":
      Iyprime()
    elif m == "Iy2":
      Iy2()
    elif m == "Iz":
      Iz()
    elif m == "Iz'":
      Izprime()
    elif m == "Iz2":
      Iz2()
    elif m == "Ox":
      Ox()
    elif m == "Ox'":
      Oxprime()
    elif m == "Ox2":
      Ox2()
    elif m == "Oy":
      Oy()
    elif m == "Oy'":
      Oyprime()
    elif m == "Oy2":
      Oy2()
    elif m == "Oz":
      Oz()
    elif m == "Oz'":
      Ozprime()
    elif m == "Oz2":
      Oz2()
    elif m == "Rx":
      Rx()
    elif m == "Rx'":
      Rxprime()
    elif m == "Rx2":
      Rx2()
    elif m == "Ry":
      Ry()
    elif m == "Ry'":
      Ryprime()
    elif m == "Ry2":
      Ry2()
    elif m == "Rz":
      Rz()
    elif m == "Rz'":
      Rzprime()
    elif m == "Rz2":
      Rz2()
    elif m == "Lx":
      Lx()
    elif m == "Lx'":
      Lxprime()
    elif m == "Lx2":
      Lx2()
    elif m == "Ly":
      Ly()
    elif m == "Ly'":
      Lyprime()
    elif m == "Ly2":
      Ly2()
    elif m == "Lz":
      Lz()
    elif m == "Lz'":
      Lzprime()
    elif m == "Lz2":
      Lz2()
    elif m == "Fx":
      Fx()
    elif m == "Fx'":
      Fxprime()
    elif m == "Fx2":
      Fx2()
    elif m == "Fy":
      Fy()
    elif m == "Fy'":
      Fyprime()
    elif m == "Fy2":
      Fy2()
    elif m == "Fz":
      Fz()
    elif m == "Fz'":
      Fzprime()
    elif m == "Fz2":
      Fz2()
    elif m == "Bx":
      Bx()
    elif m == "Bx'":
      Bxprime()
    elif m == "Bx2":
      Bx2()
    elif m == "By":
      By()
    elif m == "By'":
      Byprime()
    elif m == "By2":
      By2()
    elif m == "Bz":
      Bz()
    elif m == "Bz'":
      Bzprime()
    elif m == "Bz2":
      Bz2()
    elif m == "Dx":
      Dx()
    elif m == "Dx'":
      Dxprime()
    elif m == "Dx2":
      Dx2()
    elif m == "Dy":
      Dy()
    elif m == "Dy'":
      Dyprime()
    elif m == "Dy2":
      Dy2()
    elif m == "Dz":
      Dz()
    elif m == "Dz'":
      Dzprime()
    elif m == "Dz2":
      Dz2()
    elif m == "Ux":
      Ux()
    elif m == "Ux'":
      Uxprime()
    elif m == "Ux2":
      Ux2()
    elif m == "Uy":
      Uy()
    elif m == "Uy'":
      Uyprime()
    elif m == "Uy2":
      Uy2()
    elif m == "Uz":
      Uz()
    elif m == "Uz'":
      Uzprime()
    elif m == "Uz2":
      Uz2()


def moveFunctions(m):
  if m == "Ix":
    Ix()
  elif m == "Ix'":
    Ixprime()
  elif m == "Ix2":
    Ix2()
  elif m == "Iy":
    Iy()
  elif m == "Iy'":
    Iyprime()
  elif m == "Iy2":
    Iy2()
  elif m == "Iz":
    Iz()
  elif m == "Iz'":
    Izprime()
  elif m == "Iz2":
    Iz2()
  elif m == "Ox":
    Ox()
  elif m == "Ox'":
    Oxprime()
  elif m == "Ox2":
    Ox2()
  elif m == "Oy":
    Oy()
  elif m == "Oy'":
    Oyprime()
  elif m == "Oy2":
    Oy2()
  elif m == "Oz":
    Oz()
  elif m == "Oz'":
    Ozprime()
  elif m == "Oz2":
    Oz2()
  elif m == "Rx":
    Rx()
  elif m == "Rx'":
    Rxprime()
  elif m == "Rx2":
    Rx2()
  elif m == "Ry":
    Ry()
  elif m == "Ry'":
    Ryprime()
  elif m == "Ry2":
    Ry2()
  elif m == "Rz":
    Rz()
  elif m == "Rz'":
    Rzprime()
  elif m == "Rz2":
    Rz2()
  elif m == "Lx":
    Lx()
  elif m == "Lx'":
    Lxprime()
  elif m == "Lx2":
    Lx2()
  elif m == "Ly":
    Ly()
  elif m == "Ly'":
    Lyprime()
  elif m == "Ly2":
    Ly2()
  elif m == "Lz":
    Lz()
  elif m == "Lz'":
    Lzprime()
  elif m == "Lz2":
    Lz2()
  elif m == "Fx":
    Fx()
  elif m == "Fx'":
    Fxprime()
  elif m == "Fx2":
    Fx2()
  elif m == "Fy":
    Fy()
  elif m == "Fy'":
    Fyprime()
  elif m == "Fy2":
    Fy2()
  elif m == "Fz":
    Fz()
  elif m == "Fz'":
    Fzprime()
  elif m == "Fz2":
    Fz2()
  elif m == "Bx":
    Bx()
  elif m == "Bx'":
    Bxprime()
  elif m == "Bx2":
    Bx2()
  elif m == "By":
    By()
  elif m == "By'":
    Byprime()
  elif m == "By2":
    By2()
  elif m == "Bz":
    Bz()
  elif m == "Bz'":
    Bzprime()
  elif m == "Bz2":
    Bz2()
  elif m == "Dx":
    Dx()
  elif m == "Dx'":
    Dxprime()
  elif m == "Dx2":
    Dx2()
  elif m == "Dy":
    Dy()
  elif m == "Dy'":
    Dyprime()
  elif m == "Dy2":
    Dy2()
  elif m == "Dz":
    Dz()
  elif m == "Dz'":
    Dzprime()
  elif m == "Dz2":
    Dz2()
  elif m == "Ux":
    Ux()
  elif m == "Ux'":
    Uxprime()
  elif m == "Ux2":
    Ux2()
  elif m == "Uy":
    Uy()
  elif m == "Uy'":
    Uyprime()
  elif m == "Uy2":
    Uy2()
  elif m == "Uz":
    Uz()
  elif m == "Uz'":
    Uzprime()
  elif m == "Uz2":
    Uz2()