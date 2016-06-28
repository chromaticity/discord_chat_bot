# discord chat bot
# by: brandon lol

import discord
from discord.ext import commands
import random
from random import randint

bot = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(bot.is_logged_in)
    print('------')

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


bot.run('MTk2ODM0OTA4MzEwNzMyODAw.ClNU7A.LJ5RHATx2ZS1lUtwcKXdB9galUE')