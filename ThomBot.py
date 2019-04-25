import discord
import asyncio
from discord.ext import commands

user_display_name = ''
user_avatar_url = ''

bot = commands.Bot(command_prefix='$')
bot.remove_command('help')

@bot.event
async def on_ready():
	print("The bot is ready!")
	await bot.change_presence(activity=discord.Game(name="Being Tilted"))

@bot.listen()
async def on_message(message):
	if message.author != bot.user:
		print(message.author.display_name)

@bot.command()
async def help(ctx):
	embed = discord.Embed(title='Commands:', color=0x0080ff)
	embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
	embed.add_field(name='$say <message>', value=('Makes bot repeat message'), inline=True)
	await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, message):
	await ctx.send(message)

bot.run('')