from discord import colour
from discord.ext.commands.bot import AutoShardedBot
import discord
from discord import member
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from io import BytesIO
import asyncio
from math import ceil
import requests
import datetime
import json
import requests


path = 'background.png'
prefixespath = 'prefixes.json'

class welcomer(commands.Cog):

    def __init__(self, client):
        self.client = client

    def hey(message):
            with open("welcomer.json", "r") as f:
                channelid2 = json.load(f)

            id2 = channelid2[str(message.guild.id)]

    @commands.Cog.listener()
    async def on_ready(self):
        print('welcomer.py loaded')


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def welcomer(self, ctx):

        try:
            with open(prefixespath, "r") as f:
                prefixes = json.load(f)

            pre = prefixes[str(ctx.guild.id)]

            await ctx.send('')
        except:
            pass


        await ctx.message.delete()

        embed = discord.Embed(
            title='Bitte gib die ID an, in welchem Channel der Welcomer eingerichtet werden soll.',
            description=f'Falls du nicht weißt wie du die eines Channels herausfindest, schreibe {pre}channelid im Chat. \n \n Dieser Command ist noch unter Entwicklung.',
            colour= discord.Colour.blue()
        )
        embed.set_footer(text='Diese Nachricht wird nach 1 Minute gelöscht und der Command abgebrochen.')

        sent = await ctx.send(embed=embed)
        try:
            msg = await self.client.wait_for(
                "message",
                timeout=60,
                check=lambda message: message.author == ctx.author
                                    and message.channel == ctx.channel
            )
            welcomerid = msg.content
      

            test = welcomerid.isdigit()

            if msg:
                await sent.delete()
                await msg.delete()

                if (test) != True:
                    
                    ZahlenFehler = discord.Embed(
                        title='Fehler',
                        description='Eine ID besteht nur aus Zahlen ❌',
                        colour=discord.Colour.red()
                    )
                    ZahlenFehler.set_footer(text='Bitte führe den Command erneut aus.')

                    await ctx.send(embed = ZahlenFehler, delete_after=30)

                else:


                    test_channel = self.client.get_channel(int(welcomerid))
                
                    if test_channel != None:
                        with open("welcomer.json", "r") as f:
                                welcomer = json.load(f)

                                welcomer[str(ctx.guild.id)] = welcomerid

                        with open("welcomer.json", "w") as f:
                            json.dump(welcomer, f)
                            

                        
                        
                
                                         

                            eingerichtet = discord.Embed(
                                  title='Fertig!',
                                  description='Welcomer ist nun in diesem Kanal eingerichtet. ✅',
                                  colour=discord.Color.green()
                            )

                            eingerichtet2 = discord.Embed(
                                  title='Fertig!',
                                  description=f'Welcomer ist nun in <#{welcomerid}> eingerichtet. ✅',
                                  colour=discord.Colour.green()
                            )

                            await test_channel.send(embed = eingerichtet)
                            print('Welcomer für', ctx.guild.id, 'nun in', welcomerid)
                            await ctx.send(embed = eingerichtet2)
                            
                    else:

                        notfound = discord.Embed(
                            title='Fehler!',
                            description='Der Textkanal konnte nicht gefunden werden. ❌',
                            colour=discord.Colour.red()
                        )
                        notfound.set_footer(text='Bitte beachte, dass der Bot genung Berechtigungen haben muss.')

                        await ctx.send(embed= notfound, delete_after=30)
                        print(test_channel)




        except asyncio.TimeoutError:

            zeitabgelaufen = discord.Embed(
                        title='Zeit abgelaufen!',
                        description='Der Command wird abgebrochen, da für 1 Minute keine Antwort geschrieben worden ist. ❌',
                        colour=discord.Colour.red()
                    )

            zeitabgelaufen.set_footer(text='Bitte führe den Command neu aus.')
            
            await sent.delete()
            await ctx.send(embed = zeitabgelaufen)




    @commands.Cog.listener()
    async def on_member_join(self, member):
        
        with requests.get(member.avatar_url) as r:
            img_data = r.content
        with open('profile.jpg', 'wb') as handler:
            handler.write(img_data)
        
        im1 = Image.open("background.png")
        im2 = Image.open("profile.jpg")

        draw = ImageDraw.Draw(im1)
        font = ImageFont.truetype("BebasNeue-Regular.ttf", 32)
    # Add the Text to the result image
        draw.text((160, 40),f"Willkommen {member.name}",(255,255,255),font=font)
        draw.text((160, 80),f"Du bist der {len(list(member.guild.members))}. Member",(255,255,255),font=font)

        size = 129

        im2 = im2.resize((size, size), resample=0)

        mask_im = Image.new("L", im2.size, 0)
        draw = ImageDraw.Draw(mask_im)
        draw.ellipse((0, 0, size, size), fill=255)

        mask_im.save('mask_circle.png', quality=95)

        back_im = im1.copy()
        back_im.paste(im2, (11, 11), mask_im)


        back_im.save('welcomeimage.png', quality=95)

        f = discord.File(path, filename="welcomeimage.png")

        embed = discord.Embed()
        embed.set_image(url="attachment://welcomeimage.png")
        embed.timestamp = datetime.datetime.utcnow()

        with open("welcomer.json", "r") as f:
            channelid2 = json.load(f)

            id2 = channelid2[str(member.guild.id)]
            

            


            welcome_channel = self.client.get_channel (int(id2))

        if welcome_channel != None:
            print(welcome_channel)
            await welcome_channel.send(file= discord.File('welcomeimage.png'))
            

        else:
            print('Textkanal konnte nicht gefunden werden.')
            print(id2)
            print(welcome_channel)
            



    @commands.Cog.listener()
    async def on_member_remove(self,member):

        with requests.get(member.avatar_url) as r:
            img_data = r.content
        with open('profile.jpg', 'wb') as handler:
            handler.write(img_data)
        im1 = Image.open("background.png")
        im2 = Image.open("profile.jpg")

        draw = ImageDraw.Draw(im1)
        font = ImageFont.truetype("BebasNeue-Regular.ttf", 32)
        font2 = ImageFont.truetype("BebasNeue-Regular.ttf", 26)
    # Add the Text to the result image
        draw.text((160, 40),f"Tschüss {member.name}",(255,255,255),font=font)
        draw.text((160, 80),f"Neue Memberzahl: {len(list(member.guild.members))}",(255,255,255),font=font)

        size = 129

        im2 = im2.resize((size, size), resample=0)

        mask_im = Image.new("L", im2.size, 0)
        draw = ImageDraw.Draw(mask_im)
        draw.ellipse((0, 0, size, size), fill=255)

        mask_im.save('mask_circle.png', quality=95)

        back_im = im1.copy()
        back_im.paste(im2, (11, 11), mask_im)


        back_im.save('leaveimage.png', quality=95)

        f = discord.File(path, filename="leaveimage.png")

        embed2 = discord.Embed()
        embed2.set_image(url="attachment://leaveimage.png")
        embed2.timestamp = datetime.datetime.utcnow()



        with open("welcomer.json", "r") as f:
            channelid2 = json.load(f)

            id3 = channelid2[str(member.guild.id)]
            wirklichechteid = id3



        welcome_channel = self.client.get_channel(int(wirklichechteid))

        

        if id3 != None:
            print('\n - \n', welcome_channel, '\n - \n')
            print('\n - \n', id3 ,'\n - \n')
            await welcome_channel.send(file= discord.File('leaveimage.png'))
            

        else:
            print('\n \n - \nTextkanal konnte nicht gefunden werden.\n \n - \n')
            print('\n - \n', id3, '\n - \n')


@commands.Cog.listener()
async def on_command_error(self, ctx, error):
    if isinstance(error, commands.ValueError):
        await ctx.send('Eine ID sollte nur aus Zahlen bestehen.')
    else:
        print('COMMAND INVOKE TEST | Bitte schreibe TH GAMER#6310 an falls du diese Nachricht siehst.')


'''
    @welcomer2.error
    async def welcomer2_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Dir fehlt die Berechtigung für diesen Command. Fehlende Berechtigung: ```Administrator```')
        else:
            await ctx.send('Unbekannter Fehler | Bitte schreibe eine DM an TH GAMER#6310')'''

def setup(client):
    client.add_cog(welcomer(client))
