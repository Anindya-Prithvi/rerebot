import os
import discord
import re
from dotenv import load_dotenv
from assets.processor import process

load_dotenv()
token = os.getenv("token")
client = discord.Client()

@client.event
async def on_ready():
    #print when bot starts up
    print(f"{client.user} has connected to discord")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content == "killbot!":
        print("Kill command")
        if str(message.author) == "Yourname#1111":
            #maybe add a prompt to get username of botrunner
            await message.channel.send("I am being destroyed by "+str(message.author)+". Adios...")
            print("killing")
            exit(0)
    elif message.content[:4] == ",rr ":
        message.content = message.content[4:]
        await process(message)
    else:
        print("message intercepted but not for me")
            

client.run(token)
