import discord
import asyncio
import sys

from discord.ext.commands import Bot

bot = discord.Client()
if not discord.opus.is_loaded():
    print("manual load opus?")
    discord.opus.load_opus('opus')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if message.content.startswith('!foo'):
        await bot.send_message(message.channel, 'foo')
        print("message channel", message.channel)

    if "LOVE ME" in message.content:
        global voiceclient
        voiceclient = await bot.join_voice_channel(message.author.voice.voice_channel)
        await asyncio.sleep(.3)
        player = voiceclient.create_ffmpeg_player('nico.mp3', after=done_playing)
        player.start()

    if message.content.startswith('!leave'):
        await voiceclient.disconnect()
        print("disconnect")

    if message.content.startswith('shh'):
        print("done")


def play_sound():
    player = voiceclient.create_ffmpeg_player('nico.mp3', after=done_playing)
    player.start()

def done_playing():
    bot.loop.create_task(voiceclient.disconnect())

bot.run(sys.argv[1])

# client = discord.Client()

# @client.event
# async def on_ready():
#     print('Logged in as')
#     print(client.user.name)
#     print(client.user.id)
#     print('------')

# @client.event
# async def on_message(message):
#     if message.content.startswith('!test'):
#         counter = 0
#         tmp = await client.send_message(message.channel, 'Calculating messages...')
#         async for log in client.logs_from(message.channel, limit=100):
#             if log.author == message.author:
#                 counter += 1

#         await client.edit_message(tmp, 'You have {} messages.'.format(counter))
#     elif message.content.startswith('!sleep'):
#         await asyncio.sleep(5)
#         await client.send_message(message.channel, 'Done sleeping')

# client.run('token')