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

    reactdamn = random.choice(reactgot)

    if message.author == client.user:
        return

    if 'got' in message.content.lower():

        print('got detected\n'
        f'tried {reactdamn}'
        )

        await message.add_reaction(f'{reactdamn}')


if __name__ == "__main__":
    # Load the .env vars
    load_dotenv()

    # Add the cogs
    # asyncio.run(add_all_cogs(bot))

    try:
        token = os.environ['TOKEN']
    except KeyError:
        raise KeyError("Environment variable 'TOKEN' is not set. Have you created a .env file?")
    client.run(token)