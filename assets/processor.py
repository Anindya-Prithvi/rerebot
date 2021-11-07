import re

async def process(message):
    if message.content == "!!help":
        await message.channel.send("""Here is the list of my commands: 
```md
1. echo <your message here> : This command echoes your message
2. addfile -name <enter-filename> -content <enter-content>: Writes the file on host machine
3. showfiles: Lists all files on the host machine
4. showfile -name <filename>: Shows the content of that file
5. echo emoji <number>: sends the emoji with the corresponding number
...more coming soon!
```""")
    elif re.match("echo emoji [0-9]+",message.content):
        #possibly read from file
        getemoji = "<:panda_heart:"+message.content.split()[2]+">"
        await message.channel.send(getemoji)    
    elif re.match("echo .+",message.content):
        await message.channel.send(message.content[5:])
        await message.add_reaction('\N{THUMBS UP SIGN}')
    elif re.match("addfile -name .+ -content .+", message.content):
        if (len(os.listdir("userdir"))>50):
            await message.channel.send("This utility is blocked due to large amount of files")
            return
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
            if len(buffer)==500: buffer = buffer + "\n...and so on"
            await message.channel.send("```\n"+buffer+"```")
        except OSError:
            await message.channel.send("No such file found.")