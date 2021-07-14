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
    wr1 = message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 언어 포함]"
    if message.content.startswith('씨'):
        channel = message.channel

        def check(m):
            m = return m.content == '발' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await message.delete()
        await m.delete()
        a = await channel.send(wr1.format(msg))
        await asyncio.sleep(7)
        await a.delete()
        
        
        
access_token = os.environ["token"]
client.run(access_token)
