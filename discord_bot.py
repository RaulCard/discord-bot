import os

import discord
import youtube_dl
from discord.ext import commands

import examples.basic_voice

client = commands.Bot(command_prefix= '!')

@client.event
async def on_ready():
    """Notifies user when bot is ready
    """
    print(f"We have logged in as {client.user}")

@client.command()
async def ping(ctx):
    """Sends 'PONG!' when called

    Parameters:
    ctx (Context obj): context in which the command is being invoked under
    """
    await ctx.send("PONG!")

@client.command()
async def stop(ctx):
    await client.logout()

@client.command()
async def download_sound(ctx, url):
    ydl_options = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }]
    }
    with youtube_dl.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])

@client.command()
async def yell(ctx):
    url = "https://youtu.be/xn6hhrX34Pw"
    channel = ctx.message.author.voice.channel
    voice_client = await channel.connect()
    voice_client.play(discord.FFmpegPCMAudio("scream.mp3"))
    voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
    voice_client.source.volume = 0.75

    while True:
        if voice_client.is_playing():
            pass
        else:
            await voice_client.disconnect()
            break;

@client.command()
async def con(ctx):
    channel = ctx.message.author.voice.channel
    voice_client = await channel.connect()

@client.command()
async def dis(ctx):
    voice_client = client.voice_clients
    if len(client.voice_clients) != 0:
        await voice_client[0].disconnect()

if __name__ == "__main__":
    bot_token = os.getenv('BOT_TOKEN')
    client.run(bot_token)
