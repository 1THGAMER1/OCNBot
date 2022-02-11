import discord
from discord import member
import os
from discord.ext import commands
import asyncio
import json

from discord_components.client import DiscordComponents

#Custom Prefix


def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

        return prefixes[str(message.guild.id)]


intents = discord.Intents(messages = True, guilds = True, members = True)
client = commands.Bot(command_prefix = get_prefix, intents = intents)
'''
async def check_if_it_is_me(ctx):

    if ctx.message.author.id == 400658261512159232:

        await ctx.send('.', delete_after=1)
        return ctx.message.author.id == 400658261512159232
    else:
        await ctx.send('Du hast keine Berechtigung um diesen Command zu benutzen', delete_after=35)'''



@client.event
async def on_ready():          
    
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Version 1.2 unter Entwicklung.", url='https://twitch.tv/th__gamer'))
    
    print('Ready')



#Custom Prefix | SETZT ALLE PREFIXES ZURÜCK!!!!!

    for guild in client.guilds:

        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(guild.id)] = "o!"
        with open("prefixes.json","w") as f:
            json.dump(prefixes, f)
        print(f'Added the prefix`o!` to {guild.name}!')


        member.id = 400658261512159232
        await member.send('Dies ist ein Test')




# PREFIXES

@client.event
async def on_guild_join(guild):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "o!"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)


@client.command(aliases=['setprefix'])
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)

    await ctx.send(f"Der neue Prefix lautet: {prefix}")
    print('Neuer Prefix für', ctx.guild.id, prefix)


#Reset Prefix

@client.command(aliases=['resetprefix'])
@commands.has_permissions(administrator=True)
async def reset(ctx):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = "o!"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)

    await ctx.send('Prefix wurde zu o! zurückgesetzt!')
    print('Prefix für', ctx.guild.id, 'wurde auf o!zurückgesetzt.')

@client.event
async def on_message(msg):

    try:
        if msg.mentions[0] == client.user:

            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

            pre = prefixes[str(msg.guild.id)]

            await msg.channel.send(f"Mein Prefix für diesen Server lautet: {pre}")
    except:
        pass

    await client.process_commands(msg)
 

async def check_if_it_is_me(ctx):

    if ctx.message.author.id == 400658261512159232:

        await ctx.send('Du hast die Berechtigung um diesen Command zu benutzen', delete_after=2)
        return ctx.message.author.id == 400658261512159232
    else:
        await ctx.send('Du hast keine Berechtigung um diesen Command zu benutzen', delete_after=35)


@client.command()
@commands.check(check_if_it_is_me)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
  
    await ctx.send(f'{extension} wurde aktiviert')

@client.command()
@commands.check(check_if_it_is_me)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} wurde deaktiviert')

@client.command()
@commands.check(check_if_it_is_me)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} wurde neu aktiviert')
    print(f'{extension} wurde neu aktiviert.')


'''
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command wurde nicht gefunden')
    else:
        await ctx.send('Fehler. Die Fehlernachrichten sind noch unter Entwicklung, mehr dazu bald.')'''
 

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.ExtensionAlreadyLoaded):
        await ctx.send('Dieser Cog ist schon aktiv')
    else:
        await ctx.send('Dieser Cog ist schon aktiv.')





for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



client.run(os.getenv('TOKEN'))
