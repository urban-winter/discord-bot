import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
	print("The bot is ready!")
	await bot.change_presence(activity=discord.Game(name="Being Tilted"))

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	if message.content == "Hello":
		await message.channel.send("Hello!")

@bot.command()
async def say(ctx, arg):
	await ctx.send(arg)

bot.run('Token')