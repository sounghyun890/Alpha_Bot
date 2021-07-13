import asyncio
import time
import difflib
import discord,os


client = discord.Client()
token = "token"


@client.event
async def on_ready():
    print(f"[!] 다음으로 로그인에 성공했습니다.")
    print(f"[!] 다음 : {client.user.name}")
    print(f"[!] 다음 : {client.user.id}")
    guild_list = client.guilds
    for i in guild_list:
        print("서버 ID: {} / 서버 이름: {}".format(i.id, i.name))
    print(f"[!] 총 서버 수: {len(client.guilds)}")


@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        channel = message.channel
        await channel.send('hello라고 말해 주세요')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))
        
        
        
access_token = os.environ["token"]
client.run(access_token)
