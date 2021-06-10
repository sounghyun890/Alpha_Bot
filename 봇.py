import discord
import asyncio
import os
import datetime

client = discord.Client()
access_token = os.environ["BOT_TOKEN"]

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("시작하는 중...")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("서버 관리")#상태 메세지
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        
@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith('알파야'):
        channel = message.channel
        await channel.send('ㅇ?')
        
        if(message.content == "!현재 시간"):
        await message.channel.send(embed=discord.Embed(title="현재 시간", timestamp=datetime.datetime.utcnow()))
        
client.run(access_token)
