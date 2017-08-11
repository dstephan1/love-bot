import discord
import asyncio
import sys

from Soundboard import Soundboard

class SoundboardPlayer(discord.voice_client.StreamPlayer):
    def __init__(self, client, soundboard, after, **kwargs):
        super().__init__(soundboard, client.encoder,
                         client._connected, client.play_audio, after, **kwargs)
    def run(self):
        super().run()

if not discord.opus.is_loaded():
    print("manual load opus?")
    discord.opus.load_opus('opus')

# globals
soundboard = Soundboard()
voiceclient = None
player = None
bot = discord.Client()

async def play_sound(voicechannel, sound):
    global voiceclient
    global player
    global soundboard

    new_soundboard = False

    if not voiceclient or not voiceclient.is_connected():
        print("no voice client")

        if not voicechannel:
            print("message author is not in a channel")
            return
        voiceclient = await bot.join_voice_channel(voicechannel)
        new_soundboard = True
 
    if not player or player.is_done():
        new_soundboard = True

    # load the sound into the soundboard
    soundboard.load(sound)

    if new_soundboard:
        player = SoundboardPlayer(voiceclient, soundboard, after=done_playing)
        player.start()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    global voiceclient

    voicechannel = message.author.voice.voice_channel

    if message.content.startswith('!foo'):
        await bot.send_message(message.channel, 'foo')
        print("message channel", message.channel)

    if "love me" in message.content.lower():
        await play_sound(voicechannel, 'nico.mp3')

    if "im a weeb" in message.content.lower():
        await play_sound(voicechannel, 'sadoaiya.wav')
        
    if "bird migration" in message.content.lower():
        await play_sound(voicechannel, 'birdmigration.wav')
        
    if "ipod" in message.content.lower():
        await play_sound(voicechannel, 'ipod.wav')
        
    if message.content.startswith('!leave'):
        soundboard.clear()
        await voiceclient.disconnect()
        print("disconnected")

    if message.content.startswith('shh'):
        soundboard.clear()
        print("shh")


def done_playing():
    global voiceclient
    print("done playing")
    # if we want to do this, use the global event loop, these little event loops are super slow
    #voiceclient.loop.ensure_future(foo())
    #asyncio.ensure_future(foo())
    #await voiceclient.disconnect()
    #voiceclient.loop.create_task(foo())
    #voiceclient.loop.create_task(voiceclient.disconnect())

bot.run(sys.argv[1])