import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
	print("The bot is ready!")
	await client.change_presence(activity=discord.Game(name="Being Tilted"))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content == "Hello":
		await message.channel.send("Hello!")

@bot.command()
async def say(ctx, arg):
	await ctx.send(arg)

client.run('TOKEN')