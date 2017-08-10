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
    global voiceclient
    if message.content.startswith('!foo'):
        await bot.send_message(message.channel, 'foo')
        print("message channel", message.channel)

    if "love me" in message.content.lower():
        voiceclient = await bot.join_voice_channel(message.author.voice.voice_channel)
        await asyncio.sleep(.3)
        player = voiceclient.create_ffmpeg_player('nico.mp3', after=done_playing)
        player.start()

    if "im a weeb" in message.content.lower():
        voiceclient = await bot.join_voice_channel(message.author.voice.voice_channel)
        await asyncio.sleep(.3)
        player = voiceclient.create_ffmpeg_player('sadoaiya.wav', after=done_playing)
        player.start()
        
    if "bird migration" in message.content.lower():
        voiceclient = await bot.join_voice_channel(message.author.voice.voice_channel)
        await asyncio.sleep(.3)
        player = voiceclient.create_ffmpeg_player('birdmigration.wav', after=done_playing)
        player.start()
        
    if "ipod" in message.content.lower():
        voiceclient = await bot.join_voice_channel(message.author.voice.voice_channel)
        await asyncio.sleep(.3)
        player = voiceclient.create_ffmpeg_player('ipod.wav', after=done_playing)
        player.start()
        
    if "hol' up" in message.content.lower():
        voiceclient = await bot.join_voice_channel(message.author.voice.voice_channel)
        await asyncio.sleep(.3)
        player = voiceclient.create_ffmpeg_player('hol\' up.wav', after=done_playing)
        player.start() 
        
    if "you are like a little baby" in message.content.lower():
        voiceclient = await bot.join_voice_channel(message.author.voice.voice_channel)
        await asyncio.sleep(.3)
        player = voiceclient.create_ffmpeg_player('you are like a little baby.wav', after=done_playing)
        player.start() 
        
    if message.content.startswith('!leave'):
        await voiceclient.disconnect()
        print("disconnect")

    if message.content.startswith('shh'):
        print("done")

def done_playing():
    bot.loop.create_task(voiceclient.disconnect())

bot.run(sys.argv[1])
