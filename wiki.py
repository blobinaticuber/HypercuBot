import discord
import random
import requests
from bs4 import BeautifulSoup


async def random_page(message):
  # gets a random page from the array of pages
  page = "http://wiki.superliminal.com/wiki/Special:Random"
  webpage = requests.get(page)
  doc = BeautifulSoup(webpage.text, "html.parser")
  doctitle = doc.title
  doctext = doc.find_all("p")
  
  #reformats the ending of the url
  urla = doctitle.string
  urla = urla.replace(" ", "_")
  urla = urla.replace("^", "%5E")
  urla = urla[0:len(urla)-20]
  
  #finds the first <img tag in the HTML
  image = doc.img
  #prints the contents in the <img tag
  print(image)
  source = image.get("src")
  print(source)

  wiki_embed=discord.Embed(title=doctitle.string, color=0xff8012, description=doctext[0].string, url = "http://wiki.superliminal.com/wiki/" + urla)
  wiki_embed.set_thumbnail(url = "http://wiki.superliminal.com" + source)
  await message.channel.send(embed = wiki_embed)


async def search(message, search):
  # gets a random page from the array of pages
  #search = search.replace(" ", "_")
  #search = search.replace("^", "%5E")
  page = "http://wiki.superliminal.com/index.php?title=Special%3ASearch&search=" + search + "&go=Go"
  webpage = requests.get(page)
  doc = BeautifulSoup(webpage.text, "html.parser")
  doctitle = doc.title
  doctext = doc.find_all("p")
  
  #reformats the ending of the url
  urla = doctitle.string
  urla = urla.replace(" ", "_")
  urla = urla.replace("^", "%5E")
  urla = urla[0:len(urla)-20]
  
  #finds the first <img tag in the HTML
  image = doc.img
  #prints the contents in the <img tag
  print(image)
  source = image.get("src")
  print(source)

  wiki_embed=discord.Embed(title=doctitle.string, color=0xff8012, description=doctext[0].string, url = "http://wiki.superliminal.com/wiki/" + urla)
  wiki_embed.set_thumbnail(url = "http://wiki.superliminal.com" + source)
  await message.channel.send(embed = wiki_embed)