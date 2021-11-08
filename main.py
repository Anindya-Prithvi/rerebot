import os
import discord
import re
import asyncio
import random
from dotenv import load_dotenv
from assets.processor import process
from discord.ext import tasks


load_dotenv()
token = os.getenv("token")
client = discord.Client()
tasklist = asyncio.Queue()
customerservice = []



@client.event
async def on_ready():
    # print when bot starts up
    print(f"{client.user} has connected to discord")

@tasks.loop(seconds=1)
async def queryhandler():
    global tasklist
    if(tasklist.qsize()!=0):
        a = await tasklist.get()
        print(a)
        retval = await a
        tasklist.task_done()
        if((retval==0) or (retval==None)):
            print("Task done")
        else:
            print("Very rare <report incident>!")
    else:
        delhashes=[]
        for i in customerservice:
            with open("messages/"+str(hash(i)),"r") as f:
                if (fst:=f.read(1))==chr(0):
                    pass
                else:
                    reply = f.read(-1)
                    customerservice.remove(i)
                    await i.channel.send("<@"+str(i.author.id)+"> "+fst+reply)
                    delhashes.append('messages/'+str(hash(i)))
        for i in delhashes:
            os.remove(i)




@client.event
async def on_message(message):
    async def helper(smth):
        # await asyncio.sleep(3)
        await process(smth)

    global tasklist
    if message.author == client.user:
        return
    # if message.content == "start":
    #     await message.channel.send(",rr echo hi")
    #     await message.channel.send(",rr echo hi")
    #     await message.channel.send(",rr echo hi")
    #     await message.channel.send(",rr echo hi")
    #     await message.channel.send(",rr echo emoji 906832046721216552")
    #     await message.channel.send(",rr addfile -name henlo -content blabla")
    #     await message.channel.send(",rr showfiles")
    #     await message.channel.send(",rr showfile -name henlo")
    #     await message.channel.send(",rr bored diy")
    #     await message.channel.send(",rr bored recreational")
    #     await message.channel.send(",rr echo hi")
    #     await message.channel.send(",rr echo hi")
    #     await message.channel.send(",rr echo hi")
    #     await message.channel.send(",rr echo emoji 906832046721216552")
    #     await message.channel.send(",rr addfile -name henlo -content blabla")
    #     await message.channel.send(",rr addfile -name henlo -content blabla")
    #     await message.channel.send(",rr showfiles")
    #     await message.channel.send(",rr echo hi")
    #     await message.channel.send(",rr echo hi")
    #     await message.channel.send(",rr showfile -name henlo")
    #     await message.channel.send(",rr bored diy")
    #     await message.channel.send(",rr bored recreational")
    #     await message.channel.send(",rr showfiles")
    #     await message.channel.send(",rr echo hi")
    #     await message.channel.send(",rr echo hi")
    #     await message.channel.send(",rr showfiles")
    #     await message.channel.send(",rr showfile -name henlo")
    #     await message.channel.send(",rr bored diy")
    #     await message.channel.send(",rr bored recreational")
    #     await message.channel.send(",rr echo hi")
    #     await message.channel.send(",rr echo emoji 906832046721216552")
    #     await message.channel.send(",rr addfile -name henlo -content blabla")
    #     await message.channel.send(",rr addfile -name henlo -content blabla")
    #     await message.channel.send(",rr showfiles")
    #     await message.channel.send(",rr echo hi")
    #     await message.channel.send(",rr echo PROGRAM END")
    elif message.content == "killbot!":
        print("Kill command")
        if str(message.author) == "Yourname#1111":
            # maybe add a prompt to get username of botrunner
            await message.channel.send(
                "I am being destroyed by " + str(message.author) + ". Adios..."
            )
            print("killing")
            exit(0)

    elif re.match(",rr ownerchat", message.content):
        # will expect owner to write on console
        print(message.content[14:])
        await message.channel.send("Message has been sent, you will be mentioned on the reply :smile:")
        with open("messages/"+str(hash(message)),"w") as f:
            f.write(chr(0)+str(message.content[4:])+" by "+str(message.author))
        customerservice.append(message)

    elif message.content[:4] == ",rr ":
        message.content = message.content[4:]
        #PQ cant handle duplival lmao
        await tasklist.put(helper(message))

    else:
        print("message intercepted but not for me")

async def replyboss(message):
    print("trying")
    with open("messages/"+str(hash(message)),"r") as f:
        if (fst:=f.read(1))==chr(0):
            return message
        else:
            reply = f.read(-1)
            await message.channel.send("<@"+str(message.author.id)+"> "+fst+reply)
    os.remove(str(hash(message)))
    return 0

queryhandler.start()
client.run(token)
