import os

import discord
from discord.ext import commands

client = commands.Bot(command_prefix= '.') #Set prefix to '.'

@client.event
async def on_ready():
    """Notifies user when bot is ready
    """
    print(f"We have logged in as {client.user}!")

@client.event
async def on_message(message):
    """Prints last sent message. If message is command, process instead
    """
    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    elif message.author == client.user:
        return
    else:
        print(f"Message!: {message.content}")


@client.command()
async def ping(ctx):
    """Sends 'PONG!' when called

    Parameters:
    ctx (Context obj): context in which the command is being invoked under
    """
    await ctx.send("PONG!")

@client.command()
async def echo(ctx, *messages):
    """ Echos specified message

    Parameters:
        *messages (str): output string
    """
    output = ""
    for word in messages:
        output += word + ' '
    await ctx.send(f"ECHOING: {output}")

if __name__ == "__main__":
    bot_token = os.getenv('BOT_TOKEN')
    client.run(bot_token)
