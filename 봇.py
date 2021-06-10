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
async def on_message_delete(message):#메세지가 삭제 되면
    if message.author.bot:return
    channel = client.get_channel(849536197273059338)
    embed = discord.Embed(title=f"삭제됨", description=f"유저 : {message.author.display_name} \n유저ID : {message.author} \n서버 : {message.guild.name} \n채널 : {message.channel.mention}", color=0xFF0000)
    embed.add_field(name="삭제된 내용", value=f"내용 : {message.content}", inline=False)
    embed.set_footer(text=f"알파봇 | {time}")
    await channel.send(embed=embed)
        
@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith('알파야 자폭해'):
    elif message.content.startswith('알파야 자폭해'):
        channel = message.channel
        await channel.send('10초 후에 자폭합니다')
        await asyncio.sleep(3)
        await channel.send('자폭 할 수 있는 권한이 없어요')

    if message.content.startswith('알파야 뭐해'):
    elif message.content.startswith('알파야 뭐해'):
        channel = message.channel
        await channel.send('당신 메세지를 읽고 있습니다')

    if message.content.startswith('알파야 시간'):
    elif message.content.startswith('알파야 시간'):
        channel = message.channel
        await channel.send(embed=discord.Embed(title="현재 시간", timestamp=datetime.datetime.utcnow()))

    if message.content.startswith('알파야'):
    elif message.content.startswith('알파야'):
        channel = message.channel
        await channel.send('네?')

client.run(access_token)
