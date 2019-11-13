#!/usr/bin/env

import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Welcome to the CTS server, say hi to everyone :)'
    )
    print(f'Sent a message to {member.name}')

F = open("Credentials.txt","r")
DISCORD_TOKEN = str(F.read().rstrip('\n'))
F.close()

client.run(str(DISCORD_TOKEN))
