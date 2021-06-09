import discord
import os

client = discord.Client()
access_token = os.environ["BOT_TOKEN"]

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game=discord.Game(name='', type=1))

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith('안녕'):
        channel = message.channel
        await channel.send('반가워!')
        
client.run(access_token)
