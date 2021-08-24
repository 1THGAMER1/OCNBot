import discord
from discord.ext import commands

class TeamOcean(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ocean.py loaded')

    @commands.command()
    async def überuns(self, ctx):
        masked_link_embed2 = discord.Embed(
            title= '',
            description= '**__Über uns:__**\n \n Wir sind ein Clan, der am 9.7.2020 gegründet wurde und sich nach großen Zielen sehnt. \n Der Clan ist seit Juli 2021 geschlossen und der Server ist nun ein Community Server für coole Leute 🥸. \n \n[Valorant Discord](https://discord.gg/Sw2uq8eBpB)\n \n**__Social Media:__** \n \n [Discord](https://discord.gg/AdaQBN7) \n [Instagram](https://www.instagram.com/_team_ocean_/?igshid=1gthnsd4q9vj) \n [Twitter](https://twitter.com/TeamOeanFN?s=09) \n [Twitch](https://www.twitch.tv/TeamOceande) \n \n **__Kontakt:__** \n \n  <@630018403570155521> \n <@400658261512159232> \n oceanclanesports@gmail.com \n \n  _Mit Freundlichen Grüßen_ \n **Team Ocean Management**',
            colour = discord.Colour.blue()
        )

        masked_link_embed2.set_thumbnail(url='https://cdn.discordapp.com/attachments/778307192465260588/808721848283693146/IMG_20210208_185352_432.jpg')
        masked_link_embed2.set_footer(text='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
        masked_link_embed2.set_author(name= 'Über Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed =masked_link_embed2)

    @commands.command()
    async def roster(self, ctx):
        masked_link_embed = discord.Embed(
        title= '⬜⬜⬜⬜⬜⬜⬜ Management ⬜⬜⬜⬜⬜⬜⬜',
        description= '<@&728856232953118760> (1/1) \n <@630018403570155521>\n \n <@&734153281189838967> (1/1) \n <@400658261512159232> \n \n <@&727621609359278080> (2/2) \n <@643908772275945482> \n <@411886123950800896> \n \n <@&731226637852737556> (3/3) \n <@679332454041124894> \n <@690492859391934496> \n <@640333310010064896> \n \n <@&730859863273635940> (2/4) \n <@644895688160837642> \n <@643908772275945482> \n \n <@&731061690166149161> (1/1) \n <@563055890379309077> \n \n <@&783025556521615423> (0/1) \n \n <@&730881791732219956> (2/3) \n <@640333310010064896> \n <@690492859391934496>',
        colour = discord.Colour.blue()
    )

        masked_link_embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/778307192465260588/808721848283693146/IMG_20210208_185352_432.jpg')
        masked_link_embed.set_footer(text='Team Ocean Roster',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
        masked_link_embed.set_author(name='Team Ocean Roster')
    
        await ctx.channel.purge(limit=1)
        await ctx.send(embed =masked_link_embed)

    @commands.command()
    async def regeln(self, ctx):
        masked_link_regeln = discord.Embed(
        title= 'Regeln',
        description= '🚫 Beleidigungen in jeder Form sind untersagt. \n \n 🚫 Werbung für andere Clans etc. ist verboten. \n \n 🚫Werbung ist nur in <#727847665236443246> erlaubt. \n \n 🚫 Handel von z.B. Accounts, Guthabenkarten etc. und Betteln von V-Bucks, Skins etc. ist auf diesem Server untersagt. \n \n 🚫 Themen die jugendgefährdend sind, sind aufgrund des hohen Anteils an Minderjährigen auf diesem Server verboten. \n \n 🚫 Werbung für andere Discord Sevrer ist untersagt. \n \n Ausserdem gelten natürlich die Discord Community Richtlinien: \n  https://discord.com/guidelines',
        colour = discord.Colour.blue()
    )

        masked_link_regeln.set_thumbnail(url='https://cdn.discordapp.com/attachments/778307192465260588/808721848283693146/IMG_20210208_185352_432.jpg')
        masked_link_regeln.set_footer(text='Team Ocean Regeln',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed = masked_link_regeln)

    @commands.command()
    async def anforderungen(self, ctx):
        bewerbung = discord.Embed(
        title='',
        description='__Um unserem Clan beizutreten musst du folgende Grundvoraussetzungen erfüllen:__ \n ▫ Bereit sein **den Epic- Namen** zu ändern. \n ▫ Bereit sein den Servernickname zu ändern (zum Beispiel Ocean THGAMER).  \n ▫ Höfliches und nicht toxisches Verhalten. \n \n **__Anforderungen__** \n <@&782577432272175104> \n ▫ 3 Seasons Arena Champ \n ▫ 3 mal Top 300 in Cups \n ▫ 1 mal Top 150 in Cups \n ▫ 1000 Pr Points \n \n<@&763399186149802045> \n ▫ 3 Seasons Arena Champ \n ▫ 5 Mal Top 800 in Cups \n ▫ 400 PR Points \n \n <@&730918775657857056> \n ▫ 3 Seasons Arena Champ \n ▫ 3 Mal Top 1300 in Cups \n ▫ 170 PR Points  \n \n <@&730764354835841044> \n ▫ 1 Season Arena Champ \n ▫ 3 mal Top 2500 in Cups \n ▫ 100 PR Points \n \n <@&730917730848342077> \n ▫ 5000 Arena Punkte \n ▫ 3 Mal Top 4000 in Cups \n ▫ 50 PR Points \n \n <@&730762306581168159> \n ▫ Das ist unser Grinder Team! Jeder darf beitreten!',
        colour = discord.Colour.blue()
    )

        bewerbung.set_thumbnail(url='https://cdn.discordapp.com/attachments/778307192465260588/808721848283693146/IMG_20210208_185352_432.jpg')
        bewerbung.set_author(name='Team Ocean Beitritt',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed = bewerbung)

    @commands.command()
    async def anforderungen2(self, ctx):
        bewerbung2 = discord.Embed(
            title='',
            description='Um dich für eins unserer Teams zu bewerben musst du in \n <#828923653381947392> %apply Clan schreiben. \n \n Dann wird sich ein Bot bei dir per DM melden und dir ein paar Fragen stellen. \n \n Außerdem werden PR Points, welche auf Mobile und/oder Switch verdient wurden nur halb so viel gezählt wie auf anderen Plattformen.',
            colour = discord.Colour.blue()
    )

        bewerbung2.set_author(name='So bewirbst du dich',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
        bewerbung2.set_footer(text='Team Ocean Player Bewerbung',
        icon_url='')
    
        await ctx.channel.purge(limit=1)
        await ctx.send(embed = bewerbung2)


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def partner(self, ctx, member: discord.Member, *, reason=None):
        guild= ctx.guild
        partnerRole = discord.utils.get(guild.roles, name='Partner')

        PartnerEmbed = discord.Embed(
            title='Neuer Partner',
            description=(f'{member.mention} ist jetzt neuer Partner in {guild.name}'),
            colour= discord.Colour.blue()
    )

        PartnerEmbed.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
    

        partner1a = discord.Embed(
            title='',
            description=(f'Du bist jetzt Partner in {guild.name} ✅'),
            colour= discord.Colour.blue()
    )
        partner1a.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')

        await member.add_roles(partnerRole, reason=reason)

        await ctx.channel.purge(limit=1)
        await ctx.send(embed = PartnerEmbed)
        await member.send(embed = partner1a)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def howpartner(self, ctx):
        howpartner = discord.Embed(
            title='Du willst auch Partner werden?',
            description='Schreibe <@400658261512159232> an!\n\nBeachtet, dass wenn eine ungültige Einladung geschickt wird der Partnertext gelöscht wird!',
            colour= discord.Colour.blue()
    )

        howpartner.set_footer(text='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed = howpartner)


        #ELITE
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def elite(self, ctx, member: discord.Member, *, reason=None):
        guild= ctx.guild
        eliteRole = discord.utils.get(guild.roles, name='Elite ☠️')
        clanRole = discord.utils.get(guild.roles, name='GRINDER')
    
        eliteEmbed = discord.Embed(
            title='Neuer Elite Member',
            description=(f'{member.mention} ist jetzt im {eliteRole.mention}'),
            colour= discord.Colour.blue()
    )

        eliteEmbed.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
    

        elite1a = discord.Embed(
            title='',
            description=(f'Du bist im Elite Team bei {guild.name} ✅'),
            colour= discord.Colour.blue()
    )
        elite1a.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')

        await member.add_roles(eliteRole, reason=reason)
        await member.add_roles(clanRole, reason=reason)

        await ctx.channel.purge(limit=1)
        await ctx.send(embed = eliteEmbed)
        await member.send(embed = elite1a)


#PRO TEAM

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def proteam(self, ctx, member: discord.Member, *, reason=None):
        guild= ctx.guild
        proteamRole = discord.utils.get(guild.roles, name='Pro Team')
        clanRole = discord.utils.get(guild.roles, name='GRINDER')

        proteamEmbed = discord.Embed(
            title='Neuer Pro Team Member',
            description=(f'{member.mention} ist jetzt im {proteamRole.mention}'),
            colour= discord.Colour.blue()
    )

        proteamEmbed.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
    

        proteam1a = discord.Embed(
            title='',
            description=(f'Du bist im Pro Team bei {guild.name} ✅'),
            colour= discord.Colour.blue()
    )
        proteam1a.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')

        await member.add_roles(proteamRole, reason=reason)
        await member.add_roles(clanRole, reason=reason)
    
        await ctx.channel.purge(limit=1)
        await ctx.send(embed = proteamEmbed)
        await member.send(embed = proteam1a)


    #ACADEMY
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def academy(self, ctx, *, member: discord.Member, reason=None):
        guild= ctx.guild
        academyRole = discord.utils.get(guild.roles, name='Academy')
        clanRole = discord.utils.get(guild.roles, name='GRINDER')
    

        academyEmbed = discord.Embed(
            title='Neuer Academy Member',
            description=(f'{member.mention} ist jetzt im {academyRole.mention} Team'),
            colour= discord.Colour.blue()
    )

        academyEmbed.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
    

        academy1a = discord.Embed(
            title='',
            description=(f'Du bist jetzt im Adademy Team bei {guild.name} ✅'),
            colour= discord.Colour.blue()
    )
        academy1a.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')

        await member.add_roles(academyRole, reason=reason)
        await member.add_roles(clanRole, reason=reason)
        
        await ctx.channel.purge(limit=1)
        await ctx.send(embed = academyEmbed)
        await member.send(embed = academy1a)


        #TALENTS
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def talents(self, ctx, member: discord.Member, *, reason=None):
        guild= ctx.guild
        talentsRole = discord.utils.get(guild.roles, name='Talents')
        clanRole = discord.utils.get(guild.roles, name='GRINDER')
    

        talentsEmbed = discord.Embed(
            title='Neuer Talents Member',
            description=(f'{member.mention} ist jetzt im {talentsRole.mention} Team'),
            colour= discord.Colour.blue()
    )

        talentsEmbed.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
    

        talents1a = discord.Embed(
            title='',
            description=(f'Du bist jetzt im Talents Team bei {guild.name} ✅'),
            colour= discord.Colour.blue()
    )
        talents1a.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')

        await member.add_roles(talentsRole, reason=reason)
        await member.add_roles(clanRole, reason=reason)

        await ctx.channel.purge(limit=1)
        await ctx.send(embed = talentsEmbed)
        await member.send(embed = talents1a)

        #COMMUNITY CLAN
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def grinder(self, ctx, member: discord.Member, *, reason=None):
        guild= ctx.guild
        communityRole = discord.utils.get(guild.roles, name='GRINDER')

        communityEmbed = discord.Embed(
            title='Neuer Community Clan Member',
            description=(f'{member.mention} ist jetzt im {communityRole.mention} Team'),
            colour= discord.Colour.blue()
    )

        communityEmbed.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
    

        community1a = discord.Embed(
            title='',
            description=(f'Du bist jetzt im Grinder Team bei {guild.name} ✅'),
            colour= discord.Colour.blue()
    )
        community1a.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')

        await member.add_roles(communityRole, reason=reason)
    
        await ctx.channel.purge(limit=1)
        await ctx.send(embed = communityEmbed)
        await member.send(embed = community1a)



    @commands.command()
    async def backup(self, ctx):
    
        await ctx.channel.purge(limit=1)
        await ctx.send('Das ist die Servervorlage zu Team Ocean(29.03.2021) https://discord.new/tmej5ARgXnbN')

def setup(client):
    client.add_cog(TeamOcean(client))
