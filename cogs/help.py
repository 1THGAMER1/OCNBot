import discord
from discord import colour
from discord.ext import commands
import asyncio
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import json


intents = discord.Intents(messages = True, guilds = True, members = True)

class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('help.py loaded')
    
    @cog_ext.cog_slash(
        name="welcomerchannel",
        description="Wo ist der Welcomer eingerichtet?"
    )
    async def _welcomerchannel(ctx, member):
        with open("data/welcomer.json","r") as f:
            channel = json.load(f)
            channelid = channel[str(member.guild.id)]

        await ctx.send("Test")

    @commands.command()
    async def we(self, ctx):
        with open("data/welcomer.json", "r") as f:
            kanal = json.load(f)
            kanal2 = kanal[str(ctx.guild.id)]

        await ctx.send(f"Der Welcomer ist derzeit in <#{kanal2}> aktiv.")


    @cog_ext.cog_slash(
        name="idhelp",
        description="wie finde ich meine ID heraus?"
    )
    async def _channelid(self,ctx):
        channelid = discord.Embed(
            title='Channelid Hilfe',
            description='Dieses Video zeigt dir wie du eine ChannelID herausfindest und kopierst. [YouTube Link](https://youtu.be/6dqYctHmazc)',
            colour=discord.Colour.blue()
        )

        await ctx.send(embed = channelid)

    @cog_ext.cog_slash(
        name="submit",
        description="Schicke mir eine Nachricht"
    )
    async def _submit(self, ctx):
        await ctx.send("Placeholder")

    @commands.command()
    async def submit(self, ctx):

        submit2 = discord.Embed(
            title='Neue Nachricht',
            description='Bitte schreibe deine Nachricht in diesem Kanal:',
            colour=discord.Color.blue()
        )

        submit2.set_footer(text='Bitte beachte, dass Bilder oder sonstige Anhänge nicht verschickt werden.')

        await ctx.send(embed = submit2)
        try:
            msg = await self.client.wait_for(
                "message",
                timeout=60,
                check= lambda message: message.author == ctx.author
                                    and message.channel == ctx.channel
            )
            
            lol = msg.content

            if msg:
                await msg.delete()


                thgamer = discord.utils.get(ctx.guild.members, id=400658261512159232)
                print(thgamer)
                print(ctx.author)

                await thgamer.send(f'_Eine neue Nachricht von {ctx.author} aus dem Server {ctx.guild}:_ \n {lol}')

                verschickt = discord.Embed(
                    title='',
                    description='Deine Nachricht wurde erfolgreich verschickt ✅',
                    colour=discord.Colour.green()
                )

                await ctx.send(embed = verschickt)
        
        except asyncio.TimeoutError:
            zeitabgelaufen = discord.Embed(
                        title='Zeit abgelaufen!',
                        description='Der Command wird abgebrochen, da für 1 Minute keine Antwort geschrieben worden ist. ❌',
                        colour=discord.Colour.red()
                    )

            zeitabgelaufen.set_footer(text='Bitte führe den Command neu aus.')

            await submit2.delete()
            await ctx.send(embed = zeitabgelaufen)
            
def setup(client):
    client.add_cog(help(client))
