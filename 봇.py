import asyncio
import time
import difflib
import discord,os


client = discord.Client()
token = "token"


@client.event
async def on_ready():
    print("--- ready ---")


@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        channel = message.channel
        await channel.send('hello라고 말해 주세요')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))
        
        
        
client.run(token)
