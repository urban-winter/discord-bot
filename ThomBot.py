import discord

client = discord.Client()

@client.event
async def on_ready():
	print("The bot is ready!")
	await client.change_presence(activity=discord.Game(name="Making a bot"))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content == "Hello":
		await message.channel.send("Hello!")

client.run('NTcwMzU4NDkwOTkyNzM4MzE0.XL-B4w.Jp79yU5v34rXJX1sv13KqleIWAo')