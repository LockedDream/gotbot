import asyncio
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='ef9359e4d2422d95ec40b9742d312d14374734b1',intents=intents)

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
    '<:got666:1137419671570747554>',
    '<:got17:1296102708993982516>',
    '<:gotsip:979065494508286053>',
    '<:gotjudged:1001592848862421083>',
    '<:gotdavid:1005132112753594408>',
    '<:gotblast:1096080392999665745>',
    '<:got9:997269024595521557>',
    '<:got2:962520319795556402>',
    '<:gotlurk:974758117113987163>',
    '<:gotstare:958064790180360283>',
    '<:gotdamned:993552515025096714>',
    '<:gotenough:960565590085480458>',
    '<:gotwtf:922546697350053908>',
    '<:got:960624295359438878>',
    '<a:gotdamn:1374358305962594304>']

@bot.event
async def on_ready():
    print(
        'We are:\n'
        f'Username: {bot.user.name!r}\n'
        f'ID: {bot.user.id}'
    )

@bot.event
async def on_message(message):
    from src.got_lib import thisgotexists

    if message.author == bot.user:
        return
    
    if bot.user.mentioned_in(message):
        # responds with a random got image when a message mentions the gotbot
        librarydamn = random.choice(thisgotexists)

        print(f'got mentioned: {message.content}\n'
              f'posting: {librarydamn}'
              )
        
        await message.channel.send(f'{librarydamn}')

    elif message.content in truegot:
        # mimics a got when any message is just a got emoji

        print(f'got spotted: {message.content}\n'
              f'copying: {message.content}'
              )
        
        await message.channel.send(f'{message.content}')

    elif 'got' in message.content.lower():
        # reacts with a random got emoji when any message contains any possible "got"
        reactdamn = random.choice(reactgot)

        print(f'got detected: {message.content}\n'
        f'reacting: {reactdamn}'
        )

        await message.add_reaction(f'{reactdamn}')

    elif random.randint(0,65535) < 1:
        # exceedingly rare chance to post a specific got image

        print(f'exceedingly rare got spawned\n'
              f'posting gotdamnsaid'
              )

        await message.channel.send("https://cdn.discordapp.com/attachments/876964859353378896/1372214065824268288/gotdamsaid.png")

@bot.tree.context_menu(name='gotbomb')
async def gotbomb(interaction: discord.Interaction, message: discord.Message):
    """
    Bombs the given message with gots

    https://github.com/64andy
    """
    # All commands need a response, otherwise Discord thinks it failed
    await interaction.response.send_message("got damn!!!",
                                            ephemeral=True, delete_after=1.0
    )
    # Randomise the reaction order
    gotdeck = reactgot.copy()
    random.shuffle(gotdeck)
    
    # 1/20 chance of playing the special gotdamn
    raregot = (random.randint(0, 19) == 0)
    if raregot:
        await message.add_reaction('<a:gotdamn:1374358305962594304>')
    else:
        for got in gotdeck:
            await message.add_reaction(got)
            await asyncio.sleep(0.3)    # Helps mitigate rate-limiting

if __name__ == "__main__":
    # Load the .env vars
    load_dotenv()

    try:
        token = os.environ['TOKEN']
    except KeyError:
        raise KeyError("Environment variable 'TOKEN' is not set. Have you created a .env file?")
    bot.run(token)