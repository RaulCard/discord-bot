import os

import discord

client = discord.Client()

@client.event
async def on_ready():
    """Notifies user when bot is ready
    """
    print(f"We have logged in as {client.user}!")

@client.event
async def on_message(message):
    """Performs an action when a message is sent

    Parameters:
    message (str): message object
    """
    author = message.author
    content = message.content
    channel = message.channel
    if author != client.user:
        await message.channel.send(f"Author: {author}, Message: {content}")

@client.event
async def on_message_delete(message):
    """Performs an action when a message is deleted

    Parameters:
    message (str): message object
    """
    author = message.author
    content = message.content
    channel = message.channel
    await message.channel.send(f"Hey {author}, wtf did you just do?!")

if __name__ == "__main__":
    bot_token = os.getenv('BOT_TOKEN')
    client.run(bot_token)
