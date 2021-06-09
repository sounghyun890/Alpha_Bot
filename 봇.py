import discord
import os

client = discord.Client()
access_token = os.environ["BOT_TOKEN"]

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game=discord.Game(name='', type=1))

now = datetime.datetime.now()
time = f"{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분"

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith('알파야'):
        channel = message.channel
        await channel.send('ㅇ?')

    if message.content.startswith('현재 시간'):
        channel = message.channel
        await channel.send(time)
        
client.run(access_token)
