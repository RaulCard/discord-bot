import os

import discord

client = discord.Client()

@client.event
async def on_ready():
    """Notifies user when bot is ready
    """
    print(f"We have logged in as {client.user}!")

if __name__ == "__main__":
    bot_token = os.getenv('BOT_TOKEN')
    client.run(bot_token)
