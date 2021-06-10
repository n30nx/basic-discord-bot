import discord
from time import sleep
from discord.ext import commands
from discord import utils
import random
import os
import ffmpeg

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

@client.command()
async def play(ctx, *args):
    words = ""
    for item in args:
        words += item + " "
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice == None:
        await connect(ctx)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    song = os.path.isfile("song.webm")
    
    try:
        if song:
            os.remove("song.webm")
    except PermissionError:
        await ctx.send("Please wait for the current audio to end or type !stop.")
        return

    os.system(f'youtube-dl -f "bestaudio[ext=webm]" "ytsearch:{words}"')
    for file in os.listdir("./"):
        if file.endswith(".webm"):
            os.rename(file, "song.webm")
    voice.play(discord.FFmpegPCMAudio("song.webm"))
		
		
		
		

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
