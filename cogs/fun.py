import discord
from discord.ext import commands
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from io import BytesIO
import asyncio

def check_if_it_is_me(ctx):
    return ctx.message.author.id == 400658261512159232

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun.py loaded')



    @commands.command(aliases=['8ball'])
    async def _8ball(self, message, question):


        channel = message.channel
        async with channel.typing():
        responses = ['It is certain.',
                'It is decidely so.',
                'Without a doub.',
                'Yes, definitely',
                'You may rely on it.',
                'As I see it, yes',
                'Most likely',
                'Outlook good.',
                'Yes.',
                'Signs point to yes',
                'Reply hazy, try again.',
                'Ask again later',
                'Better not tell you now',
                'Cannot predict now.',
                'Concentrate and ask again',
                "Don't count on it",
                'My reply is no',
                'My sources say no',
                'Outlook not so good',
                'Very doubtful']

        await channel.purge(limit=1)
        await channel.send(f'Frage: {question} \n Antwort {random.choice(responses)}')



#Schreibanzeige
    @commands.command()
    @commands.check(check_if_it_is_me)
    async def lol(self, message):
        channel = message.channel

        async with channel.typing():
  
            await channel.send('Beta')


#WANTED
    @commands.command()
    async def wanted(self, message, user: discord.Member = None):

        channel = message.channel
    
        async with channel.typing():

            if user == None:
                #user = message.author
                await channel.send('Die richtige Schreibweise lautet: ```o!wanted @USER```')
            else:
    
                wanted = Image.open('wanted.png')

                asset = user.avatar_url_as(size = 128)
                data = BytesIO(await asset.read())
                pfp = Image.open(data)

                pfp = pfp.resize((755, 754))
                wanted.paste(pfp, (233, 471))
                wanted.save('profile.png')
    
                await channel.purge(limit=1)
                await channel.send(file = discord.File('profile.png'))



    @commands.command()
    async def ping(self, message):

        channel = message.channel

        await channel.purge(limit=1)
        await channel.send(f'Pong! Meine Latenz beträgt: ``{round(self.client.latency * 1000)}ms``')



def setup(client):
    client.add_cog(fun(client))
