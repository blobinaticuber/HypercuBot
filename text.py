import random
import discord

from PIL import Image

randomfacts = ["The 3x3x3x3 has 216 stickers", "The 4D Rubik's Cube has 8 sides", "In 4D, an edge piece has 3 colours, and can be twisted in 6 ways instead of 2", "In 4D, a corner piece has 4 colours, and can be twisted in 12 ways instead of 3", "In 4D, twisting a side is like rotating a whole cube instead of just turning a square", "The formula to calculate the number of states for the 3x3x3x3 is (24!x32!)&2 x 16!&2 x 2^23 x (3!)^31 x 3 x (4!&2)^15 x 4", "To write 3x3x3x3 shorter, you can use an exponent like 3^4", "MC4D is a program that lets you play with 4-dimensional twisty puzzles", "The 3x3x3x3 has 8 1-coloured pieces, 24 2-coloured pieces, 32 3-coloured pieces, and 16 4-coloured pieces", "The speedsolving world record for the 3x3x3x3 is 10:11 by Tetrian22", "The FMC world record for the 3x3x3x3 is 211 twists with no computer help, by Charles Doan", "Melinda's Physical 2x2x2x2 is a real puzzle that you can play with that works just like a 2x2x2x2", "The 4th dimension in MC4D is represented as inwards vs outwards due to the projection", "Many standard 3x3x3 methods can be scaled up and used on the 3x3x3x3", "The speedsolving world record for Melinda's Physical 2x2x2x2 is 1:06.04 by Grant S"]

command_names = ["**&randomfact:**", "**&help:**", "**&ps:**", "**&tss:**", "**&wiki random**", "&wiki (search)"]
command_values = ["Tells you a random fact about hypercubes", "Help for the Discord virtual 2^4 simulator", "Generates a physical 2^4 scramble. The # means to do a U2, then stack the left endcap to the right. Type a number after the s to make it generate multiple scrambles. You can then import that list into csTimer.", "Generates a scramble for the Twisty Stacky 2^3 minipuzzle. % means to stack that side to the opposite side. Type a number after the s to make it generate multiple scrambles. You can then import that list into csTimer.", "Load a random Superliminal Wiki page", "Search for a page on the Superliminal Wiki"]

help_names = ["**Cell rotations**", "**3D rotations**", "**4D rotations**", "**Scramble**", "**Reset to solved**", "**Backup the current state**", "**Load from a backup**", "**&2^4**"]
help_values = ["&(cell)(x,y,z)(' or 2)", "&(x,y,z)(' or 2)", "&(cell)-I", "&vs", "&reset", "&backup", "&load(paste backup here)", "show the current puzzle state"]

async def command_text(message):
  command_embed=discord.Embed(title="Commands", color=0xffff00)
  for i in range(len(command_names)):
    command_embed.add_field(name=command_names[i], value=command_values[i], inline=False)
  await message.channel.send(embed = command_embed)
  
  
async def help_text(message):
  help_embed=discord.Embed(title="Help", color=0x00ffff)
  for i in range(len(help_names)):
    help_embed.add_field(name=help_names[i], value=help_values[i], inline=False)
  await message.channel.send(embed = help_embed)

async def random_fact(message):
  fact_embed=discord.Embed(title="Ramdom Fact", color=0xff00ff, description=random.choice(randomfacts))
  await message.channel.send(embed = fact_embed)
  