import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None

    if message.content.startswith('!안녕'):
        channel = message.channel
        await channel.send('반가워!')
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
