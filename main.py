import discord
import os

import phys2222
import stickers
import twisty_stacky
import text
import wiki

from keep_alive import keep_alive

client = discord.Client()
@client.event

# sends a message when the bot is logged in to the console
async def on_ready():
    print('{0.user}'.format(client)+' has logged in')
@client.event

# called when any message is sent
async def on_message(message):
  move = message.content[1:]
  if message.content.startswith("&"):
    if message.content.startswith("&commands"):
      await text.command_text(message)
      
    elif message.content.startswith("&funfact"):
      await (text.fun_fact(message))
      
    elif message.content.startswith("&help"):
      stickers.reset()
      #await stickers.sticker_board(message, "Solved")
      await text.help_text(message)
      
    # shows the current state of the 2^4 simulator
    elif message.content.startswith("&2^4"):
      await stickers.sticker_board(message, "2^4")
      
    # resets the puzzle to the solved state
    elif message.content.startswith("&reset"):
      stickers.reset()
      await stickers.sticker_board(message, "Reset")
      
    # begins the 3d rotations of the puzzle
    elif message.content.startswith("&y"):
      if message.content.startswith("&y'"):
        stickers.yprimerotation()
      elif message.content.startswith("&y2"):
        stickers.y2rotation()
      else:
        stickers.yrotation()
      await stickers.sticker_board(message, move)
    elif message.content.startswith("&z"):
      if message.content.startswith("&z'"):
        stickers.zprimerotation()
      elif message.content.startswith("&z2"):
        stickers.z2rotation()
      else:
        stickers.zrotation()
      await stickers.stickers.sticker_board(message, move)
    elif message.content.startswith("&x"):
      if message.content.startswith("&x'"):
        stickers.xprimerotation()
      elif message.content.startswith("&x2"):
        stickers.x2rotation()
      else:
        stickers.xrotation()
      await stickers.sticker_board(message, move)
    elif message.content.startswith("&U-I"):
      if message.content.startswith("&U-I2"):
        stickers.UtoI2()
      else:
        stickers.UtoI()
      await stickers.sticker_board(message, move)
    elif message.content.startswith("&D-I"):
      if message.content.startswith("&D-I2"):
        stickers.UtoI2()
      else:
        stickers.DtoI()
      await stickers.sticker_board(message, move)
    elif message.content.startswith("&F-I"):
      if message.content.startswith("&F-I2"):
        stickers.FtoI2()
      else:
        stickers.FtoI()
      await stickers.sticker_board(message, move)
    elif message.content.startswith("&B-I"):
      if message.content.startswith("&B-I2"):
        stickers.FtoI2()
      else:
        stickers.BtoI()
      await stickers.sticker_board(message, move)
    elif message.content.startswith("&R-I"):
      if message.content.startswith("&R-I2"):
        stickers.RtoI2()
      else:
        stickers.RtoI()
      await stickers.sticker_board(message, move)
    elif message.content.startswith("&L-I"):
      if message.content.startswith("&L-I2"):
        stickers.RtoI2()
      else:
        stickers.LtoI()
      await stickers.sticker_board(message, move)
    #if the message starts with &[any of the cell letters]
    elif message.content.startswith("&I") or message.content.startswith("&O") or message.content.startswith("&R") or message.content.startswith("&L") or message.content.startswith("&F") or message.content.startswith("&B") or message.content.startswith("&D") or message.content.startswith("&U"):
      # m = message.content
      # sets m = message w&0 the &
      m = move
      #if there is a comma in m (multiple moves)
      if "," in m:
        # noco counts how many commas there are
        noco = m.count(",")
        # for loop that runs however many commas there are times
        for i in range(noco+1):
          # result is the index of where the first comma is
          result = m.find(",")
          if result == -1:
            result = len(m)+1
          print("i = " + str(i))
          print("number of commas = " + str(noco))
          noco = noco - 1
          print("result = " + str(result))
          stickers.moveFunctions(m[0:result])
          print("moveFunctions(" + str(m[0:result]) + ")")
          m = m[result+1:]
          print("m = " + str(m))
      else:
        stickers.moveFunctions(m)
      await stickers.sticker_board(message, move)
      
    # scrambles the virtual 2^4
    elif message.content.startswith("&vs"):
      stickers.virtScram()
      await stickers.sticker_board(message, move)
      
    # sends a physical 2^4 scramble
    elif message.content.startswith("&ps"):
      numbir = message.content
      numberOfScrambles = numbir[3:]
      if len(numberOfScrambles) == 0:
        numberOfScrambles = "1"
      await phys2222.generatephysscram(numberOfScrambles, message)

    # sends a twisty stacky scramble
    elif message.content.startswith("&tss"):
      numbir = message.content
      numberOfScrambles = numbir[4:]
      if len(numberOfScrambles) == 0:
        numberOfScrambles = 1
      await message.channel.send(twisty_stacky.scramble(numberOfScrambles))


    # wiki codes
    elif message.content.startswith("&wiki"):
      if message.content.startswith("&wiki random"):
        await (wiki.random_page(message))
      else:
        await (wiki.search(message, message.content[5:]))

      
    
      
      # if none of the above statements were true, do this
    else:
      await message.channel.send("<:hypergun:902608227139731496>")


# connects this code to the bot by using the bot's token
keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
