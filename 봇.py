
import asyncio
import time
import difflib
import discord,os
import datetime
from discord.ext import tasks
from itertools import cycle
from discord.utils import get
import re



client = discord.Client()
guild_list = client.guilds
status = cycle(["!도움",f"테스트개의 서버에 참여 중","수정중 오류 주의","로그 확인은 로그서버로 문의"])



@client.event
async def on_ready():
    print(f"[!] 다음으로 로그인에 성공했습니다.")
    print(f"[!] 다음 : {client.user.name}")
    print(f"[!] 다음 : {client.user.id}")
    for i in guild_list:
        print("서버 ID: {} / 서버 이름: {}".format(i.id, i.name))
    print(f"[!] 총 서버 수: {len(client.guilds)}")
    
    

    change_status.start()    # 봇이 on_ready 상태라면, change_message 함수 실행

@tasks.loop(seconds=5)    # n초마다 다음 메시지 출력
async def change_status():
    sever = {len(client.guilds)}
    await client.change_presence(activity=discord.Game(next(status)))
    

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot:return

    text = message.content
    newtext1 = ''.join(char for char in text if char.isalnum())
    newtext2 = re.sub(r'[0-9]+', '', newtext1)

    await message.channel.send(newtext2)
    if newtext2..content.find("씨발") :
        message.delete()

   
    





access_token = os.environ["token"]
client.run(access_token)
