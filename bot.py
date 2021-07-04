import discord
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

async def check_if_it_is_me(ctx):

    if ctx.message.author.id == 400658261512159232:

        await ctx.send('Du hast die Berechtigung um diesen Command zu benutzen.', delete_after=10)
        return ctx.message.author.id == 400658261512159232
    else:
        await ctx.send('Du hast keine Berechtigung um diesen Command zu benutzen', delete_after=30)



@client.event
async def on_ready():          
    
    DiscordComponents(client)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Bewerbungen geschlossen! ", url='https://twitch.tv/th__gamer'))
    
    print('Ready')



#Custom Prefix | SETZT ALLE PREFIXES ZURÜCK!!!!!


    #for guild in client.guilds:

        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(guild.id)] = "o!"
        with open("prefixes.json","w") as f:
            json.dump(prefixes, f)
        #print(f'Added the prefix`o!` to {guild.name}!')


#WELCOMER



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
        print('ON COMMAND ERROR TEST | Bitte schreibe TH GAMER#6310 an falls du diese Nachricht siehst.')
        '''

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.ExtensionAlreadyLoaded):
        await ctx.send('Dieser Cog ist schon aktiv')
    else:
        await ctx.send('Dieser Cog ist schon aktiv.')





for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



client.run('NzExNTY4ODM0NTkwNDA4NzY1.XsE6Hg.0UMjWqRmv_afqQNKLO-DkXy7U9U')
