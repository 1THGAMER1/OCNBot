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
            description='[Einladungslink](https://discord.com/oauth2/authorize?client_id=711568834590408765&permissions=0&redirect_uri=https%3A%2F%2Fdiscord.com%2Foauth2%2Fauthorize%3Fclient_id%3D711568834590408765%26scope%3Dbot%26permissions%3D8.&scope=bot%20applications.commands)',
            colour = discord.Colour.blue()
    )

        invite.set_footer(text='Ocean Bot',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed = invite)
        
    @commands.command()
    async def version(self, ctx):
        version = discord.Embed(
            title='Version 1.1.0',
            description='Der Bot befindet sich in Version **1.1.0**\n \n**__NEU:__**\n-Neuer überarbeiteter Welcomer, nun kann jeder ganz einfach den Welcomer in seinen Server benutzen.\n-Submit Command in der Beta Version eingeführt. (Schreibe mich für neue Vorschläge oder Feedback an.\n-Oberflächenupdates der Antworten.\n-Weitere kleine Fehlerbehebungen\n Amogus',
            colour = discord.Colour.blue()
            
    ) 
            
        version.set_footer(text='Ocean Bot Version 1.1.0',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')

            
        await ctx.channel.purge(limit=1)
        await ctx.send(embed = version)
        
        
    @commands.command()
    async def nextversion(self,ctx):
        nxversion = discord.Embed(
            title = 'Nächste Version 1.2.0',
            description = '**Neue Features in der neuen Version**:\n-Benutzung von Buttons\n-Weitere erneuerungen der UI ```unter anderem ein neuer Help Command\nRollenvergabe Command```\n-Weitere neue Commands. Du kannst sie mit dem Submit Command vorschlagen!',
            colour = discord.Colour.blue()
            
    )
        nxversion.set_footer(text='Version 1.2.0 wird wahrscheinlich im Frühjahr 2022 erscheinen.',
        icon_url='https://cdn.discordapp.com/emojis/824668236200804383.png?v=1')
        
        await ctx.channel.purge(limit=1)
        await ctx.send(embed = nxversion)


def setup(client):
    client.add_cog(others(client))
