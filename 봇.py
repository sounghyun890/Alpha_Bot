import discord
import asyncio
import os
import datetime

client = discord.Client()
access_token = os.environ["BOT_TOKEN"]
bot = Bot("your prefix")

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

    message_content = message.content

    a = message_content.find("알파야")
    a = a - message_content.find("알파야 자폭해")
    a = a - message_content.find("알파야 뭐해")
    a = a - message_content.find("알파야 시간")
    a = a - message_content.find("알파야 고양이")
    a = a - message_content.find("알파야 강아지")
    
    if message.content.startswith('알파야 자폭해'):
        channel = message.channel
        await channel.send('10초 후에 자폭합니다')
        await asyncio.sleep(3)
        await channel.send('자폭 할 수 있는 권한이 없어요')

    if message.content.startswith('알파야 뭐해'):
        channel = message.channel
        await channel.send('당신 메세지를 읽고 있습니다')

    if message.content.startswith('알파야 시간'):
        channel = message.channel
        await channel.send(embed=discord.Embed(title="현재 시간", timestamp=datetime.datetime.utcnow()))
        
    if message.content.startswith('알파야 고양이'):
        channel = message.channel
        await channel.send('야옹~')
        
    if message.content.startswith('알파야 강아지'):
        channel = message.channel
        await channel.send('멍멍!')

    if a>=5 :
        channel = message.channel
        await channel.send('네?')
        
client.run(access_token)
