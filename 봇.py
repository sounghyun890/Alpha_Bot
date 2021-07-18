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
        helps = [discord.Embed(title='목차', description='1.기능\n2.명령어\n3.봇정보\n4.개발자', color=0x00ffff),
                 discord.Embed(title='기능', description='TNS봇은 욕설감지봇으로 욕설 감지시 자동으로 삭제합니다\n로그확인,욕 수정및 추가,그외 문의는 TNS서버를 이용해주세요', color=0x00fffff),
                 discord.Embed(title='명령어', description='!청소 [갯수]\n갯수만큼 메세지 삭제\n그외 업데이트 예정 ', color=0x00fffff),
                 discord.Embed(title='봇정보', description=f'봇생성일:2021.6.16\n이용서버 수: {len(client.guilds)}\n봇 서버\nhttps://discord.gg/hFryJ4zYyw\n하트는 개발자에게 큰 도움이 됩니다\nhttps://koreanbots.dev/bots/848795383751639080', color=0x00fffff),
                 discord.Embed(title='개발자', description='Tanat#5542\n고양이를 좋아하며 봇의 주인이다\nPines#6810\n개발팀원이며 잠수일때가 많다', color=0x00fffff),]
        help_msg = await message.channel.send(embed=helps[n])
        for i in ['⏪', '◀️', '⏹', '▶️', '⏩']:
            await help_msg.add_reaction(i)
        def check(reaction, user):
            return user == message.author
        while True:
            try:
                reaction, user = await client.wait_for('reaction_add', check=check, timeout=180)
            except asyncio.TimeoutError:
                break
            if reaction.emoji == '⏪':
                n = 0
                await help_msg.edit(embed=helps[n])
            elif reaction.emoji == '⏩':
                n = len(helps)-1
                await help_msg.edit(embed=helps[n])
            elif reaction.emoji == '◀️':
                if n != 0:
                    n -= 1
                    await help_msg.edit(embed=helps[n])
            elif reaction.emoji == '▶️':
                if n != len(helps)-1:
                    n += 1
                    await help_msg.edit(embed=helps[n])
            elif reaction.emoji == '⏹':
                await help_msg.delete()
                break
        
        
        
access_token = os.environ["token"]
client.run(access_token)
