import os
import sys
from getEvents import *
import discord
from dotenv import load_dotenv


TOKEN = "REDUCTED"

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "e":
        print(str(message.author)+" asked "+ message.content)
        await message.delete()
    if message.content.startswith('e'):
        await message.channel.send(getNextEvent())
    if message.content == "r":
        print(str(message.author)+" asked "+message.content)
        await message.delete()
    if message.content.startswith('r'):
        await message.channel.send(getRanked())
    

   
    if (message.content.startswith('$') == True):
        if(message.content == "$help"):
            
            print(str(message.author)+" asked "+message.content)
            await message.delete()
            await message.channel.send(getHelp())
        else:
            print(str(message.author)+" asked "+message.content)
            await message.channel.send(getSpecificEvent(message.content))
            await message.delete()
    
client.run(TOKEN)
