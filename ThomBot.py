import discord
import asyncio
from datetime import datetime
from discord.ext import commands

prefix = '$'

bot = commands.Bot(command_prefix=prefix)
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
	embed.add_field(name=f'{prefix}help', value=('Displays this message.'), inline=True)
	embed.add_field(name=f'{prefix}say <message>', value=('Makes bot say message'), inline=True)
	embed.add_field(name=f'{prefix}noot', value=('Noot Noot!'), inline=True)
	embed.add_field(name=f'{prefix}time', value=('Displays UK time'), inline=False)
	await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, message):
	await ctx.send(message)

@bot.command()
async def noot(ctx):
	await ctx.send('Noot Noot!')

@bot.command()
async def time(ctx):
	current_time = datetime.today().strftime('%H:%M:%S')
	embed = discord.Embed(color=0x0080ff)
	embed.add_field(name=':alarm_clock: Time:', value=(f'Current UK time is: {current_time}'), inline=True)
	await ctx.send(embed=embed)

bot.run('')