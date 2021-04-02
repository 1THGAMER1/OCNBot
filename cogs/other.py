import  discord
from discord.ext import commands

class others(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('other.py loaded')

    #EINLADUNG
    @commands.command()
    async def invite(self, ctx):
        invite = discord.Embed(
            title='Lade mich in dein Server ein!',
            description='[Einladungslink](https://discord.com/oauth2/authorize?client_id=711568834590408765&scope=bot&permissions=8)',
            colour = discord.Colour.blue()
    )

        invite.set_footer(text='Ocean Bot',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed = invite)


def setup(client):
    client.add_cog(others(client))