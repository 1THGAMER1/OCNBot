import discord 
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import requests
import datetime
import asyncio

path="media/valback.png"

class valorant(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Valorant.py loaded")

    @commands.command(help="In bearbeitung")
    async def valstats(self, message, *, question):
        channel = message.channel


        async with channel.typing():


            embed = discord.Embed(
                title='Bitte gib ausserdem deinen Tag ein',
            )
            sent = await message.send(embed= embed)
            try:
                msg = await self.client.wait_for(
                    "message",
                    timeout=90,
                    check = lambda message : message.author == message.author
                                            and message.channel == message.channel
                )
                id = msg.content

                antwort = requests.get(f'https://api.henrikdev.xyz/valorant/v1/account/{question}/{id}')
                antwort2 = requests.get(f'https://api.henrikdev.xyz/valorant/v1/mmr/eu/{question}/{id}')


                hey = antwort.json()
                hey2 = (hey['status'])

                rank=antwort2.json()

                if hey2 == 404:
                    await message.send("Dein Name wurde nicht gefunden. Überprüfe deine Eingabe.")
                elif hey2 == 424:
                    await message.send("Die Anfragerate wurde überschritten. Bitte warte 2 Minuten!")
                elif hey2 == 429:
                    await message.send("You reached your account endpoint rate Limit, please try again later")
                elif hey2 == 200:
                    pass
                else:
                    await message.send("Name nicht gefunden")


                #level = (hey['data']['account_level'])
                banner =(hey['data']['card']['wide'])

                rank2=(rank['data']['currenttierpatched'])
                rankbild = (rank['data']['images']['large'])
                

                #await message.send(bild)

                with requests.get(banner) as r:
                    img_data = r.content
                with open("large.jpg", "wb") as handler:
                    handler.write(img_data)

                with requests.get(rankbild) as r:
                    img_data = r.content
                with open("rbild.png", "wb") as handler:
                    handler.write(img_data)
                
                im1 = Image.open("media/valback.png")
                im2 = Image.open("large.jpg")
                rb = Image.open("rbild.png")

                im3 = im2.resize((861, 245))
                im3.save("larger.png")
                position = ((639, 0))

                rb2 = rb.resize((183, 183))
                rb2.save("rb2.png")
                position2 = ((380, 0))

                draw = ImageDraw.Draw(im1)
                font = ImageFont.truetype("fonts/BebasNeue-Regular.ttf", 50)
                font2 = ImageFont.truetype("fonts/BebasNeue-Regular.ttf", 60)

                draw.text((22,81), f"{question}",(255,255,255), font = font2)
                draw.text((391, 195), f"{rank2}", (255,255,255), font = font)

                back_im = im1.copy()
                back_im.paste(im3, position)
                back_im.paste(rb2, position2, rb2)

                back_im.save("banner.png", quality=100)


                await message.send(file = discord.File("banner.png"))


                

            except asyncio.TimeoutError:

                zeitabgelaufen = discord.Embed(
                        title='Zeit abgelaufen!',
                        description='Der Command wird abgebrochen, da für 90 Sekunden keine Antwort geschrieben worden ist. ❌',
                        colour=discord.Colour.red()
                    )

                zeitabgelaufen.set_footer(text='Bitte führe den Command neu aus.')

                await message.send(embed = zeitabgelaufen)




def setup(client):
    client.add_cog(valorant(client))