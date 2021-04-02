import discord
import os
from discord.ext import commands
import asyncio


intents = discord.Intents(messages = True, guilds = True, members = True)
client = commands.Bot(command_prefix = 'o!', intents = intents)

def check_if_it_is_me(ctx):
    return ctx.message.author.id == 400658261512159232




@client.event
async def on_ready():          
    
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Join now Team Ocean! ", url='https://twitch.tv/th__gamer'))
    
    print('Ready')




@client.command()
@commands.check(check_if_it_is_me)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
  
    await ctx.send(f'{extension} wurde aktiviert')

@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} wurde deaktiviert')

@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} wurde neu aktiviert')









for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzExNTY4ODM0NTkwNDA4NzY1.XsE6Hg.0UMjWqRmv_afqQNKLO-DkXy7U9U')
