import discord
import os
import discord.ext
from discord.ext import commands

# use env to hide token
from dotenv import load_dotenv
from pathlib import Path
env_path = Path('path to env file')
load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv('DISCORD_TOKEN')
# -----

# runs the discord bot
client = discord.Client()

# predetermined messages
@client.event
async def on_message(message):

    if message.author == client.user:
        return
    # reading and writing messages:
    # message 1
    # what is it looking for and where?
    if message.content.startswith("TRIGGER") and message.channel.name == 'COMMAND-CHANNEL':
        # what will it say back?
        # channel where message will be send
        # channel ID from discord
        channel = client.get_channel(XXXXXXXXXXXX)
        await channel.send('MESSAGE')

    # message 2
    if message.content.startswith("TRIGGER_2") and message.channel.name == 'COMMAND-CHANNEL':
        channel = client.get_channel(XXXXXXXXXXXX)
        await channel.send('MESSAGE_2')


# confirm bot is running
@client.event
async def on_ready():
    print("RUNNING")

# run, get token
if __name__ == '__main__':
    client.run(TOKEN)
