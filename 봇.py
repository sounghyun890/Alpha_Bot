import asyncio
import time
import difflib
import discord,os
import datetime
from discord.ext import tasks
from itertools import cycle
from discord.utils import get
import json
import requests

riot_token = "RGAPI-2aea1cfd-fa8f-4e00-b86b-b8668ad9d749"

client = discord.Client()

status = cycle(["!도움",f"59개의 서버에 참여 중","수정중 오류 주의","로그 확인은 로그서버로 문의"])


@client.event
async def on_ready():
    print(f"[!] 다음으로 로그인에 성공했습니다.")
    print(f"[!] 다음 : {client.user.name}")
    print(f"[!] 다음 : {client.user.id}")
    guild_list = client.guilds
    for i in guild_list:
        print("서버 ID: {} / 서버 이름: {}".format(i.id, i.name))
    print(f"[!] 총 서버 수: {len(client.guilds)}")

    change_status.start()    # 봇이 on_ready 상태라면, change_message 함수 실행

@tasks.loop(seconds=5)    # n초마다 다음 메시지 출력
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
    

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
   

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
  
    if message.channel.id == 850316721989877780:return
    if message.channel.id == 851016540714172426:return
    if message.guild.id == 849536031283478599 :
        if message.channel.id != 858552903659683851 : return
    if message.guild.id == 653083797763522580:return
    message_content = message.content
    
    #특수
    if message.content.startswith("/검색 "):
        UserName = message.content.replace("/검색 ", "")
        UserInfoUrl = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + UserName
        res = requests.get(UserInfoUrl, headers={"X-Riot-Token":riot_token})
        resjs = json.loads(res.text)

        if res.status_code == 200:
            UserIconUrl = "http://ddragon.leagueoflegends.com/cdn/11.3.1/img/profileicon/{}.png"
            embed = discord.Embed(title=f"{resjs['name']} 님의 플레이어 정보", description=f"**{resjs['summonerLevel']} LEVEL**", color=0xFF9900)

            UserInfoUrl_2 = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + resjs["id"]
            res_2 = requests.get(UserInfoUrl_2, headers={"X-Riot-Token":riot_token})
            res_2js = json.loads(res_2.text)

            if res_2js == []: # 언랭크일때
                embed.add_field(name=f"{resjs['name']} 님은 언랭크입니다.", value="**언랭크 유저의 정보는 출력하지 않습니다.**", inline=False)

            else: # 언랭크가 아닐때
                for rank in res_2js:
                    if rank["queueType"] == "RANKED_SOLO_5x5":
                        embed.add_field(name="솔로랭크", value=f"**티어 : {rank['tier']} {rank['rank']} - {rank['leaguePoints']} LP**\n"
                                                           f"**승 / 패 : {rank['wins']} 승 {rank['losses']} 패**", inline=True)

                    else:
                        embed.add_field(name="자유랭크", value=f"**티어 : {rank['tier']} {rank['rank']} - {rank['leaguePoints']} LP**\n"
                                                            f"**승 / 패 : {rank['wins']} 승 {rank['losses']} 패**", inline=True)

            embed.set_author(name=resjs['name'], url=f"http://fow.kr/find/{UserName.replace(' ', '')}", icon_url=UserIconUrl.format(resjs['profileIconId']))
            await message.channel.send(embed=embed)



    #초성
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
    bad = bad + message_content.find("ㅅ2ㅂ")
    bad = bad + message_content.find("ㅅ3ㅂ")
    bad = bad + message_content.find("ㅅ4ㅂ")
    bad = bad + message_content.find("ㅅ5ㅂ")
    bad = bad + message_content.find("ㅅ6ㅂ")
    bad = bad + message_content.find("ㅅ7ㅂ")
    bad = bad + message_content.find("ㅅ8ㅂ")
    bad = bad + message_content.find("ㅅ9ㅂ")
    bad = bad + message_content.find("ㅅ#ㅂ")
    bad = bad + message_content.find("ㅅ$ㅂ")
    bad = bad + message_content.find("ㅅ%ㅂ")
    bad = bad + message_content.find("ㅅ^ㅂ")
    bad = bad + message_content.find("ㅅ&ㅂ")
    bad = bad + message_content.find("ㅅ*ㅂ")
    bad = bad + message_content.find("ㅅ~ㅂ")
    bad = bad + message_content.find("ㅅ1ㅂ")#28
    bad = bad + message_content.find("ㅅ{ㅂ")
    bad = bad + message_content.find("ㅅ}ㅂ")
    bad = bad + message_content.find("ㅅ[ㅂ")
    bad = bad + message_content.find("ㅅ]ㅂ")
    bad = bad + message_content.find("ㅅ;ㅂ")
    bad = bad + message_content.find("ㅅ'ㅂ")
    bad = bad + message_content.find("ㅅ:ㅂ")
    bad = bad + message_content.find("ㅅ\ㅂ")
    bad = bad + message_content.find("ㅅ|ㅂ")
    bad = bad + message_content.find("ㅅ`ㅂ")
    bad = bad + message_content.find("ㅅ  ㅂ")
    bad = bad + message_content.find("씨ㅂ")
    bad = bad + message_content.find("씨바")
    bad = bad + message_content.find("ㅅㅣㅂ")
    bad = bad + message_content.find("ㅅㅣㅂㅏㄹ")
    bad = bad + message_content.find("ㅆㅣㅂㅏㄹ")#28
    bad = bad + message_content.find("ㅅ  ㅂ")
    bad = bad + message_content.find("ㅅ   ㅂ")
    bad = bad + message_content.find("ㅅ    ㅂ")
    bad = bad + message_content.find("ㅅ     ㅂ")
    bad = bad + message_content.find("ㅅ      ㅂ")
    bad = bad + message_content.find("ㅅ       ㅂ")
    bad = bad + message_content.find("ㅅ        ㅂ")
    bad = bad + message_content.find("ㅅ         ㅂ")
    bad = bad + message_content.find("ㅅ          ㅂ")
    bad = bad + message_content.find("ㅅ           ㅂ")
    bad = bad + message_content.find("ㅅ            ㅂ")
    bad = bad + message_content.find("ㅅ             ㅂ")
    bad = bad + message_content.find("ㅅ              ㅂ")#57
    bad = bad + message_content.find("ㅆㅂ")
    bad = bad + message_content.find("ㅅ.ㅂ")
    bad = bad + message_content.find("⨉")
    bad = bad + message_content.find("ㅈㄴ")
    bad = bad + message_content.find("ㅈଅㄴ")
    bad = bad + message_content.find("ㄷ.ㅊ")
    bad = bad + message_content.find("ㅈ⨋ㄴ")
    bad = bad - message_content.find("ㅗㅜ")
    bad = bad + message_content.find("ᐲᗨ")


    if bad >= -63 :
        await message.delete() 
        a = await message.channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 초성 포함]")
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
    bad1 = bad1 + message_content.find("씨2발")#34
    bad1 = bad1 + message_content.find("씨3발")
    bad1 = bad1 + message_content.find("씨4발")
    bad1 = bad1 + message_content.find("씨5발")
    bad1 = bad1 + message_content.find("씨6발")
    bad1 = bad1 + message_content.find("씨7발")
    bad1 = bad1 + message_content.find("씨8발")
    bad1 = bad1 + message_content.find("씨9발")
    bad1 = bad1 + message_content.find("씨#발")
    bad1 = bad1 + message_content.find("씨$발")
    bad1 = bad1 + message_content.find("씨%발")
    bad1 = bad1 + message_content.find("씨^발")
    bad1 = bad1 + message_content.find("씨&발")
    bad1 = bad1 + message_content.find("씨*발")
    bad1 = bad1 + message_content.find("씨~발")#48
    bad1 = bad1 + message_content.find("시2발")
    bad1 = bad1 + message_content.find("시3발")
    bad1 = bad1 + message_content.find("시4발")
    bad1 = bad1 + message_content.find("시5발")
    bad1 = bad1 + message_content.find("시6발")
    bad1 = bad1 + message_content.find("시7발")
    bad1 = bad1 + message_content.find("시8발")
    bad1 = bad1 + message_content.find("시9발")
    bad1 = bad1 + message_content.find("시#발")
    bad1 = bad1 + message_content.find("시$발")
    bad1 = bad1 + message_content.find("시%발")
    bad1 = bad1 + message_content.find("시^발")
    bad1 = bad1 + message_content.find("시&발")
    bad1 = bad1 + message_content.find("시*발")
    bad1 = bad1 + message_content.find("시~발")
    bad1 = bad1 + message_content.find("시1발")#64
    bad1 = bad1 + message_content.find("시!발")
    bad1 = bad1 + message_content.find("껒")
    bad1 = bad1 + message_content.find("꺼ㅈ")
    bad1 = bad1 + message_content.find("비융신")
    bad1 = bad1 + message_content.find("씨  발")
    bad1 = bad1 + message_content.find("시   발")
    bad1 = bad1 + message_content.find("시    발")
    bad1 = bad1 + message_content.find("시     발")
    bad1 = bad1 + message_content.find("시      발")
    bad1 = bad1 + message_content.find("시       발")
    bad1 = bad1 + message_content.find("시        발")
    bad1 = bad1 + message_content.find("시         발")
    bad1 = bad1 + message_content.find("시          발")
    bad1 = bad1 + message_content.find("시           발")
    bad1 = bad1 + message_content.find("시            발")
    bad1 = bad1 + message_content.find("시             발")
    bad1 = bad1 + message_content.find("시              발")#80
    bad1 = bad1 + message_content.find("ㅑ발")
    bad1 = bad1 + message_content.find("^ㅣ발")
    bad1 = bad1 + message_content.find("^^발")
    bad1 = bad1 + message_content.find("^^ㅂ")
    bad1 = bad1 + message_content.find("시  발")
    bad1 = bad1 + message_content.find("씨   발")
    bad1 = bad1 + message_content.find("씨    발")
    bad1 = bad1 + message_content.find("씨     발")
    bad1 = bad1 + message_content.find("씨      발")
    bad1 = bad1 + message_content.find("씨       발")
    bad1 = bad1 + message_content.find("씨        발")
    bad1 = bad1 + message_content.find("씨         발")
    bad1 = bad1 + message_content.find("씨          발")
    bad1 = bad1 + message_content.find("씨           발")
    bad1 = bad1 + message_content.find("씨            발")
    bad1 = bad1 + message_content.find("씨             발")
    bad1 = bad1 + message_content.find("씨              발")#80
    bad1 = bad1 + message_content.find("미칰")
    bad1 = bad1 + message_content.find("씨빨")
    bad1 = bad1 + message_content.find("시@@발")
    bad1 = bad1 + message_content.find("시.발")
    bad1 = bad1 + message_content.find("씨.발")#103
    bad1 = bad1 + message_content.find("10새")
    bad1 = bad1 + message_content.find("10세")
    bad1 = bad1 + message_content.find("10쉑")
    bad1 = bad1 + message_content.find("10쉐")
    bad1 = bad1 + message_content.find("10쌔")
    bad1 = bad1 + message_content.find("10쎄")
    bad1 = bad1 + message_content.find("10알")
    bad1 = bad1 + message_content.find("10창")
    bad1 = bad1 + message_content.find("18것")
    bad1 = bad1 + message_content.find("18노")
    bad1 = bad1 + message_content.find("18놈")
    bad1 = bad1 + message_content.find("18뇬")
    bad1 = bad1 + message_content.find("18롬")
    bad1 = bad1 + message_content.find("18새")
    bad1 = bad1 + message_content.find("18색기")
    bad1 = bad1 + message_content.find("18세끼")
    bad1 = bad1 + message_content.find("18세리")
    bad1 = bad1 + message_content.find("凸")#121
    bad1 = bad1 + message_content.find("18섹")
    bad1 = bad1 + message_content.find("18스")
    bad1 = bad1 + message_content.find("18아")
    bad1 = bad1 + message_content.find("ㄱㅐ쌔끼")
    bad1 = bad1 + message_content.find("ㄱㅆㄲ")
    bad1 = bad1 + message_content.find("ㅅㅂㄹㅇ")
    bad1 = bad1 + message_content.find("ㅆㅍ")
    bad1 = bad1 + message_content.find("ㅆ앙")
    bad1 = bad1 + message_content.find("개색키")
    bad1 = bad1 + message_content.find("색끼")
    bad1 = bad1 + message_content.find("개색히")
    bad1 = bad1 + message_content.find("십새기")
    bad1 = bad1 + message_content.find("뒈져")
    bad1 = bad1 + message_content.find("새꺄")
    bad1 = bad1 + message_content.find("세꺄")
    bad1 = bad1 + message_content.find("시벌")
    bad1 = bad1 + message_content.find("십스키")
    bad1 = bad1 + message_content.find("썅")
    bad1 = bad1 + message_content.find("씨바랄")
    bad1 = bad1 + message_content.find("씨랼")
    bad1 = bad1 + message_content.find("씹쉐")
    bad1 = bad1 + message_content.find("씨부럴")
    bad1 = bad1 + message_content.find("씨부랄")
    bad1 = bad1 + message_content.find("씨파")
    bad1 = bad1 + message_content.find("씹년")
    bad1 = bad1 + message_content.find("띠ㅋ발")
    bad1 = bad1 + message_content.find("띸발")
    bad1 = bad1 + message_content.find("찌랄")
    bad1 = bad1 + message_content.find("엠병")
    bad1 = bad1 + message_content.find("엿같")#151
    bad1 = bad1 + message_content.find("쑤발")
    bad1 = bad1 + message_content.find("병sin")
    bad1 = bad1 + message_content.find("c2bal")
    bad1 = bad1 + message_content.find("ㅁㅣ친")
    bad1 = bad1 + message_content.find("ㅁl친")
    bad1 = bad1 + message_content.find("z랄")
    bad1 = bad1 + message_content.find("Z랄")
    bad1 = bad1 + message_content.find("병 신")
    bad1 = bad1 + message_content.find("병  신")
    bad1 = bad1 + message_content.find("병   신")
    bad1 = bad1 + message_content.find("병    신")
    bad1 = bad1 + message_content.find("병     신")
    bad1 = bad1 + message_content.find("병      신")
    bad1 = bad1 + message_content.find("병       신")
    bad1 = bad1 + message_content.find("병        신")
    bad1 = bad1 + message_content.find("병         싱")
    bad1 = bad1 + message_content.find("병          신")
    bad1 = bad1 + message_content.find("병           신")
    bad1 = bad1 + message_content.find("병            신")
    bad1 = bad1 + message_content.find("병             신")
    bad1 = bad1 + message_content.find("병              신")
    bad1 = bad1 + message_content.find("씨;발")
    bad1 = bad1 + message_content.find("씨.발")
    bad1 = bad1 + message_content.find("쌔 끼")
    bad1 = bad1 + message_content.find("병.신")
    bad1 = bad1 + message_content.find("시:발")
    bad1 = bad1 + message_content.find("붱신")
    bad1 = bad1 + message_content.find("이색이")
    bad1 = bad1 + message_content.find("시?발")
    bad1 = bad1 + message_content.find("시이바")
    bad1 = bad1 + message_content.find("시?발")
    bad1 = bad1 + message_content.find("씨 ଏ발")
    bad1 = bad1 + message_content.find("븅쉰")
    bad1 = bad1 + message_content.find("씨이발")
    bad1 = bad1 + message_content.find("씨이팔")
    bad1 = bad1 + message_content.find("c2bal")
    bad1 = bad1 + message_content.find("sibar")
    bad1 = bad1 + message_content.find("Sibar")
    bad1 = bad1 + message_content.find("SIBAR")
    bad1 = bad1 + message_content.find("미치겠")
    bad1 = bad1 + message_content.find("시bal")
    bad1 = bad1 + message_content.find("닭쳐")
    bad1 = bad1 + message_content.find("ㅅ발")
    bad1 = bad1 + message_content.find("Tlqkf")
    bad1 = bad1 + message_content.find("tlqkf")
    bad1 = bad1 + message_content.find("등sin")
    bad1 = bad1 + message_content.find("등신")
    bad1 = bad1 - message_content.find("1등신")
    bad1 = bad1 - message_content.find("2등신")
    bad1 = bad1 - message_content.find("3등신")
    bad1 = bad1 - message_content.find("4등신")
    bad1 = bad1 - message_content.find("5등신")
    bad1 = bad1 - message_content.find("6등신")
    bad1 = bad1 - message_content.find("7등신")
    bad1 = bad1 - message_content.find("8등신")
    bad1 = bad1 - message_content.find("9등신")
    bad1 = bad1 - message_content.find("10등신")
    bad1 = bad1 + message_content.find("닥@쳐")
    bad1 = bad1 + message_content.find("개새기")
    bad1 = bad1 + message_content.find("싸발")
    bad1 = bad1 + message_content.find("ㅆ발")
    bad1 = bad1 + message_content.find("んй刀│")
    bad1 = bad1 + message_content.find("𓂻𓃱𓅿𓅿𓂭 ")
    bad1 = bad1 + message_content.find("ኀዞላዞ")
    bad1 = bad1 + message_content.find("슈발")
    bad1 = bad1 + message_content.find("지럴")
    bad1 = bad1 + message_content.find("븅딱")
    bad1 = bad1 + message_content.find("야발")
    bad1 = bad1 + message_content.find("씨불")
    bad1 = bad1 + message_content.find("개시키")#201
    bad1 = bad1 + message_content.find("존  나")
    bad1 = bad1 + message_content.find("존   나")
    bad1 = bad1 + message_content.find("존    나")
    bad1 = bad1 + message_content.find("존     나")
    bad1 = bad1 + message_content.find("존      나")
    bad1 = bad1 + message_content.find("존       나")
    bad1 = bad1 + message_content.find("존        나")
    bad1 = bad1 + message_content.find("존         나")
    bad1 = bad1 + message_content.find("존          나")
    bad1 = bad1 + message_content.find("존           나")
    bad1 = bad1 + message_content.find("존            나")
    bad1 = bad1 + message_content.find("존             나")
    bad1 = bad1 + message_content.find("존              나")
    bad1 = bad1 + message_content.find("존1나")
    bad1 = bad1 + message_content.find("존2나")
    bad1 = bad1 + message_content.find("존3나")
    bad1 = bad1 + message_content.find("존4나")
    bad1 = bad1 + message_content.find("존5나")
    bad1 = bad1 + message_content.find("존6나")
    bad1 = bad1 + message_content.find("존7나")
    bad1 = bad1 + message_content.find("존8나")
    bad1 = bad1 + message_content.find("존9나")
    bad1 = bad1 + message_content.find("존#나")
    bad1 = bad1 + message_content.find("존$나")
    bad1 = bad1 + message_content.find("존%나")
    bad1 = bad1 + message_content.find("존^나")
    bad1 = bad1 + message_content.find("존&나")
    bad1 = bad1 + message_content.find("존*나")
    bad1 = bad1 + message_content.find("존~나")
    bad1 = bad1 + message_content.find("존1나")#28
    bad1 = bad1 + message_content.find("존{나")
    bad1 = bad1 + message_content.find("존}나")
    bad1 = bad1 + message_content.find("존[나")
    bad1 = bad1 + message_content.find("존]나")
    bad1 = bad1 + message_content.find("존;나")
    bad1 = bad1 + message_content.find("존'나")
    bad1 = bad1 + message_content.find("존:나")
    bad1 = bad1 + message_content.find("존\나")
    bad1 = bad1 + message_content.find("존|나")
    bad1 = bad1 + message_content.find("존`나")
    bad1 = bad1 + message_content.find("시바")
    bad1 = bad1 - message_content.find("시바견")
    bad1 = bad1 + message_content.find("쳐발")
    bad1 = bad1 + message_content.find("리발")
    bad1 = bad1 + message_content.find("시부랄")





    if bad1 >= -244 :
        await message.delete() 
        a = await message.channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 언어 포함]")
        await message.delete() 
        await asyncio.sleep(7)
        await a.delete()


    #폐드립
    bad2 = message_content.find("ㄴㄱㅁ")
    bad2 = bad2 + message_content.find("느금마")
    bad2 = bad2 + message_content.find("니 엄마")
    bad2 = bad2 + message_content.find("느그 어머니")
    bad2 = bad2 + message_content.find("폐륜")
    bad2 = bad2 + message_content.find("느그어미")#6
    bad2 = bad2 + message_content.find("ㄴㄱ마")
    bad2 = bad2 + message_content.find("느금ㅁ")
    bad2 = bad2 + message_content.find("니 애미")
    bad2 = bad2 + message_content.find("니애미")
    bad2 = bad2 + message_content.find("니@ㅐ미")
    bad2 = bad2 + message_content.find("ㄴㅇㅁ")
    bad2 = bad2 + message_content.find("애미")
    bad2 = bad2 + message_content.find("@ㅐ미")
    bad2 = bad2 + message_content.find("니 아비")
    bad2 = bad2 + message_content.find("니미씹")
    bad2 = bad2 + message_content.find("니아비")
    bad2 = bad2 + message_content.find("니아배")
    bad2 = bad2 + message_content.find("니어미")
    bad2 = bad2 + message_content.find("니 어미")
    bad2 = bad2 + message_content.find("뉘뮈")#21
    bad2 = bad2 + message_content.find("애⨈미")
    bad2 = bad2 + message_content.find("애⨉미")
    bad2 = bad2 + message_content.find("넉엄마")
    bad2 = bad2 + message_content.find("OH미")
    bad2 = bad2 + message_content.find("oH미")
    bad2 = bad2 + message_content.find("ㅇH미")
    bad2 = bad2 + message_content.find("ㄴ7ㅁ")
    bad2 = bad2 + message_content.find("@ㅐㅁㅣ")
    bad2 = bad2 + message_content.find("애ଅ미")
    bad2 = bad2 + message_content.find("ㄴㄱ.ㅁ")
    bad2 = bad2 + message_content.find("애1미")
    bad2 = bad2 + message_content.find("ㄴ.ㄱ.ㅁ")
    
    
    
    if bad2 >= -32 :
        await message.delete() 
        a = await message.channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:부모욕 포함]")
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
    bad3 = bad3 + message_content.find("질내사정")
    bad3 = bad3 + message_content.find("hentai")
    bad3 = bad3 + message_content.find("HENTAI")
    bad3 = bad3 - message_content.find("자지마")
    bad3 = bad3 - message_content.find("보지마")
    bad3 = bad3 + message_content.find("섿스")
    bad3 = bad3 - message_content.find("자지러")
    bad3 = bad3 + message_content.find("섹.스")
    bad3 = bad3 - message_content.find("좇다")
    bad3 = bad3 - message_content.find("좇아")
    bad3 = bad3 + message_content.find("쫓")
    bad3 = bad3 + message_content.find("se X")
    bad3 = bad3 + message_content.find("sex")
    bad3 = bad3 + message_content.find("셱스")
    bad3 = bad3 - message_content.find("건조까")#20
    bad3 = bad3 + message_content.find("쎽스")
    bad3 = bad3 - message_content.find("자나보지")
    bad3 = bad3 + message_content.find("SeX")
    bad3 = bad3 + message_content.find("sEx")
    bad3 = bad3 + message_content.find("SEx")
    bad3 = bad3 + message_content.find("sEX")
    bad3 = bad3 + message_content.find("seX")
    bad3 = bad3 - message_content.find("보지 않")
    bad3 = bad3 - message_content.find("보지도 않")
    bad3 = bad3 - message_content.find("보지도 마")
    
    
    if bad3 >= -21 :
        await message.delete() 
        a = await message.channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:성적발언 포함]") 
        await asyncio.sleep(7)
        await a.delete()
    
    #외국어 욕설
    bad4 = message_content.find("fuck")
    bad4 = bad4 + message_content.find("쉣")
    bad4 = bad4 + message_content.find("퍽큐")
    bad4 = bad4 + message_content.find("FUCK")
    bad4 = bad4 + message_content.find("Fuck")
    bad4 = bad4 + message_content.find("ファック")
    bad4 = bad4 + message_content.find("他妈的")#11
    bad4 = bad4 + message_content.find("뻑큐")
    bad4 = bad4 + message_content.find("뻐큐")
    bad4 = bad4 + message_content.find("뻑큐")
    bad4 = bad4 + message_content.find("뽁큐")
    bad4 = bad4 + message_content.find("℉uck")
    bad4 = bad4 + message_content.find("fūck")#14
    bad4 = bad4 + message_content.find("shut up")
    bad4 = bad4 + message_content.find("SHUT UP")
    bad4 = bad4 + message_content.find("Shut up")
    bad4 = bad4 + message_content.find("Shut Up")
    bad4 = bad4 + message_content.find("ᖴᑘᑢᖽᐸ")
    bad4 = bad4 + message_content.find("퍼킹")
    bad4 = bad4 + message_content.find("퍽킹")
    
    
    
    
    if bad4 >= -19 :
        await message.delete() 
        a = await message.channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:외국어욕 포함]")
        await asyncio.sleep(7)
        await a.delete()


    #비하발언
    bad5 = message_content.find("따까리")
    bad5 = bad5 + message_content.find("찐따")
    bad5 = bad5 + message_content.find("미친놈")
    bad5 = bad5 + message_content.find("싸가지")#3
    bad5 = bad5 + message_content.find("쌍년")
    bad5 = bad5 + message_content.find("미틴년")
    bad5 = bad5 + message_content.find("미친년")
    bad5 = bad5 + message_content.find("창년")
    bad5 = bad5 + message_content.find("잡년")
    bad5 = bad5 + message_content.find("걸레년")
    bad5 = bad5 + message_content.find("걸래년")
    bad5 = bad5 + message_content.find("tns년")
    bad5 = bad5 + message_content.find("TNS년")
    bad5 = bad5 + message_content.find("도구년")
    
    
    if bad5 >= -13 :
        await message.delete() 
        a = await message.channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:비하발언 포함]")
        await asyncio.sleep(7)
        await a.delete()

    #이모티콘 특수문자
    bad6 = message_content.find("🖕🏻")
    bad6 = bad6 + message_content.find("👌🏻👈🏻")
    bad6 = bad6 + message_content.find("👉🏻👌🏻")
    bad6 = bad6 + message_content.find("🤏🏻")

    if bad6 >= -3 :
        await message.delete() 
        a = await message.channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 이모티콘 포함]")
        await asyncio.sleep(7)
        await a.delete()
    
        
        
    if  message.author.display_name == "씨발" :
        a = await message.channel.send(message.author.name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 닉네임]")
        await message.delete() 
        await asyncio.sleep(7)
        await a.delete()
    if  message.author.display_name == "느금마" :
        a = await message.channel.send(message.author.name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 닉네임]")
        await message.delete() 
        await asyncio.sleep(7)
        await a.delete()
    if  message.author.display_name == "병신" :
        a = await message.channel.send(message.author.name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 닉네임]")
        await message.delete() 
        await asyncio.sleep(7)
        await a.delete()
    if  message.author.display_name == "느검" :
        if message_content.find("마") == 0 :    
            a = await message.channel.send(message.author.name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 닉네임]")
            await message.delete() 
            await asyncio.sleep(7)
            await a.delete()
    if  message.author.display_name == "씨" :
        if message_content.find("발") == 0 :    
            a = await message.channel.send(message.author.name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 닉네임]")
            await message.delete() 
            await asyncio.sleep(7)
            await a.delete()
    
    
    
    channel = client.get_channel(854918431597920256)
    embed = discord.Embed(title=f"전송", description=f"서버 : {message.guild.name} \n유저 : {message.author}", color=0x00FF64)
    embed.add_field(name="전송된 내용", value=f"내용 : {message.content}", inline=False)
    embed.set_footer(text=f"TNS 봇 ")
    await channel.send(embed=embed)
    
    
    adm = 0 #adm아니면 0 관리자는 1 개발자는 2
    if message.author.id == 731713372990603296 : #Tanat
        adm = 1
    if message.author.id == 664851821701103616 : #Pines
        adm = 2
    if message.author.id == 548127237954600971 : #웅엥웅
        adm = 0
    if message.author.id == 424477748044627968 : #just그냥이
        adm = 3
        
    if message.content == "!embed" :
        await message.delete()
        if adm == 1 :
            await message.channel.send("TNS봇 관리자 "+message.author.mention+"님이 "+message.guild.name+"서버에 참여 중 입니다")
        if adm == 2 :
            await message.channel.send("TNS봇 개발자 "+message.author.mention+"님이 "+message.guild.name+"서버에 참여 중 입니다")
        if adm == 3 :
            await message.channel.send("이상한 관종 "+message.author.mention+"님이 "+message.guild.name+"서버에 참여 중 입니다")
            
    if message.content == "!도배" :
        await message.delete()
        if adm == 1 :
            await message.channel.send("TNS관리자:도배 금지입니다.")
        if adm == 2 :
            await message.channel.send("TNS개발자:도배 금지입니다.")
    if message.content == "!잡담" :
        await message.delete()
        if adm == 1 :
            await message.channel.send("TNS관리자:잡담 금지입니다.")
        if adm == 2 :
            await message.channel.send("TNS개발자:잡담 금지입니다.")
    if message.content == "!성의" :
        await message.delete()
        if adm == 1 :
            await message.channel.send("TNS관리자:성의없는 질문 금지입니다.")
        if adm == 2 :
            await message.channel.send("TNS개발자:성의없는 질문 금지입니다.")
    if message.content == "!심심" :
        await message.delete()
        if adm == 1 :
            await message.channel.send("TNS관리자가 심심해 합니다.")
        if adm == 2 :
            await message.channel.send("TNS개발자가 심심해 합니다.")
    if message.content == "!조용" :
        await message.delete()
        if adm == 1 :
            await message.channel.send("TNS관리자가 누군가 조용히 하길 원합니다.")
        if adm == 2 :
            await message.channel.send("TNS개발자가 누군가 조용히 하길 원합니다.")
    if message.content == "!훈수" :
        await message.delete()
        if adm == 1 :
            await message.channel.send("TNS관리자:훈수 금지입니다.")
        if adm == 2 :
            await message.channel.send("TNS개발자:훈수 금지입니다.")
    if message.content == "!홍보" :
        await message.delete()
        if adm == 1 :
            await message.channel.send("TNS관리자:홍보 금지입니다.")
        if adm == 2 :
            await message.channel.send("TNS개발자:홍보 금지입니다.")
    if message.content == "!관리자" :
        if adm == 1 :
            await message.delete()
            role = discord.utils.get(message.guild.roles, name="관리자")
            await message.author.add_roles(role)
  
    badp = bad+bad1+bad2+bad3+bad4+bad5
    
    if message.content.startswith("!청소 "):
        if adm == 1 :
            purge_number = message.content.replace("!청소 ", "")
            check_purge_number = purge_number.isdigit()

            if check_purge_number == True:
                await message.channel.purge(limit=int(purge_number) + 1)
                msg = await message.channel.send(f"**{purge_number}개**의 메시지를 삭제했습니다.")
                await asyncio.sleep(5)
                await msg.delete()

            else:
                await message.channel.send("올바른 값을 입력해주세요.")
    

    def check(m):
	return m.channel.id == message.channel.id and m.author == message.author
    if message.content == "씨" :
        try:
	        msg = await client.wait_for('발', timeout=60.0, check=check)
        except asyncio.TimeoutError:
	        
        else:
	        await message.delete() 
                a = await message.channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:비하발언 포함]")
                await asyncio.sleep(7)
                await a.delete()
             
@client.event
async def on_message_delete(message):
    if message.guild.id == 653083797763522580 : return
    


    if message.author.bot:return
    
    
    channel = client.get_channel(854918431597920256)
    embed = discord.Embed(title=f"삭제됨", description=f"서버 : {message.guild.name} ({message.guild.id}) \n채널 : {message.channel.name} ({message.channel.id}) \n유저 : {message.author} ({message.author.id})", color=0xFF0000)
    embed.add_field(name="삭제된 내용", value=f"내용 : {message.content}", inline=False)
    embed.set_footer(text=f"TNS 봇 ")
    await channel.send(embed=embed)
    

    

    if message.channel.id ==850316721989877780:return
    if message.channel.id ==842673635478339625:return
    if message.guild.id ==829703185001611285:return
    if message.channel.id ==829972943705997312:return
    if message.channel.id ==774639716548214804:return
    if message.channel.id ==854235324653633538:return
    if message.guild.id == 856905070280179723 :return
    if message.channel.id ==706162734160543776:return

    chennalID = 0
    if message.channel.id == 858552903659683851 :
        chennalID=849536197273059338

    if message.guild.id == 852772557911228428 : #정천중학교
        chennalID=853509254606225418

    if message.guild.id == 842652067763453964 :
        chennalID=853509288109539368
        
    if message.guild.id == 764348395510431755 :
        chennalID=853509428970782780
        
    if message.guild.id == 349414439147274245 : #달밤
        chennalID=855319991003381760

    if message.guild.id == 854267517526867978 :
        chennalID=858706381515522069

    
    channel = client.get_channel(chennalID)
    embed = discord.Embed(title=f"삭제함", description=f"유저 : {message.author.display_name} \n유저ID : {message.author} \n서버 : {message.guild.name} \n채널 : {message.channel}", color=0xFF0000)
    embed.add_field(name="삭제된 내용", value=f"내용 : {message.content}", inline=False)
    embed.set_footer(text=f"TNS 봇")
    await channel.send(embed=embed)

    
    





access_token = os.environ["token"]
client.run(access_token)
