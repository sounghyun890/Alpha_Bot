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
    if message.content.startswith('알파야 자폭해'):
        channel = message.channel
        await channel.send('10초 후에 자폭합니다')
        await asyncio.sleep(3)
        await channel.send('자폭 할 수 있는 권한이 없어요')
        
    if message.content.startswith('알파야 안녕'):
        channel = message.channel
        await channel.send('안녕하세요!')
        
    if message.content.startswith('알파야 뭐해'):
        channel = message.channel
        await channel.send('당신 메세지를 읽고 있습니다')
        
    if message.content.startswith('!현재 시간'):
        channel = message.channel
        await channel.send(embed=discord.Embed(title="현재 시간", timestamp=datetime.datetime.utcnow()))
        
    if message.content.startswith('알파야'):
        channel = message.channel
        await channel.send('ㅇ?')
        
client.run(access_token)
