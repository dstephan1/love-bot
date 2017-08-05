import discord
import asyncio
import sys

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

    if "love me" in message.content.lower():
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

def done_playing():
    bot.loop.create_task(voiceclient.disconnect())

bot.run(sys.argv[1])
