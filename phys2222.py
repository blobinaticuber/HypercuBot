import random
import discord

scrambleLength = [8, 10, 12]
Lphysmoves = ["Ly", "Ly'", "Ly2", "Lx2", "Lz2", "Lx2,y", "Lx2,y'", "Lx", "Lx,y", "Lx,y'", "Lx,y2", "Lx'", "Lx',y", "Lx',y'", "Lx',y2", "Lz", "Lz,y", "Lz,y'", "Lz,y2", "Lz'", "Lz',y", "Lz',y'", "Lz',y2", ""]
Rphysmoves = ["Ry", "Ry'", "Ry2", "Rx2", "Rz2", "Rx2,y", "Rx2,y'", "Rx", "Rx,y", "Rx,y'", "Rx,y2", "Rx'", "Rx',y", "Rx',y'", "Rx',y2", "Rz", "Rz,y", "Rz,y'", "Rz,y2", "Rz'", "Rz',y", "Rz',y'", "Rz',y2", ""]

# generates a phys 2^4 scramble by calling random moves
async def generatephysscram(n, message):
  message_text = ""
  for j in range(int(n)):
    # prints line numbers for multi scramble input into csTimer
    message_text += "\n" + str(j+1) + ". "
    for i in range(random.choice(scrambleLength)):
      rand = random.choice(Lphysmoves)
      rand2 = random.choice(Rphysmoves)
      message_text += rand + " " + rand2 + " # "
  if n == "1":
    text = " Physical 2x2x2x2 Scramble:"
  else:
    text = " Physical 2x2x2x2 Scrambles:"
  scramble_embed=discord.Embed(title=n+text, color=0xff0000, description=message_text)
  
  await message.channel.send(embed=scramble_embed)