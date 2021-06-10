<h2> It's only working on linux so if you want to run this on windows turn on WSL and download a linux distro from Microsoft Store. </h2>

<p>
  <a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python->=_3.8-royalblue.svg"></a>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#customization">Customization</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#wsl">WSL</a>
</p>

## Installation

```console
# Clone the discord bot
$ git clone https://github.com/n30nx/basic_discord_bot.git

# cd to basic_discord_bot directory
$ cd basic_discord_bot

# Install the python's requirements.
$ python3 -m pip install -r requirements.txt

# Install youtube-dl for bot.
$ sudo snap install youtube-dl  # DEBIAN
$ sudo pacman -S youtube-dl    # ARCH
$ sudo snap install youtube-dl  # FEDORA
```

## Usage

Change <q>YOUR TOKEN</q> to your discord token. If you don't have one go to <a href="https://discord.com/developers">discord's developers page</a>, log in and click to New Application button. And give your project a name. Then go to the bot section on that new page and create a bot. You can change the bot's name here. Then click on the <q>Click to Reveal Token</q> and copy that token and paste to the section below on code. 
```python
client.run('YOUR TOKEN')
```
Bot's invite link: https://discord.com/api/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.com&scope=bot

You can find out your bot's client id from General Information section, you can also directly generate your own invite link from OAuth2 section.

## Customization

I actually had a customized bot that i wrote and i decided to add this commands to that bot too. So you can basically change the words section below to bot to print some random phrases like "Yippee ki yay" :P.
```python
@client.command()
async def phrase(ctx):
	#Change this
	randomList = ["words"]
	a = len(randomList) + 1
	b = random.sample(range(1, a), 1)
	for num in b:
		c = int(num)
	await ctx.send(randomList[c-1])
```
You can also change that commands names.

And you can change the command prefix for the bot.
```python
client = commands.Bot(command_prefix="!") # You can change command prefix
```
Just change the ! to whatever you want.

You can edit the commands section too.

```python
@client.command()
async def commands(ctx):
	await ctx.send(f"You should use '!' before the commands. \nconnect: Bot connects to the channel. \nplay: Bot plays song. \ndisconnect: Bot disconnects. \npause: Bot pauses the audio. \nstop: Bot stops the audio. \nresume: Bot resumes the audio. \ncreate_invite_link: Creates an invite link and sends to the person who used the command. \nrandom:")
```


## WSL

First of all you should turn on Windows Subsystem for Linux:

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

Secondly you should download a linux distro from microsoft store than let it install and you're ready to start installation steps.



                                 
