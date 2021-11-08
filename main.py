import os
import discord
import re
import asyncio
import random
from dotenv import load_dotenv
from assets.processor import process


load_dotenv()
token = os.getenv("token")
client = discord.Client()
tasklist = asyncio.PriorityQueue()
cmd_cnt = 0


@client.event
async def on_ready():
    # print when bot starts up
    print(f"{client.user} has connected to discord")


@client.event
async def on_message(message):
    async def helper(smth):
        # await asyncio.sleep(3)
        await process(smth)

    global tasklist
    global cmd_cnt
    cmd_cnt += 1
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
    elif message.content[:4] == ",rr ":
        message.content = message.content[4:]
        await tasklist.put((random.randint(1, 30), helper(message)))
        a = await tasklist.get()
        print(tasklist)
        await a[1]
        tasklist.task_done()

    else:
        print("message intercepted but not for me")


client.run(token)
