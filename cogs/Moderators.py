import discord
from discord.ext import commands
import datetime

class moderators(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderators.py loaded.')


        #KICK

    @commands.command() 
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, * , reason=None): 

        await member.kick(reason=reason)

        kick = discord.Embed(
            title='Gekickt!',
            description=f'{member.mention} wurde gekickt. Grund : {reason}!',
            colour=discord.Colour.blue()
    
    )
        kick.set_footer(text="Team Ocean",
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
        kick.timestamp = datetime.datetime.utcnow()
        kick.set_thumbnail(url='https://cdn.discordapp.com/attachments/778307192465260588/808721848283693146/IMG_20210208_185352_432.jpg')


        kick2 = discord.Embed(
            title='Du wurdest gekickt!',
            description=f'Du wurdest aus dem Team Ocean Server gekickt. Grund : {reason}.',
            colour=discord.Colour.blue()
    )

        kick2.set_footer(text="Team Ocean",
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
        kick2.timestamp = datetime.datetime.utcnow()
        kick2.set_thumbnail(url='https://cdn.discordapp.com/attachments/778307192465260588/808721848283693146/IMG_20210208_185352_432.jpg')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed = kick)
        await member.send(embed = kick2)

        #BAN

    @commands.command() 
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, * , reason=None): 
        
        await member.ban(reason=reason)

        ban = discord.Embed(
            title='Gebannt!',
            description=f'{member.mention} wurde gebannt wegen {reason}!',
            colour=discord.Colour.blue()
    
    )
        ban.set_footer(text="Team Ocean",
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
        ban.timestamp = datetime.datetime.utcnow()
        ban.set_thumbnail(url='https://cdn.discordapp.com/attachments/778307192465260588/794243542489759774/tenor.gif')


        ban2 = discord.Embed(
            title='Du wurdest gebannt!',
            description=f'Du wurdest im Team Ocean Server gebannt wegen {reason}.',
            colour=discord.Colour.blue()
    )

        ban2.set_footer(text="Team Ocean",
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
        ban2.timestamp = datetime.datetime.utcnow()
        ban2.set_thumbnail(url='https://cdn.discordapp.com/attachments/778307192465260588/794243542489759774/tenor.gif')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed = ban)
        await member.send(embed = ban2)



#UNBAN

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        bannedUsers = await ctx.guild.bans()
        name, discriminator = member.split("#")

        for ban in bannedUsers:
            user = ban.user

            if(user.name, user.discriminator) == (name, discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{user.mention} wurde entbannt.")
                return

#Mute  

    @commands.command()
    @commands.has_permissions(manage_permissions=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)


        mutedEmbed = discord.Embed(
            title='',
            description=(f'{member.mention} wurde gemuted, {reason} ✅'),
            colour= discord.Colour.blue()
    )
        mutedEmbed.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')

        mutedEmbed2 = discord.Embed(
            title='',
            description=(f'Du wurdest im Server {guild.name} gemuted, wegen {reason} gemuted'),
            colour= discord.Colour.blue()
    )
        mutedEmbed2.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
    
    
        await member.add_roles(mutedRole, reason=reason)
    
    
        await ctx.channel.purge(limit=1)
        await ctx.send(embed = mutedEmbed)
        await member.send(embed = mutedEmbed2)

    
    #UNMUTE

    @commands.command()
    @commands.has_permissions(manage_permissions=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        unmutedEmbed = discord.Embed(
            title='',
            description=(f'{member.mention} wurde unmuted ✅'),
            colour= discord.Colour.blue()
    )
        unmutedEmbed.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')
    
        unmutedEmbed2 = discord.Embed(
            title='',
            description=(f'Du wurdest im {ctx.guild.name} Server unmuted ✅'),
            colour= discord.Colour.blue()
    )
        unmutedEmbed.set_author(name='Team Ocean',
        icon_url='https://cdn.discordapp.com/attachments/778307192465260588/809793314614149140/android-icon-96x96.png')



        await member.remove_roles(mutedRole)


        await ctx.channel.purge(limit=1)
        await ctx.send(embed = unmutedEmbed)
        await member.send(embed = unmutedEmbed2)

    
#Clear
    @commands.command(aliases = ['purge','nuke','delete'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f'{amount} Nachrichten wurden gelöscht ✅', delete_after=7)


def setup(client):
    client.add_cog(moderators(client))
