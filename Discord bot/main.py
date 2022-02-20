import discord
import os
import requests
import json
import random

client = discord.Client()

bad_words = ["darn", "crap", "dagnabbit", "son of a monkey", "bullspit"]

starter_response = [
  "chill out",
  "ʷᵃᵗᶜʰ ʸᵒᵘʳ ᵖʳᵒᶠᵃⁿⁱᵗʸ",
  "watch your language, young man."
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send('wassup wit it')

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in message.content for word in bad_words):
    await message.channel.send(random.choice(starter_response))


client.run(os.environ['TOKEN'])