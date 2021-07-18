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
    if message.content == '!도움말' or message.content == '!도움' or message.content == '/help':
        n = 0
        helps = [discord.Embed(title='목차', description='페이지 2\n 관리기능\n페이지 3\n편의기능\n페이지 4\n재미기능\n페이지 5\n봇정보', color=0x00ffff),
                 discord.Embed(title='관리기능', description='!kick [사용자 맨션]\n특정사용자를 서버에서 킥시켜요\n!ban [사용자 맨션]\n특정사용자를 서버에서 밴시켜요\n!뮤트 (맨션)\n사용자를 뮤트 시켜요\n!언뮤트 \n사용자의 뮤트를 풀어요\n통방입장중 \n통방입장중라는 역할을 추가하시고 음성채널에 들어가시면 역할이 들어가져있습니다.', color=0x00fffff),
                 discord.Embed(title='편의기능', description='!타이머 [시간(초기준)]\n몇초의 타이머를 설정하고 끝나면 맨션해 드려요\n !주사위 (숫자)\n도박입니다\n !서버정보\n현재 서버의 정보를 알려줘요\n!내정보\n디엠으로 내 정보를 알려줘요\n !파이\n파이입니다\n !원주율\n원주율입니다\n !핑 \n현재 핑을 측정해서 알려줘요', color=0x00fffff),
                 discord.Embed(title='재미기능', description='가위또는 바위 또는 보)\n가위바위보 게임을 해요', color=0x00fffff),
                 discord.Embed(title='봇정보', description='!개발자\n저를 만들어주신분을 알려드려요!\n!건의 (메시지)\n건의를 하고 싶으면 이렇게 쳐주세요!\n!오픈소스**\n제가 쓴 오픈소스를 알려드려요', color=0x00fffff),]
        help_msg = await message.channel.send(embed=helps[n])
        for i in [':rewind:', ':arrow_backward:', ':stop_button:', ':arrow_forward:', ':fast_forward:']:
            await help_msg.add_reaction(i)
        def check(reaction, user):
    return user == message.author and reaction.message.channel == message.channel
        while True:
            try:
                reaction, user = await client.wait_for('reaction_add', check=check, timeout=120)
            except asyncio.TimeoutError:
                break
            if reaction.emoji == ':rewind:':
                n = 0
                await help_msg.edit(embed=helps[n])
            elif reaction.emoji == ':fast_forward:':
                n = len(helps)-1
                await help_msg.edit(embed=helps[n])
            elif reaction.emoji == ':arrow_backward:':
                if n != 0:
                    n -= 1
                    await help_msg.edit(embed=helps[n])
            elif reaction.emoji == ':arrow_forward:':
                if n != len(helps)-1:
                    n += 1
                    await help_msg.edit(embed=helps[n])
            elif reaction.emoji == ':stop_button:':
                await help_msg.delete()
                break
        
        
        
access_token = os.environ["token"]
client.run(access_token)
