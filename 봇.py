
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
    message_content = message.content
    
    bad = message_content.find("ㅅㅂ")
    bad = bad + message_content.find("ㅂㅅ")
    bad = bad + message_content.find("ㅄ")
    bad = bad + message_content.find("ㅈㄴ")
    bad = bad + message_content.find("ㅈㄹ")
    bad = bad + message_content.find("ㅈㄹㄴ")
    bad = bad + message_content.find("1ㅂ")
    bad = bad + message_content.find("ㅅ ㅂ")
    bad = bad + message_content.find("ㄷㅊ")
    bad = bad + message_content.find("ㅗ")
    bad = bad + message_content.find("ㄷ ㅊ")
    bad = bad + message_content.find("ㄲㅈ")
    bad = bad + message_content.find("2ㅂ")
    bad = bad + message_content.find("3ㅂ")
    bad = bad + message_content.find("4ㅂ")
    bad = bad + message_content.find("5ㅂ")
    bad = bad + message_content.find("6ㅂ")
    bad = bad + message_content.find("7ㅂ")
    bad = bad + message_content.find("8ㅂ")
    bad = bad + message_content.find("9ㅂ")
    bad = bad + message_content.find("#ㅂ")
    bad = bad + message_content.find("$ㅂ")
    bad = bad + message_content.find("%ㅂ")
    bad = bad + message_content.find("^ㅂ")
    bad = bad + message_content.find("&ㅂ")
    bad = bad + message_content.find("*ㅂ")
    bad = bad + message_content.find("~ㅂ")
    bad = bad + message_content.find("1ㅂ")#28
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
    bad = bad + message_content.find("╭∩╮")#64
    bad = bad + message_content.find("ㅁㅊ")


    if bad >= -65 :
        await message.delete() 
        a = await message.channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 초성 또는 특수문자 포함]")
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
    bad1 = bad1 - message_content.find("시발점")
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
    bad1 = bad1 + message_content.find("#발")
    bad1 = bad1 + message_content.find("$발")
    bad1 = bad1 + message_content.find("%발")
    bad1 = bad1 + message_content.find("^발")
    bad1 = bad1 + message_content.find("&발")
    bad1 = bad1 + message_content.find("*발")
    bad1 = bad1 + message_content.find("~발")
    bad1 = bad1 + message_content.find("시1발")#64
    bad1 = bad1 + message_content.find("!발")
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
    bad1 = bad1 + message_content.find("@발")
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
    bad1 = bad1 + message_content.find("@쳐")
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
    bad1 = bad1 + message_content.find("1나")
    bad1 = bad1 + message_content.find("2나")
    bad1 = bad1 + message_content.find("3나")
    bad1 = bad1 + message_content.find("4나")
    bad1 = bad1 + message_content.find("5나")
    bad1 = bad1 + message_content.find("6나")
    bad1 = bad1 + message_content.find("7나")
    bad1 = bad1 + message_content.find("8나")
    bad1 = bad1 + message_content.find("9나")
    bad1 = bad1 + message_content.find("#나")
    bad1 = bad1 + message_content.find("존$나")
    bad1 = bad1 + message_content.find("%나")
    bad1 = bad1 + message_content.find("^나")
    bad1 = bad1 + message_content.find("&나")
    bad1 = bad1 + message_content.find("*나")
    bad1 = bad1 + message_content.find("존~나")
    bad1 = bad1 + message_content.find("1나")#28
    bad1 = bad1 + message_content.find("{나")
    bad1 = bad1 + message_content.find("}나")
    bad1 = bad1 + message_content.find("[나")
    bad1 = bad1 + message_content.find("]나")
    bad1 = bad1 + message_content.find(";나")
    bad1 = bad1 + message_content.find('존"나')
    bad1 = bad1 + message_content.find(":나")
    bad1 = bad1 + message_content.find("\나")
    bad1 = bad1 + message_content.find("|나")
    bad1 = bad1 + message_content.find("`나")
    bad1 = bad1 + message_content.find("시바")
    bad1 = bad1 - message_content.find("시바견")
    bad1 = bad1 + message_content.find("쳐발")
    bad1 = bad1 + message_content.find("리발")
    bad1 = bad1 + message_content.find("시부랄")
    bad1 = bad1 + message_content.find("c발")
    bad1 = bad1 + message_content.find("C발")
    bad1 = bad1 - message_content.find("시발유")
    bad1 = bad1 - message_content.find("시발역")
    bad1 = bad1 - message_content.find("시발택시")
    bad1 = bad1 - message_content.find("시발수뢰")
    bad1 = bad1 - message_content.find("지랄배기")
    bad1 = bad1 - message_content.find("지랄탄")
    bad1 = bad1 - message_content.find("미친증")
    bad1 = bad1 - message_content.find("지랄버릇")
    bad1 = bad1 + message_content.find("띠발")
    bad1 = bad1 + message_content.find("시불")
    bad1 = bad1 + message_content.find("쉬발")
    bad1 = bad1 + message_content.find("려차")
    bad1 = bad1 + message_content.find("人Ｈ刀I")
    bad1 = bad1 + message_content.find("새키")#242
    bad1 = bad1 + message_content.find("2신")
    bad1 = bad1 + message_content.find("3신")
    bad1 = bad1 + message_content.find("4신")
    bad1 = bad1 + message_content.find("5신")
    bad1 = bad1 + message_content.find("6신")
    bad1 = bad1 + message_content.find("7신")
    bad1 = bad1 + message_content.find("8신")
    bad1 = bad1 + message_content.find("9신")
    bad1 = bad1 + message_content.find("병#신")
    bad1 = bad1 + message_content.find("$신")
    bad1 = bad1 + message_content.find("%신")
    bad1 = bad1 + message_content.find("^신")
    bad1 = bad1 + message_content.find("&신")
    bad1 = bad1 + message_content.find("*신")
    bad1 = bad1 + message_content.find("병~신")
    bad1 = bad1 + message_content.find("1신")
    bad1 = bad1 + message_content.find("병!신")#27
    bad1 = bad1 + message_content.find("스키들")
    bad1 = bad1 + message_content.find("개스키")#276
    bad1 = bad1 + message_content.find("^ㅟ발")
    bad1 = bad1 + message_content.find("ㅆl발")
    bad1 = bad1 + message_content.find("ㅅl발")
    bad1 = bad1 + message_content.find("씨/발")
    bad1 = bad1 + message_content.find("/발")
    bad1 = bad1 + message_content.find("/신")
    bad1 = bad1 + message_content.find("/랄")#283
    bad1 = bad1 + message_content.find("/끼")#269
    bad1 = bad1 + message_content.find("씨10발")
    bad1 = bad1 + message_content.find("씨11발")
    bad1 = bad1 + message_content.find("씨12발")
    bad1 = bad1 + message_content.find("씨13발")
    bad1 = bad1 + message_content.find("씨14발")
    bad1 = bad1 + message_content.find("씨15발")
    bad1 = bad1 + message_content.find("씨16발")
    bad1 = bad1 + message_content.find("씨17발")
    bad1 = bad1 + message_content.find("씨18발")
    bad1 = bad1 + message_content.find("씨19발")
    bad1 = bad1 + message_content.find("씨20발")
    bad1 = bad1 + message_content.find("씨21발")
    bad1 = bad1 + message_content.find("씨22발")
    bad1 = bad1 + message_content.find("씨23발")
    bad1 = bad1 + message_content.find("씨24발")
    bad1 = bad1 + message_content.find("씨25발")
    bad1 = bad1 + message_content.find("씨26발")
    bad1 = bad1 + message_content.find("씨27발")
    bad1 = bad1 + message_content.find("씨28발")
    bad1 = bad1 + message_content.find("씨29발")
    bad1 = bad1 + message_content.find("시10발")
    bad1 = bad1 + message_content.find("시11발")
    bad1 = bad1 + message_content.find("시12발")
    bad1 = bad1 + message_content.find("시13발")
    bad1 = bad1 + message_content.find("시14발")
    bad1 = bad1 + message_content.find("시15발")
    bad1 = bad1 + message_content.find("시16발")
    bad1 = bad1 + message_content.find("시17발")
    bad1 = bad1 + message_content.find("시18발")
    bad1 = bad1 + message_content.find("시19발")
    bad1 = bad1 + message_content.find("시20발")
    bad1 = bad1 + message_content.find("시21발")
    bad1 = bad1 + message_content.find("시22발")
    bad1 = bad1 + message_content.find("시23발")
    bad1 = bad1 + message_content.find("시24발")
    bad1 = bad1 + message_content.find("시25발")
    bad1 = bad1 + message_content.find("시26발")
    bad1 = bad1 + message_content.find("시27발")
    bad1 = bad1 + message_content.find("시28발")
    bad1 = bad1 + message_content.find("시29발")
    bad1 = bad1 + message_content.find("Sibal")
    bad1 = bad1 + message_content.find("sibal")
    bad1 = bad1 + message_content.find("Subal")
    bad1 = bad1 + message_content.find("subal")
    bad1 = bad1 + message_content.find("ToRl")
    
    
    


    if bad1 >= -314 :
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
    bad2 = bad2 + message_content.find("애/미")#33
    
    
    
    if bad2 >= -33 :
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
    bad3 = bad3 - message_content.find("해보지")
    bad3 = bad3 + message_content.find("ㅈ망")
    bad3 = bad3 + message_content.find("ㅈ까")
    bad3 = bad3 - message_content.find("보지말")
    bad3 = bad3 - message_content.find("보지 말")
    bad3 = bad3 + message_content.find("파이즈리")
    bad3 = bad3 + message_content.find("오나홀")
    bad3 = bad3 + message_content.find("페라치오")
    bad3 = bad3 + message_content.find("팸돔")
    bad3 = bad3 + message_content.find("좃까")
    bad3 = bad3 - message_content.find("나 보지")
    bad3 = bad3 - message_content.find("가 보지")
    bad3 = bad3 + message_content.find("소추")
    bad3 = bad3 - message_content.find("보지않")
    bad3 = bad3 + message_content.find("섻")
    bad3 = bad3 + message_content.find("섹ㅅ")
    
    
    if bad3 >= -25 :
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
    bad4 = bad4 + message_content.find("^tt^")
    bad4 = bad4 + message_content.find("son of")
    bad4 = bad4 + message_content.find("mother")
    bad4 = bad4 + message_content.find("fat ass")
    bad4 = bad4 + message_content.find("Fat ass")
    bad4 = bad4 + message_content.find("Fat Ass")
    bad4 = bad4 + message_content.find("bitch")
    bad4 = bad4 + message_content.find("Son of")
    bad4 = bad4 + message_content.find("Bloody hell")
    bad4 = bad4 + message_content.find("傻逼")
    bad4 = bad4 + message_content.find("王八蛋")
    bad4 = bad4 + message_content.find("找死吗")
    
    
    
    
    if bad4 >= -31 :
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
    bad5 = bad5 + message_content.find("썅뇬")
    bad5 = bad5 + message_content.find("쌍놈")
    
    
    if bad5 >= -15 :
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
        
    text = message.content
    newtext1 = ''.join(char for char in text if char.isalnum())
    newtext2 = re.sub(r'[0-9]+', '', newtext1)
    bad = ["씨발", "병신", "닥쳐","시발"]
    
    await message.channel.send(newtext2)
    for i in bad:
        if i in text:
            return
    for i in bad:
        if i in newtext2:
            await message.delete()
            
            
    #특수
    if message.content.startswith('씨'):
        channel = message.channel
        def check(m):
            return m.content == ("발") and m.channel == channel
        msg = await client.wait_for('message', check=check)
        await message.delete()
        a = await channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 언어 포함]")
        await asyncio.sleep(7)
        await a.delete()
    if message.content.startswith('시'):
        channel = message.channel
        def check(m):
            return m.content == ("발") and m.channel == channel
        msg = await client.wait_for('message', check=check)
        await message.delete()
        a = await channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 언어 포함]")
        await asyncio.sleep(7)
        await a.delete()
    if message.content.startswith('병'):
        channel = message.channel
        def check(m):
            return m.content == ("신") and m.channel == channel
        msg = await client.wait_for('message', check=check)
        await message.delete()
        a = await channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 언어 포함]")
        await asyncio.sleep(7)
        await a.delete()
    if message.content.startswith('섹'):
        channel = message.channel
        def check(m):
            return m.content == ("스") and m.channel == channel
        msg = await client.wait_for('message', check=check)
        await message.delete()
        a = await channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 언어 포함]")
        await asyncio.sleep(7)
        await a.delete()
    if message.content.startswith('애'):
        channel = message.channel
        def check(m):
            return m.content == ("미") and m.channel == channel
        msg = await client.wait_for('message', check=check)
        await message.delete()
        a = await channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 언어 포함]")
        await asyncio.sleep(7)
        await a.delete()
    if message.content.startswith('쌔'):
        channel = message.channel
        def check(m):
            return m.content == ("끼") and m.channel == channel
        msg = await client.wait_for('message', check=check)
        await message.delete()
        a = await channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 언어 포함]")
        await asyncio.sleep(7)
        await a.delete()
    if message.content.startswith('지'):
        channel = message.channel
        def check(m):
            return m.content == ("랄") and m.channel == channel
        msg = await client.wait_for('message', check=check)
        await message.delete()
        a = await channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 언어 포함]")
        await asyncio.sleep(7)
        await a.delete()
    if message.content.startswith('ㅅ'):
        channel = message.channel
        def check(m):
            return m.content == ("ㅂ") and m.channel == channel
        msg = await client.wait_for('message', check=check)
        await message.delete()
        a = await channel.send(message.author.display_name+"님의 메세지가 삭제 되었습니다.\n[사유:부적절한 언어 포함]")
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
    
    

   
    





access_token = os.environ["token"]
client.run(access_token)
