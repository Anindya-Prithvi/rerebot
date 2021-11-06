import os
import discord
import re
from dotenv import load_dotenv

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
    elif re.match("echo .+",message.content):
        await message.channel.send(message.content[5:])
    elif re.match("addfile -name .+ -content .+", message.content):
        breakit = message.content.split(" -")
        if len(breakit[1])>50:
            await message.channel.send("Filename is big, please reconsider.")
            return
        if re.match("\/\.\.", breakit[1]):
            await message.channel.send("No sneaky sneaky :)")
            return
        #addfile, name something, content something else
        try:
            thedir = "userdir/"
            f=open(thedir+breakit[1][5:], 'a') #no overwriting stuff :)
            f.write(breakit[2][8:])
            f.close()
            await message.channel.send("File written successfully!")
        except OSError:
            await message.channel.send("Could not create file. Possible invalid name")
            return
    elif message.content=="showfiles":
        tosend = "```py\nHere are some files and folders I know of:\n"
        for i,f in enumerate(os.listdir("userdir")):
            if i>30:
                tosend = tosend+"\nAnd some more..."
                break
            tosend = tosend+f"{i+1}. {f}\n"
        tosend = tosend+"\n```"        
        await message.channel.send(tosend)
    elif re.match("showfile -name .+",message.content):
        try:
            f = open(f"userdir/{message.content[15:]}","r")
            buffer = f.read(500)
            await message.channel.send("```\n"+buffer+"```")
        except OSError:
            await message.channel.send("No such file found.")
            

client.run(token)
