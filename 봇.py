import discord
import os, requests
import numpy as np
import random, datetime
import nacl, ffmpeg
import youtube_dl
import asyncio
import time
import math

from youtubesearchpython import VideosSearch
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

queues = {}
musiclist = {}
nowplay = {}
vote = {}

client = discord.Client()
token = "token"

prf = "!"


        if "entries" in result:
            # Can be a playlist or a list of videos
            Video = result["entries"][0]
        else:
            m_url = result

            title = m_url["title"]

            msd = int(m_url["duration"])

            m_url = m_url["formats"][1]["url"]
        m_urld = url
        mant = f"[{title}]({m_urld}) 를 재생합니다!"
        try:
            is_p = message.guild.voice_client.is_playing()
        except AttributeError:
            is_p = False
        if is_p == True:  # 예약
            now_vol = 1
            player = discord.PCMVolumeTransformer(
                discord.FFmpegPCMAudio(
                    source=m_url,
                    before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
                ),
                volume=now_vol,
            )
            if server.id in queues:
                queues[server.id].append(player)
            else:
                queues[server.id] = [player]  # 딕셔너리 쌍 추가
            dgy = len(queues[server.id])
            mant = f"[{title}]({m_urld}) 를\n**{dgy}번** 대기열에 예약하였습니다!"
            start = time.time()
            mdp = [m_urld, title, message.author.id, msd]
            if server.id in musiclist:
                musiclist[server.id].append(mdp)
            else:
                musiclist[server.id] = [mdp]  # 딕셔너리 쌍 추가
            return await tg.edit(
                embed=discord.Embed(title=f"예약📥", description=f"{mant}", color=0x0170ED)
            )
        server = message.guild
        start = time.time()
        now_p = [m_urld, title, message.author.id, msd, start]
        if server.id in nowplay:  # 지금노래
            nowplay[server.id].append(now_p)
        else:
            nowplay[server.id] = [now_p]  # 딕셔너리 쌍 추가
        now_vol = 1
        source = discord.PCMVolumeTransformer(
            discord.FFmpegPCMAudio(
                source=m_url,
                before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            ),
            volume=now_vol,
        )
        try:
            mis = message.guild.voice_client.is_connected()
        except AttributeError:
            mis = False
        if mis == False:
            voice = await client.get_channel(message.author.voice.channel.id).connect()
            voice.play(
                source, after=lambda e: check_queue(message.guild.id, message.author.id)
            )
        else:
            message.guild.voice_client.play(
                source, after=lambda e: check_queue(message.guild.id, message.author.id)
            )
        await tg.edit(
            embed=discord.Embed(title=f"검색🔍", description=f"{mant}", color=0x0170ED)
        )

    if message.content == f"{prf}스킵":
        server = message.guild
        try:
            client.get_channel(message.author.voice.channel.id)
        except AttributeError:
            return await message.channel.send("먼저 음성채널에 참가해주세요!")
        try:
            if message.guild.voice_client.channel.id == message.author.voice.channel.id:
                try:
                    qd = nowplay[message.guild.id][0]
                    is_p = message.guild.voice_client.is_playing()
                except AttributeError:
                    return await message.channel.send("현재 노래가 재생중이 아닙니다!")
                except KeyError:
                    return await message.channel.send("현재 노래가 재생중이 아닙니다!")
                if is_p == True:
                    if int(qd[2]) == message.author.id:
                        if server.id in vote:
                            del vote[server.id]
                        message.guild.voice_client.stop()
                        return await message.channel.send(
                            embed=discord.Embed(
                                title=f"스킵⏭",
                                description=f"노래가 스킵되었습니다!",
                                color=0x0170ED,
                            )
                        )
                    else:
                        mvm = message.author.voice.channel.members
                        mvm_num = int(len(mvm))
                        server = message.guild
                        if server.id not in vote:
                            vote[server.id] = []
                        vote_d = [message.author.id]
                        if f"{message.author.id}" in str(vote[server.id]):
                            return await message.channel.send(
                                embed=discord.Embed(
                                    title=f"스킵⏭",
                                    description=f"이미 스킵에 투표하였습니다.",
                                    color=0x0170ED,
                                )
                            )
                        if server.id in vote:
                            vote[server.id].append(vote_d)
                        else:
                            vote[server.id] = [vote_d]  # 딕셔너리 쌍 추가
                        if mvm_num > 3:  # 2명보다 크다면
                            mvm_num_nng = int(round(mvm_num - 2, 2))
                            if int(len(vote[server.id])) == mvm_num_nng:
                                del vote[server.id]
                                message.guild.voice_client.stop()
                                return await message.channel.send(
                                    embed=discord.Embed(
                                        title=f"스킵⏭",
                                        description=f"재생중인 노래가 투표에 의해 스킵되었습니다.",
                                        color=0x0170ED,
                                    )
                                )
                            else:
                                return await message.channel.send(
                                    embed=discord.Embed(
                                        title=f"스킵⏭",
                                        description=f"스킵투표를 하였습니다. ({(len(vote[server.id]))}/{mvm_num_nng})투표",
                                        color=0x0170ED,
                                    )
                                )
                        else:
                            return await message.channel.send(
                                embed=discord.Embed(
                                    title=f"스킵⏭",
                                    description=f"참가인원이 2명밖에 없어 투표할수 없습니다.\n노래를 재생한사람이 스킵해주세요!",
                                    color=0x0170ED,
                                )
                            )

                        return await message.channel.send(
                            embed=discord.Embed(
                                title=f"스킵⏭",
                                description=f"자신이 추가한 노래만 스킵할 수 있습니다!",
                                color=0x0170ED,
                            )
                        )
                else:
                    await message.channel.send("현재 노래가 재생중이 아닙니다!")
            else:
                return await message.channel.send("PH봇과 같은 음성채널에 있어야합니다!")
        except AttributeError:
            return await message.channel.send(
                embed=discord.Embed(
                    title=f"스킵⏭", description=f"노래가 재생중이 아닙니다!", color=0x0170ED
                )
            )

    if message.content == f"{prf}지금노래":
        try:
            server = message.guild
            if server.id in nowplay:
                now_p = nowplay[server.id][0]
            else:
                return await message.channel.send("현재는 재생중인 노래가 없습니다.")
            if str(now_p[3]) == "LIVE":
                return await message.channel.send(
                    embed=discord.Embed(
                        title=f"지금노래🎵",
                        description=f"[{now_p[1]}]({now_p[0]}) [**{now_p[3]}**] 가 재생중입니다.\n재생한 사람 : <@{now_p[2]}>",
                        color=0x0170ED,
                    )
                )
            await message.channel.send(
                embed=discord.Embed(
                    title=f"지금노래🎵",
                    description=f"[{now_p[1]}]({now_p[0]}) 가 재생중입니다.\n{print_progress(int(time.time()) - int(now_p[4]),now_p[3])}**{hms((time.time()) - int(now_p[4]))}/{now_p[3]}**\n재생한 사람 : <@{now_p[2]}>",
                    color=0x0170ED,
                )
            )
        except IndexError:
            return await message.channel.send("현재는 재생중인 노래가 없습니다.")

    if message.content.startswith(f"{prf}대기열삭제"):
        try:
            client.get_channel(message.author.voice.channel.id)
        except AttributeError:
            return await message.channel.send("먼저 음성채널에 참가해주세요!")
        try:
            if message.guild.voice_client.channel.id == message.author.voice.channel.id:
                try:
                    num = int(message.content[7:])
                    server = message.guild
                    pd_n = len(musiclist[server.id])
                except IndexError:
                    return await message.channel.send(
                        embed=discord.Embed(
                            title=f"대기열삭제🗑",
                            description=f"노래가 재생중이 아닙니다.",
                            color=0x0170ED,
                        )
                    )
                except KeyError:
                    return await message.channel.send(
                        embed=discord.Embed(
                            title=f"대기열삭제🗑",
                            description=f"노래가 재생중이 아닙니다.",
                            color=0x0170ED,
                        )
                    )
                except ValueError:
                    return await message.channel.send(
                        embed=discord.Embed(
                            title=f"대기열삭제🗑",
                            description=f"명령어 사용법을 확인해주세요!\n!대기열삭제 [대기열번호(정수)]",
                            color=0x0170ED,
                        )
                    )
                try:
                    qd = musiclist[server.id][num - 1]
                except IndexError:
                    return await message.channel.send(
                        embed=discord.Embed(
                            title=f"대기열삭제🗑",
                            description=f"일치하는 대기열번호가 없습니다.",
                            color=0x0170ED,
                        )
                    )
                if num == 0:
                    return await message.channel.send(
                        embed=discord.Embed(
                            title=f"대기열삭제🗑",
                            description=f"일치하는 대기열번호가 없습니다.",
                            color=0x0170ED,
                        )
                    )
                if int(qd[2]) == message.author.id:
                    del queues[server.id][num - 1]
                    del musiclist[server.id][num - 1]
                    await message.channel.send(
                        embed=discord.Embed(
                            title=f"대기열삭제🗑",
                            description=f"대기열 **{num}**번이 삭제되었습니다.",
                            color=0x0170ED,
                        )
                    )
                else:
                    await message.channel.send(
                        embed=discord.Embed(
                            title=f"대기열삭제🗑",
                            description=f"자신이 추가한 노래만 삭제 가능합니다!",
                            color=0x0170ED,
                        )
                    )
            else:
                return await message.channel.send("PH봇과 같은 음성채널에 있어야합니다!")
        except AttributeError:
            return await message.channel.send(
                embed=discord.Embed(
                    title=f"대기열삭제🗑", description=f"노래가 재생중이 아닙니다!", color=0x0170ED
                )
            )

    if message.content == f"{prf}대기열":
        server = message.guild
        author = message.author
        try:
            con = ""
            num = 1
            i = 0
            try:
                while True:
                    da = musiclist[server.id][i]
                    if str(da[3]) == "LIVE":
                        da_cho = f"[**{da[3]}**]"
                    else:
                        da_cho = f"**{hms(da[3])}**"
                    con += f"{num}번 - [{da[1]}]({da[0]}) {da_cho} - <@{da[2]}>\n"
                    num += 1
                    i += 1
                    if i == 10:
                        break
            except:
                pass
            page_d = len(musiclist[server.id])
            if page_d > 10:

                page_d_m = page_d / 10
                max_p = math.ceil(page_d_m)
                page = 1
                embed = discord.Embed(
                    title="대기열🗃",
                    description=f"{con}",
                    color=0x0170ED,
                    timestamp=message.created_at,
                )
                embed.set_footer(
                    text=f"페이지 : {page} / {max_p}", icon_url=client.user.avatar_url
                )
                tg = await message.channel.send(embed=embed)
                while True:
                    await tg.add_reaction("◀")
                    await tg.add_reaction("⏹")
                    await tg.add_reaction("▶")

                    def diary_write_check(reaction, user):
                        return (
                            user == author
                            and str(reaction) in ["◀", "⏹", "▶"]
                            and tg.id == reaction.message.id
                        )  # 이모지 리액션 부분

                    reaction, user = await client.wait_for(
                        "reaction_add", timeout=30.0, check=diary_write_check
                    )  # 이모지 리액션 부분
                    if str(reaction.emoji) == "◀":
                        await tg.clear_reactions()
                        if page - 1 == 0:
                            con = ""
                            num = 1
                            i = 0
                            try:
                                while True:
                                    da = musiclist[server.id][i]
                                    if str(da[3]) == "LIVE":
                                        da_cho = f"[**{da[3]}**]"
                                    else:
                                        da_cho = f"**{hms(da[3])}**"
                                    con += f"{num}번 - [{da[1]}]({da[0]}) {da_cho} - <@{da[2]}>\n"
                                    num += 1
                                    i += 1
                                    if i == 10:
                                        break
                            except:
                                pass
                        else:
                            page = 1
                            con = ""
                            num = 1
                            i = 0
                            try:
                                while True:
                                    da = musiclist[server.id][i]
                                    if str(da[3]) == "LIVE":
                                        da_cho = f"[**{da[3]}**]"
                                    else:
                                        da_cho = f"**{hms(da[3])}**"
                                    con += f"{num}번 - [{da[1]}]({da[0]}) {da_cho} - <@{da[2]}>\n"
                                    num += 1
                                    i += 1
                                    if i == 10:
                                        break
                            except:
                                pass
                    if str(reaction.emoji) == "▶":
                        await tg.clear_reactions()
                        if page == max_p:
                            pass
                        else:
                            con = ""
                            fd = page * 10
                            num = fd + 1
                            i = fd
                            i_max = i + 10
                            try:
                                while True:
                                    da = musiclist[server.id][i]
                                    if str(da[3]) == "LIVE":
                                        da_cho = f"[**{da[3]}**]"
                                    else:
                                        da_cho = f"**{hms(da[3])}**"
                                    con += f"{num}번 - [{da[1]}]({da[0]}) {da_cho} - <@{da[2]}>\n"
                                    num += 1
                                    i += 1
                                    if i == i_max:
                                        break
                            except:
                                pass
                            page += 1

                    if str(reaction.emoji) == "⏹":
                        await tg.clear_reactions()
                        break

                    embed = discord.Embed(
                        title="대기열🗃",
                        description=f"{con}",
                        color=0x0170ED,
                        timestamp=message.created_at,
                    )
                    embed.set_footer(
                        text=f"페이지 : {page} / {max_p}", icon_url=client.user.avatar_url
                    )
                    await tg.edit(embed=embed)

            else:

                if con == "":
                    return await message.channel.send(
                        embed=discord.Embed(
                            title=f"대기열🗃",
                            description=f"현재 대기열이 비어있습니다.",
                            color=0x0170ED,
                        )
                    )
                await message.channel.send(
                    embed=discord.Embed(
                        title=f"대기열🗃", description=f"{con}", color=0x0170ED
                    )
                )
        except KeyError:
            await message.channel.send("대기중인 노래가 없습니다.")
        except asyncio.exceptions.TimeoutError:
            await tg.clear_reactions()
        
        
        
access_token = os.environ["token"]
client.run(access_token)
