import discord
from time import sleep
from discord.ext import commands
from discord import utils
import random
import ffmpeg
import validators
import youtube_dl
import asyncio
from youtubesearchpython import VideosSearch

client = commands.Bot(command_prefix="!") # You can change command prefix

@client.command()
async def phrase(ctx):
	#Change this
	randomList = ["words"]
	a = len(randomList) + 1
	b = random.sample(range(1, a), 1)
	for num in b:
		c = int(num)
	await ctx.send(randomList[c-1])


@client.command()
async def connect(ctx):
	voiceChannel = ctx.author.voice.channel
	voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
	if voice == None:
		await voiceChannel.connect()
		await ctx.guild.change_voice_state(channel=voiceChannel, self_mute = False, self_deaf = True)
		await ctx.send(f"Connected to {voiceChannel}")
	else:
		await ctx.send("I am already connected.")

	
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
@client.command()
async def play(ctx, *args):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    arg = ""
    for item in args:
        arg += item + " "
       
    if arg == "":
        await ctx.send("Empty search")
    global YDL_OPTIONS
    global FFMPEG_OPTIONS

    if voice == None:
        await bağlan(ctx)
        await asyncio.sleep(3)
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    
    if not validators.url(arg):
        videosSearch = VideosSearch(arg, limit = 1).result()
        url = videosSearch["result"][0]["link"]

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
    url = info['formats'][0]['url']
    songTitle = videosSearch["result"][0]["title"]

    if not voice.is_playing():
        voice.play(discord.FFmpegPCMAudio(url, **FFMPEG_OPTIONS))
        await ctx.send(f"Now Playing: {songTitle}")
    return

@client.command()
async def disconnect(ctx):
	voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
	if voice != None:
		await voice.disconnect()
		await ctx.send("Disconnected")
	else:
		await ctx.send("I am not connected.")

@client.command()
async def pause(ctx):
	voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
	if voice != None:
		voice.pause()
		await ctx.send("Paused.")

@client.command()
async def stop(ctx):
	voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
	if voice != None:
		voice.stop()
		await ctx.send("Stopped.")

@client.command()
async def resume(ctx):
	voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
	if voice.is_paused():
		voice.resume()

@client.command()
async def clear(ctx, amount):
	await ctx.channel.purge(limit = int(amount))

@client.command()
async def create_invite_link(ctx):
        inviteLink = await ctx.channel.create_invite(max_uses=1,unique=True)
        await ctx.author.send(inviteLink)

@client.command()
async def commands(ctx):
	await ctx.send(f"You should use '!' before the commands. \nconnect: Bot connects to the channel. \nplay: Bot plays song. \ndisconnect: Bot disconnects. \npause: Bot pauses the audio. \nstop: Bot stops the audio. \nresume: Bot resumes the audio. \ncreate_invite_link: Creates an invite link and sends to the person who used the command. \nphrase:")


client.run('YOUR TOKEN')
