import random

import discord
from discord.ext import commands, tasks
import random
import time
import sup

TOKEN = 'OTY4MDI4MTkzMjkyNDMxMzYw.YmY4gg.9gIqmiDPqQcu4rdarzCEXu2QjhI'
intents = discord.Intents.default()
intents.members = True
job = sup.Counter()

client = commands.Bot(command_prefix='!')
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.command()
async def how(ctx):
    await ctx.send(":question::question::question: say the magic sentence to Mr.Bones and you will be freed"
                   " :question::question::question:")
    time.sleep(5)
    await ctx.send("Mr.Bones requires you to say the magic sentence. Follow the Blue Clues", tts=True)
    time.sleep(10)
    await ctx.send("https://imgur.com/a/zR9l2dL")

@client.command()
async def offme(ctx):
    channel = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    if channel and channel.is_connected():
        if ctx.author.voice:
            if job.count == 0:
                await ctx.send("https://imgur.com/eLvHusL")
                job.increse()
                return
            elif job.count == 1:
                if channel and channel.is_connected():
                    granted_sound = discord.FFmpegOpusAudio('endgame.wav')
                    time.sleep(2)
                    channel.play(granted_sound)
                    await ctx.send("https://imgur.com/a/z35AxCg")
                    while channel.is_playing():
                        time.sleep(0.1)
                    channel.stop()
                    job.rest()
                    await ctx.send(f":question::question::question:Mr.Bones offed {ctx.message.author} :question::question::question:")
                    await channel.disconnect()
                    return





@client.command()
async def wildride(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        if voice and voice.is_connected():
            wildride_sound = discord.FFmpegOpusAudio('wildride.mp3')
            time.sleep(2)
            await ctx.send("https://imgur.com/a/e0gMsGq")
            voice.play(wildride_sound)
            while voice.is_playing():
                time.sleep(0.1)
            voice.stop()
            return

@client.command()
async def bone(ctx):
    if ctx.author.voice:
        channel = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
        if channel and channel.is_connected():

            if str(ctx.author) == "Krusty#6852":
                granted_sound = discord.FFmpegOpusAudio('granted.wav')
                time.sleep(2)
                channel.play(granted_sound)
                while channel.is_playing():
                    time.sleep(0.1)
                await channel.disconnect()
            else:
                repeat_sound = discord.FFmpegOpusAudio('repeat.wav')
                time.sleep(2)
                channel.play(repeat_sound)
                while channel.is_playing():
                    time.sleep(0.1)




@client.command()
async def pls(ctx):
    if ctx.author.voice:
        channel = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
        if channel and channel.is_connected():
            i = random.randint(0, 10)
            if i in range(0, 7):
                error_sound = discord.FFmpegOpusAudio('error.wav')
                time.sleep(2)
                channel.play(error_sound)

            elif i in range(7, 10):
                clue_sound = discord.FFmpegOpusAudio('clues.wav')
                time.sleep(2)
                channel.play(clue_sound)

            elif i == 10:
                wrong_sound = discord.FFmpegOpusAudio('wrong.wav')
                time.sleep(2)
                channel.play(wrong_sound)
        while channel.is_playing():
            time.sleep(0.1)
        print("end")
        return


client.run(TOKEN)
