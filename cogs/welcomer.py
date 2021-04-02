import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from io import BytesIO
import asyncio
from math import ceil
import requests
import datetime

path = 'background.png'

class welcomer(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('welcomer.py loaded')

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

        welcome_channel = self.client.get_channel(id=787039810133032991)


        if welcome_channel != None:
            await welcome_channel.send(file= discord.File('welcomeimage.png'), embed=embed)

        else:
            print('Textkanal konnte nicht gefunden werden.')


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

        welcome_channel = self.client.get_channel(id=787039810133032991)


        if welcome_channel != None:
            await welcome_channel.send(file= discord.File('leaveimage.png'), embed=embed2)

        else:
            print('Textkanal konnte nicht gefunden werden.')

def setup(client):
    client.add_cog(welcomer(client))
