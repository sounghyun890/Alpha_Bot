import asyncio
import time
import difflib
import discord,os


client = discord.Client()
token = "token"
riot_token = "rtoken"

@client.event
async def on_ready():
    print("--- ready ---")


@client.event
async def on_message(message):
    if message.content.startswith('씨'):
        channel = message.channel
        

        def check(m):
            return m.content == '발' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))
        
        
        
client.run(token)
