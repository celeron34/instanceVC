import discord
import asyncio

TOKEN = 'your token'
intents = discord.Intents.all()
client = discord.Client(intents=intents)
instanceVCs = set()

@client.event
async def on_ready():
	print('Ready!')

@client.event
async def on_voice_state_update(member:discord.Member, before:discord.VoiceState, after:discord.VoiceState):
	if after.channel != None: # 参加したとき
		if member.voice.channel.name.lower() == 'createvc': # create instance
			# instanceVC生成＋移動
			instanceVC = await member.voice.channel.category.create_voice_channel('instanceVC')
			await member.move_to(instanceVC)
			instanceVCs.add(instanceVC)

	if before.channel != None: # 離脱したとき
		if before.channel.members == [] and before.channel in instanceVCs:
			await before.channel.delete()
			instanceVCs.remove(before.channel)

@client.event
async def on_error(e, args, kwargs):
	print(kwargs)

async def main():
	async with client:
		await client.start(TOKEN)

if __name__ == '__main__':
	asyncio.run(main())
