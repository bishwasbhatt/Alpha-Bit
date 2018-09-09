import discord
from discord.ext import commands

TOKEN = 'NDcyMjU0MzcxNzQ5NDI5MjU4.Djwsuw.cW2up0aQFY7gXBgFqtLm-z6MzK4'

client = commands.Bot(command_prefix = '*')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Not Fortnite'))
    print('Alpha Bit has joined the lobby.')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()




@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name ='Humans')
    await client.add_roles(member, role)

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted.')

@client.command()
async def ping():
    await client.say('Pong!')

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        color = discord.Color.green()
    )

    embed.set_author(name='Help')
    embed.add_field(name='*ping', value='Returns Pong!', inline=False)

    await client.send_message(author, embed=embed)

client.run(TOKEN)
