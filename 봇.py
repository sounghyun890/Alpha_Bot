import asyncio
import discord,os
import datetime


client = discord.Client()
    
    
@client.event
async def on_ready():
    print("로그인 된 봇:") #화면에 봇의 아이디, 닉네임이 출력되는 코드
    print(client.user.name)
    print(client.user.id)
    print("===========")
    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("시작하는 중...")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("!도움 찾기")#상태 메세지
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        game = discord.Game("!도움 듣기")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)        
# 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
# 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
        
now = datetime.datetime.now()
time = f"{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분"

@client.event
async def on_message_delete(message):#메세지가 삭제 되면
    if message.author.bot:return
    
    if message.guild.id ==653083797763522580:return


    channel = client.get_channel(849536197273059338)
    embed = discord.Embed(title=f"삭제됨", description=f"유저 : {message.author.display_name} \n유저ID : {message.author} \n서버 : {message.guild.name} \n채널 : {message.channel.mention}", color=0xFF0000)
    embed.add_field(name="삭제된 내용", value=f"내용 : {message.content}", inline=False)
    embed.set_footer(text=f"TNS 봇 | {time}")
    await channel.send(embed=embed)


@client.event    
async def on_message_edit(before, after):#메세지 수정 되면(작동 안함)
    if message.author.bot:return
    channel = client.get_channel(849536197273059338)
    embed = discord.Embed(title=f"수정됨", description=f"유저 : {before.author.mention} 채널 : {before.channel.mention}", color=0xFF9900)
    embed.add_field(name="수정 전 내용", value=before.content, inline=True)
    embed.add_field(name="수정 후 내용", value=after.content, inline=True)
    embed.set_footer(text=f"{before.guild.name} | {time}")
    await channel.send(embed=embed)

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot:
        return None
   

    id = message.author.id
    channel = message.channel

    if message.content == "!도움":
        embed = discord.Embed(title = "TNS 봇의 도움말", description = '''
        욕 검열 봇입니다
TNS봇은 삭제 된 내용을 로그서버로 전송하고 있습니다
만약 개인정보 보호를 원하신다면 로그서버의 설명 게시판을 읽어주세요
욕 추가 및 수정을 원하시면 로그 서버의 문의 채팅방을 이용해주세요
봇 로그 보러가기 https://discord.gg/hFryJ4zYyw''', color = 0x08FFFA)
        await message.author.send(embed = embed)
        await message.delete()


    if message.author.bot:
    
        await message.author.send(embed = embed) # message.channel.send를 message.author.send로
    message_content = message.content
    
    bad = message_content.find("ㅅㅂ")#초성 욕설
    bad = bad + message_content.find("ㅂㅅ")#초성 욕설
    bad = bad + message_content.find("ㅄ")#초성 욕설
    bad = bad + message_content.find("ㅈㄴ")#초성 욕설
    bad = bad + message_content.find("ㅈㄹ")#초성 욕설
    bad = bad + message_content.find("ㅈㄹㄴ")#초성 욕설
    bad = bad + message_content.find("ㅅ1ㅂ")#35#초성 욕설
    bad = bad + message_content.find("ㅅ ㅂ")#47#초성 욕설
    bad = bad + message_content.find("ㄷㅊ")#초성 욕설
    bad = bad + message_content.find("ㅗ")#초성 욕설
    bad = bad + message_content.find("ㄷ ㅊ")#51#초성 욕설
    bad = bad + message_content.find("ㄲㅈ")#초성 욕설
    bad = bad + message_content.find("ㅗ")#초성 욕설
    bad = bad + message_content.find("씨발")#욕설
    bad = bad + message_content.find("닥쳐")#욕설
    bad = bad + message_content.find("꺼져")#욕설
    bad = bad + message_content.find("지랄")#욕설
    bad = bad + message_content.find("시발")#욕설
    bad = bad + message_content.find("쌔끼")#욕설
    bad = bad + message_content.find("병신")#욕설
    bad = bad + message_content.find("샤발")#욕설
    bad = bad + message_content.find("씨 발")#욕설
    bad = bad + message_content.find("닥ㅊ")#욕설
    bad = bad + message_content.find("병 신")#욕설
    bad = bad + message_content.find("*발")#욕설
    bad = bad + message_content.find("*신")#욕설
    bad = bad + message_content.find("야발")#욕설
    bad = bad + message_content.find("새끼")#욕설
    bad = bad + message_content.find("빠큐")#욕설
    bad = bad + message_content.find("븅신")#욕설
    bad = bad + message_content.find("미친")#욕설
    bad = bad + message_content.find("시놈발")#욕설
    bad = bad + message_content.find("시이발")#욕설
    bad = bad + message_content.find("개세끼")#욕설
    bad = bad + message_content.find("게세끼")#욕설
    bad = bad + message_content.find("TLQKF")#영어 욕설
    bad = bad + message_content.find("ㅈ랄")#욕설
    bad = bad + message_content.find("씌발")#폐드립
    bad = bad + message_content.find("씹발")#욕설
    bad = bad + message_content.find("씌발")#욕설
    bad = bad + message_content.find("씹창")#욕설
    bad = bad + message_content.find("시이이벌")#욕설
    bad = bad + message_content.find("뒤져")#욕설
    bad = bad + message_content.find("존나")#욕설
    bad = bad + message_content.find("싯팔")#80#욕설
    bad = bad + message_content.find("ㅣ발")#욕설
    bad = bad - message_content.find("시발점")#-
    bad = bad - message_content.find("ㅗㅜㅑ")#-
    
    bad = bad + message_content.find("ㄴㄱㅁ")#초성 폐드립
    bad = bad + message_content.find("느금마")#폐드립
    bad = bad + message_content.find("니 엄마")#폐드립
    bad = bad + message_content.find("느그 어머니")#폐드립
    bad = bad + message_content.find("싸발")#폐드립
    bad = bad + message_content.find("폐륜")
    bad = bad + message_content.find("느그어미")#폐드립
    
    bad = bad + message_content.find("좇")#섹드립
    bad = bad + message_content.find("좆")#섹드립
    bad = bad + message_content.find("섹스")#섹드립
    bad = bad + message_content.find("보지")#섹드립
    bad = bad + message_content.find("섹 스")#섹드립
    bad = bad + message_content.find("조까")#섹드립
    bad = bad + message_content.find("porn")#섹드립
    bad = bad + message_content.find("자지")#섹드립
    bad = bad + message_content.find("불알")#섹드립
    bad = bad + message_content.find("ㅈ같")#섹드립
    bad = bad + message_content.find("기모찌")#섹드립
    bad = bad + message_content.find("자위")#섹드립
    bad = bad + message_content.find("딸딸이")#섹드립
    bad = bad + message_content.find("SEX")#섹드립
    bad = bad + message_content.find("Sex")#섹드립
    bad = bad + message_content.find("섹슥")#섹드립
    bad = bad + message_content.find("포르노")#섹드립
    bad = bad - message_content.find("자위대")#64#-
    bad = bad - message_content.find("자지말")#68#-
    bad = bad - message_content.find("자지마")#50#-
    bad = bad - message_content.find("보지마")#-
    
    bad = bad + message_content.find("fuck")#외국어 욕설
    bad = bad + message_content.find("Tlqkf")#영어 욕설
    bad = bad + message_content.find("tlqkf")#영어 욕설
    bad = bad + message_content.find("쉣")#영어 욕설
    bad = bad + message_content.find("퍽큐")#영어 욕설
    bad = bad + message_content.find("FUCK")#영어 욕설
    bad = bad + message_content.find("Fuck")#영어 욕설
    bad = bad + message_content.find("sibar")#영어 욕설
    bad = bad + message_content.find("Sibar")#영어 욕설
    bad = bad + message_content.find("SIBAR")#영어 욕설
    bad = bad + message_content.find("ファック")#외국어 욕
    bad = bad + message_content.find("他妈的")#외국어 욕
    
    bad = bad + message_content.find("따까리")#비하 발언
    bad = bad + message_content.find("찐따")#비하
    bad = bad + message_content.find("미친놈")#비하
    bad = bad + message_content.find("싸가지")#비하
    

    
    
    if bad >= -78 :
        a = await message.channel.send(message.author.mention+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 언어 포함]")
        await message.delete() 
        await asyncio.sleep(7)
        await a.delete()
    await bot.process_commands(messsage)
'''
@bot.command()
async def button(ctx):
    embeds = [discord.Embed(title="1 page"), discord.Embed(title="2 page"), discord.Embed(title="3 page"), discord.Embed(title="4 page"), discord.Embed(title="5 page")]
    e = Paginator(bot=bot,
                  ctx=ctx,
                  embeds=embeds,
                  only=ctx.author)
    await e.start()
'''

access_token = os.environ["token"]
client.run(access_token)
