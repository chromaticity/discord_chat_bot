# discord chat bot
# by: brandon lol
# APIs: discord.py, spotipy8

import discord
from discord.ext import commands
import random
from random import randint
import sys
import os

bot = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(bot.is_logged_in)
    print('------')
    bot.change_presence(game=discord.Game(name="Python 3.5.2"), status=None, afk=False)

@bot.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await bot.send_message(message.channel, 'Calculating messages...')
        async for log in bot.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await bot.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await bot.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!roulette'):
        tmpArr = [];
        for server in bot.servers:
            for member in server.members:
                tmpArr.append(member)
        arrInd = len(tmpArr)
        randInd = randint(0, arrInd - 1)
        targetedUser = tmpArr[randInd]
        formattedUser = str(targetedUser).split("#")[0]
        await bot.send_message(message.channel, "BANG BANG!!!! {} is dead!".format(formattedUser))

    elif message.content.startswith('!funfact'):
        # update this array
        funFacts = ["Fun Fact: McIlhenny loves Perl.", "Fun Fact: CSUN is fucking garbage", "Fun Fact: Rafi taught me how 2 hack", 
        "Fun Fact: My nuts itch", "Fun Fact: Rafa told me to make up shit for these facts", "Fun Fact: Dat Dao taught me literally everything for this major, I can drop out now if I fucking want to.", 
        "Fun Fact: Dwayne Pascua's nickname is Dwayne Pascua", "Fun Fact: It's time to kick ass and display fun facts, and I'm all out of fun facts", 
        "Fun Fact: HE DINDU NUFFIN", "Fun Fact: NippleShredder says 'Saw Dewd'", "Fun Fact: Nikolai thinks he shoulda done drugs and used his dick suckin mouth for big money and not perm numbers", 
        "Fun Fact: You can use the !funfact command to throw out fun facts", "Fun Fact: The Mitochondria is the powerhouse of the cell"]

        ffArrInd = len(funFacts)
        randNum = randint(0, ffArrInd - 1)
        funFact = funFacts[randNum]
        # print fun fact i guess
        await bot.send_message(message.channel, funFact)
   
    elif message.content.startswith('!starttheparty'):
        os.system("cd /bots/discord_chat_bot && python3.5 run.py &");

# get this api key from discord's site when you're logged in...
bot.run('MjI4OTQwNjM2NDE2Mzc2ODQz.C19CxQ.BBA7kvgPuUkP-kqH8rzX0jZ71k4')
