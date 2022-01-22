# DiscordBot
A secure and customizable bot for controlling cross-server announcements and interactions within Discord.
Within the code of the bot, you can give it anywhere from one to one million different triggers that send a message to a targeted group.

# Reccomendations
It is best to create a channel specifically for giving commands to the bot.

# How to Use
For every trigger you need a keyword, the command channel's ID, target channel, and the message you want sent.

# Triggers
The word you want to give the bot to tell it to send the message you want.
Every trigger should start with universal symbol (!, $, #, ETC.)
if message.content.startswith('_TRIGGER_')

# Command Channel
The channel you want to send the commands in.
message.channel.name == '_CHANNEL_NAME_'

# Target Channel
The channel receiving the message.
channel = client.get_channel(_CHANNELID_)

# Message
The message youre sending.
await channel.sent('_MESSAGE_')

