import discord

client = discor.client()

@client.event
async def on_ready():
	print("The bot is ready!")
	await client.change_presence(game=discord.Game(name="Making a bot"))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content == "Hello":
		await client.send_message(message.channel, "World")

client.run(NTcwMzU4NDkwOTkyNzM4MzE0.XL-B4w.Jp79yU5v34rXJX1sv13KqleIWAo)