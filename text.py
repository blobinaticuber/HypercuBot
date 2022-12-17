import random
import discord

from PIL import Image

with open('funFacts.txt') as f:
  lines = f.readlines()
  funLength = len(lines)

command_names = ["**&funfact:**", "**&help:**", "**&ps:**", "**&tss:**", "**&wiki random**", "&wiki (search)"]
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

async def fun_fact(message):
  fact_embed = discord.Embed(title="Fun Fact", color=0xff00ff, description=lines[random.randint(0,funLength)] )
  await message.channel.send(embed = fact_embed)
  