import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith('안녕'):
        channel = message.channel
        await channel.send('반가워!')
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
