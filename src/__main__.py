import asyncio
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(
        'We are:\n'
        f'Username: {client.user.name!r}\n'
        f'ID: {client.user.id}'
    )

@client.event
async def on_message(message):
    reactgot = [
        '<:got666:1370384342957953105>',
        '<:got17:1370384315111964672>',
        '<:gotsip:1370384287861440573>',
        '<:gotjudged:1370384259931443252>',
        '<:gotdavid:1370384225295011932>',
        '<:gotblast:1370384200976433232>',
        '<:got9:1370384162925838427>',
        '<:got2:1370384127819382864>',
        '<:gotlurk:1370384100908597269>',
        '<:gotstare:1370384073746550835>',
        '<:gotdamned:1370384042024763572>',
        '<:gotenough:1370384012069044336>',
        '<:gotwtf:1370383982251868160>',
        '<:got:1370383947795533976>']
    
    truegot = [
        '<got666:1137419671570747554>',
        '<got17:1296102708993982516>',
        '<gotsip:979065494508286053>',
        '<gotjudged:1001592848862421083>',
        '<gotdavid:1005132112753594408>',
        '<gotblast:1096080392999665745>',
        '<got9:997269024595521557>',
        '<got2:962520319795556402>',
        '<gotlurk:974758117113987163>',
        '<gotstare:958064790180360283>',
        '<gotdamned:993552515025096714>',
        '<gotenough:960565590085480458>',
        '<gotwtf:922546697350053908>',
        '<got:960624295359438878>'
    ]

    reactdamn = random.choice(reactgot)

    if message.author == client.user:
        return

    if 'got' in message.content.lower():
        # reacts with a random got emoji when any message contains any possible "got"

        print(f'got detected: {message.content}\n'
        f'reacting: {reactdamn}'
        )

        await message.add_reaction(f'{reactdamn}')

    if client.user.mentioned_in(message):
        # responds with a random got emoji when a message mentions the gotbot

        print(f'got mentioned: {message.content}\n'
              f'posting: {reactdamn}'
              )
        
        await message.channel.send(f'{reactdamn}')

    if message.content in truegot:
        # mimics a got when any message is just a got emoji

        print(f'got spotted: {message.content}\n'
              f'copying: {message.content}'
              )
        
        await message.channel.send(f'{message.content}')

if __name__ == "__main__":
    # Load the .env vars
    load_dotenv()

    try:
        token = os.environ['TOKEN']
    except KeyError:
        raise KeyError("Environment variable 'TOKEN' is not set. Have you created a .env file?")
    client.run(token)