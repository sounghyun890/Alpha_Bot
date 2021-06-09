import discord
import os
import datetime

client = discord.Client()
access_token = os.environ["BOT_TOKEN"]

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game=discord.Game(name='', type=1))
    
    @client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("서버관리")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith('알파야'):
        channel = message.channel
        await channel.send('ㅇ?')

    if message.content.startswith('!현재 시간'):
        now = datetime.datetime.now()
        시간 = str(now.hour+9)
        if 시간 >= 24 :
             시간 = 시간 - 24
        time = f"{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {시간}시 {str(now.minute)}분"
        channel = message.channel
        await channel.send(time)
        
client.run(access_token)
