import discord
import asyncio
import random
import openpyxl
from discord import Member
from discord.ext import commands
import youtube_dl
from urllib.request import urlopen, Request
import urllib
import urllib.request
import bs4
import os
import sys
import json
from selenium import webdriver
import time
import datetime

client = discord.Client()
access_token = os.environ["BOT_TOKEN"]
    
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
    
    #초성 욕설
    bad = message_content.find("ㅅㅂ")
    bad = bad + message_content.find("ㅂㅅ")
    bad = bad + message_content.find("ㅄ")
    bad = bad + message_content.find("ㅈㄴ")
    bad = bad + message_content.find("ㅈㄹ")
    bad = bad + message_content.find("ㅈㄹㄴ")
    bad = bad + message_content.find("ㅅ1ㅂ")
    bad = bad + message_content.find("ㅅ ㅂ")
    bad = bad + message_content.find("ㄷㅊ")
    bad = bad + message_content.find("ㅗ")
    bad = bad + message_content.find("ㄷ ㅊ")
    bad = bad + message_content.find("ㄲㅈ")
    bad = bad + message_content.find("ㅗ")
    
    if bad >= -12 :
        a = await message.channel.send(message.author.mention+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 초성 포함]")
        await message.delete() 
        await asyncio.sleep(7)
        await a.delete()


    #욕설
    bad1 = message_content.find("씨발")
    bad1 = bad1 + message_content.find("닥쳐")
    bad1 = bad1 + message_content.find("꺼져")
    bad1 = bad1 + message_content.find("지랄")
    bad1 = bad1 + message_content.find("시발")
    bad1 = bad1 + message_content.find("쌔끼")
    bad1 = bad1 + message_content.find("병신")
    bad1 = bad1 + message_content.find("샤발")
    bad1 = bad1 + message_content.find("씨 발")
    bad1 = bad1 + message_content.find("닥ㅊ")
    bad1 = bad1 + message_content.find("병 신")
    bad1 = bad1 + message_content.find("*발")
    bad1 = bad1 + message_content.find("*신")
    bad1 = bad1 + message_content.find("야발")
    bad1 = bad1 + message_content.find("새끼")
    bad1 = bad1 + message_content.find("빠큐")
    bad1 = bad1 + message_content.find("븅신")
    bad1 = bad1 + message_content.find("미친")
    bad1 = bad1 + message_content.find("시놈발")
    bad1 = bad1 + message_content.find("시이발")
    bad1 = bad1 + message_content.find("개세끼")
    bad1 = bad1 + message_content.find("게세끼")
    bad1 = bad1 + message_content.find("TLQKF")
    bad1 = bad1 + message_content.find("ㅈ랄")
    bad1 = bad1 + message_content.find("씌발")
    bad1 = bad1 + message_content.find("씹발")
    bad1 = bad1 + message_content.find("씌발")
    bad1 = bad1 + message_content.find("씹창")
    bad1 = bad1 + message_content.find("시이이벌")
    bad1 = bad1 + message_content.find("뒤져")
    bad1 = bad1 + message_content.find("존나")
    bad1 = bad1 + message_content.find("싯팔")
    bad1 = bad1 + message_content.find("ㅣ발")
    bad1 = bad1 + message_content.find("시발점")
    bad1 = bad1 + message_content.find("TLqkf")
    
    if bad1 >= -34 :
        a = await message.channel.send(message.author.mention+"님의 메세지가 삭제 되었습니다.\n[사유:욕설 포함]")
        await message.delete() 
        await asyncio.sleep(7)
        await a.delete()


    #폐드립
    bad2 = message_content.find("ㄴㄱㅁ")
    bad2 = bad2 + message_content.find("느금마")
    bad2 = bad2 + message_content.find("니 엄마")
    bad2 = bad2 + message_content.find("느그 어머니")
    bad2 = bad2 + message_content.find("싸발")
    bad2 = bad2 + message_content.find("폐륜")
    bad2 = bad2 + message_content.find("느그어미")
    
    if bad2 >= -6 :
        a = await message.channel.send(message.author.mention+"님의 메세지가 삭제 되었습니다.\n[사유:부모욕 포함]")
        await message.delete() 
        await asyncio.sleep(7)
        await a.delete()

    
    #섹드립
    bad3 = message_content.find("좇")
    bad3 = bad3 + message_content.find("좆")
    bad3 = bad3 + message_content.find("섹스")
    bad3 = bad3 + message_content.find("보지")
    bad3 = bad3 + message_content.find("섹 스")
    bad3 = bad3 + message_content.find("조까")
    bad3 = bad3 + message_content.find("porn")
    bad3 = bad3 + message_content.find("자지")
    bad3 = bad3 + message_content.find("불알")
    bad3 = bad3 + message_content.find("ㅈ같")
    bad3 = bad3 + message_content.find("기모찌")
    bad3 = bad3 + message_content.find("자위")
    bad3 = bad3 + message_content.find("딸딸이")
    bad3 = bad3 + message_content.find("SEX")
    bad3 = bad3 + message_content.find("Sex")
    bad3 = bad3 + message_content.find("섹슥")
    bad3 = bad3 + message_content.find("포르노")
    bad3 = bad3 - message_content.find("자위대")
    bad3 = bad3 - message_content.find("자지말")
    bad3 = bad3 - message_content.find("자지마")
    bad3 = bad3 - message_content.find("보지마")
    
    if bad3 >= -12 :
        a = await message.channel.send(message.author.mention+"님의 메세지가 삭제 되었습니다.\n[사유:성적발언 포함]")
        await message.delete() 
        await asyncio.sleep(7)
        await a.delete()
    
    #외국어 욕설
    bad4 = message_content.find("fuck")
    bad4 = bad4 + message_content.find("Tlqkf")
    bad4 = bad4 + message_content.find("tlqkf")
    bad4 = bad4 + message_content.find("쉣")
    bad4 = bad4 + message_content.find("퍽큐")
    bad4 = bad4 + message_content.find("FUCK")
    bad4 = bad4 + message_content.find("Fuck")
    bad4 = bad4 + message_content.find("sibar")
    bad4 = bad4 + message_content.find("Sibar")
    bad4 = bad4 + message_content.find("SIBAR")
    bad4 = bad4 + message_content.find("ファック")
    bad4 = bad4 + message_content.find("他妈的")
    
    if bad4 >= -11 :
        a = await message.channel.send(message.author.mention+"님의 메세지가 삭제 되었습니다.\n[사유:외국어욕 포함]")
        await message.delete() 
        await asyncio.sleep(7)
        await a.delete()


    #비하발언
    bad5 = message_content.find("따까리")
    bad5 = bad5 + message_content.find("찐따")
    bad5 = bad5 + message_content.find("미친놈")
    bad5 = bad5 + message_content.find("싸가지")
    
    if bad5 >= -3 :
        a = await message.channel.send(message.author.mention+"님의 메세지가 삭제 되었습니다.\n[사유:비하발언 포함]")
        await message.delete() 
        await asyncio.sleep(7)
        await a.delete()
    await bot.process_commands(messsage)

    #초성 욕설 bad 12개
    #욕설 bad1 34개
    #폐드립 bad2 6개
    #섹드립 bad3 20개
    #외국어 욕설 bad4 11개
    #비하발언 bad5 3개
@client.event  
async def on_message(message):
     if message.content.startswith('!주사위'):

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await message.channel.send("1")
        if randomNum == 2:
            await message.channel.send("2")
        if randomNum ==3:
            await message.channel.send("3")
        if randomNum ==4:
            await message.channel.send("4")
        if randomNum ==5:
            await message.channel.send("5")
        if randomNum ==6:
            await message.channel.send("6")
            
@client.event  
async def on_message(message):            
    if message.content.startswith("!날씨"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location+'날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()  # 온도
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지

        embed = discord.Embed(
            title=learn[1]+ ' 날씨 정보',
            description=learn[1]+ '날씨 정보입니다.',
            colour=discord.Colour.gold()
        )
        embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)  # 현재온도
        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)  # 체감온도
        embed.add_field(name='현재상태', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)  # 오늘날씨 # color=discord.Color.blue()
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)  # 구분선
        embed.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)  # 내일오전날씨
        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태
        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태



        await client.send_message(message.channel,embed=embed)
    
client.run(access_token)
