# discord chat bot
# by: brandon lol

import discord
from discord.ext import commands
import random
from random import randint
import spotipy
import spotipy.util as util
import sys

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
    elif message.content.startswith('!toptracks'):
        # remember that you need to export the client id and all that other shit to the server...
        # as env variables
        # like so: 
        token = util.prompt_for_user_token("chroma_0", "user-top-read")

        if token:
            sp = spotipy.Spotify(auth=token)
            results = sp.current_user_top_tracks(limit=5)
            for item in results['items']:
                track = item['name']
                artist = item['artists'][0]['name']
                # print(track['name'] + ' - ' + track['artists'][0]['name'])
                await bot.send_message(message.channel, "Brandon's Top 5 Tracks - Time Period: Whenever")
                await bot.send_message(message.channel, track + " - " + artist)
        else:
            print("Can't get token for", username)


bot.run('')