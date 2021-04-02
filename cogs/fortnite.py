import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from io import BytesIO
import asyncio
from math import ceil
import requests
import datetime


class fortnite(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fortnite.py loaded')


#STATS COMMAND

    @commands.command()
    async def stats(self, message, *, question):
        channel = message.channel

        async with channel.typing():

            response = requests.get(f'https://fortnite-api.com/v1/stats/br/v2/?name={question}')
            hey = response.json()
            hey2 = (hey['data'])
            hey3 = (hey2['account'])
            hey4 = (hey3['name'])
            hey5 = (hey2['battlePass'])
            hey6 = (hey5['level'])
            hey7 = (hey2['stats'])
            hey8 = (hey7['all'])  #All
            hey9 = (hey8['overall']) #Overall/Gesamt
            hey10 = (hey9['wins'])
            hey11 = (hey9['kills'])
            hey12 = (hey9['kd'])
            hey13 = (hey9['matches'])
            hey14 = (hey9['winRate'])
            hey15 = (hey9['minutesPlayed'])
            hey16 = (hey8['solo']) #Solo
            hey17 = (hey16['wins'])
            hey18 = (hey16['kills'])
            hey19 = (hey16['top25'])
            hey20 = (hey16['kd'])
            hey21 = (hey16['matches'])
            hey22 = (hey16['winRate'])
            hey23 = (hey8['duo']) #Duo
            hey24 = (hey23['wins'])
            hey25 = (hey23['kills'])
            hey26 = (hey23['top12'])
            hey27 = (hey23['kd'])
            hey28 = (hey23['matches'])
            hey29 = (hey23['winRate'])
            hey30 = (hey8['squad'])#Teams
            hey31 = (hey30['wins'])#
            hey32 = (hey30['top6'])#
            hey33 = (hey30['kills'])#
            hey34 = (hey30['kd'])#
            hey35 = (hey30['matches'])
            hey36 = (hey30['winRate'])

            days = hey15//1440    #5,61736111111
            days1 = days%1440
            hour = days1//0.35
            minute = days1/0.2

            zeit = days, hour, minute

    #print(f'{(int(days))} {(int(hour))} {(int(minute))}')

#Rundung 1 Gesamt
            class Data(object):
                def __init__(self,zahl):
                    self.zahl = zahl

                def __round__(self, dezimalstellenanzahl):
                    return round(self.zahl, dezimalstellenanzahl)

            zahlen = [hey12]

            for zahl in zahlen:
                d = Data(zahl)
        #print (round(d, 2))

#Rundung 2 Gesamt
                def __round__(self, dezimalstellenanzahl):
                    return round(self.zahl, dezimalstellenanzahl)

                zahlen2 = [hey14]

            for zahl in zahlen2:
                d2 = Data(zahl)
        #print (round(d2,2))

# Rundung 3 Solo
                def __round__(self, dezimalstellenanzahl):
                    return round(self.zahl, dezimalstellenanzahl)

                zahlen3 = [hey20]

            for zahl in zahlen3:
                d3 = Data(zahl)
        #print (round(d3,2))

#Rundung 4 Solo
                def __round__(self, dezimalstellenanzahl):
                    return round(self.zahl, dezimalstellenanzahl)

                zahlen4 = [hey22]

            for zahl in zahlen4:
                d4 = Data(zahl)
        #print (round(d4,2))

#Rundung 5 Duo
                def __round__(self, dezimalstellenanzahl):
                    return round(self.zahl, dezimalstellenanzahl)

                zahlen5 = [hey26]

            for zahl in zahlen5:
                d5 = Data(zahl)
        #print (round(d5,2))

#Rundung 6 Duo
                def __round__(self, dezimalstellenanzahl):
                    return round(self.zahl, dezimalstellenanzahl)

                zahlen6 = [hey29]

            for zahl in zahlen6:
                d6 = Data(zahl)
        #print (round(d6,2))

#Rundung 7 Teams

                def __round__(self, dezimalstellenanzahl):
                    return round(self.zahl, dezimalstellenanzahl)

                zahlen7 = [hey34]

            for zahl in zahlen7:
                d7 = Data(zahl)
        #print (round(d7,2))

#Rundung 8 Teams

                def __round__(self, dezimalstellenanzahl):
                    return round(self.zahl, dezimalstellenanzahl)

                zahlen8 = [hey36]

            for zahl in zahlen8:
                d8 = Data(zahl)
        #print (round(d8,2))




    # Saves the Profile Picture as a file for PIL to edit it.

            im1 = Image.open("Stats.png")

    # Font Stuff
            draw = ImageDraw.Draw(im1)
            font = ImageFont.truetype("BebasNeue-Regular.ttf", 82)
            font2 = ImageFont.truetype("BebasNeue-Regular.ttf", 64)
            font3 = ImageFont.truetype("BebasNeue-Regular.ttf", 52)
    # Add the Text to the result image
               #X  #Y
            draw.text((50, 150),f'{hey4}',(255,255,255),font=font)
            draw.text((850, 515), f"{hey6}", (255,255,255),font=font2)
            draw.text((1080, 295), f"{hey10}", (255,255,255), font=font2)
            draw.text((850, 390),f"{hey11}", (255,255,255), font=font2)  #Kills Gesamt
            draw.text((1080, 390),f"{(round(d,2))}", (255,255,255), font=font2)
            draw.text((850, 295),f"{hey13}", (255,255,255), font=font2)
            draw.text((1240, 295),f"{(round(d2,2))}%", (255,255,255), font=font2)
            draw.text((1210, 390),f"{(int(days))}   {(int(hour))}  {(int(minute))}", (255,255,255), font=font2)
            draw.text((300, 400), f"{hey17}", (255,255,255), font=font3) #Siege Solo
            draw.text((300, 510), f"{hey18}", (255,255,255), font=font3) #Kills Solo
            draw.text((70, 510), f"{hey19}", (255,255,255), font=font3) #Top 25 Solo
            draw.text((522, 510), f"{(round(d3,2))}", (255,255,255), font=font3) #kd Solo
            draw.text((70, 400), f"{hey21}", (255,255,255), font=font3)
            draw.text((525, 400), f"{(round(d4,2))}%", (255,255,255), font=font3)
            draw.text((300,750), f"{hey24}", (255,255,255), font=font3)
            draw.text((300, 865), f"{hey25}", (255,255,255), font=font3)
            draw.text((70, 870),f"{hey26}", (255,255,255), font=font3)
            draw.text((525,870), f"{(round(d5,2))}", (255,255,255), font=font3)
            draw.text((65,750), f"{hey28}", (255,255,255), font=font3)
            draw.text((530,755), f"{(round(d6,2))}%", (255,255,255), font=font3)
            draw.text((1065, 750), f"{hey31}", (255,255,255), font=font3)
            draw.text((825, 870), f"{hey32}", (255,255,255), font=font3)
            draw.text((1060, 870), f"{hey33}", (255,255,255), font=font3)
            draw.text((1280, 870), f"{(round(d7,2))}", (255,255,255), font=font3)
            draw.text((820, 755), f"{hey35}", (255,255,255), font=font3)
            draw.text((1285,755), f"{(round(d8,2))}%", (255,255,255), font=font3)


            size = 129

    # Masks the profile picture and adds it to the background.
            im1 = im1.copy()


            im1.save('stats2.png', quality=95)
    # Stuff to send the embed with a local image.


            stats = discord.Embed(
                title=f'Stats von {question}',
                colour = discord.Colour.blue()
    )
            stats.set_image(url="attachment://stats2.png")
            stats.timestamp = datetime.datetime.utcnow()

    
            await channel.purge(limit=1)
            await message.send(file= discord.File('stats2.png'), embed=stats)
    #print(hey12)











def setup(client):
    client.add_cog(fortnite(client))