import discord
import os
from discord.ext import commands
from keep_awake import keep_awake

import giphy_client
from giphy_client.rest import ApiException
import random

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print(f"we have logged in as {client.user}")

@client.command()
async def siesta(ctx):
  await ctx.channel.send(f"Hi! {ctx.author.mention} it's great to see you")


@client.command()
async def helpme(ctx):
  await ctx.channel.send(f'Hey {ctx.author.mention}! please type (.gif "search anything")')

@client.command()
async def gif(ctx,*,q="random"):
    api_key="4mwKht785I6YvXyTSEZVBokaJsz52A1V"
    api_instance = giphy_client.DefaultApi()
    try: 
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=10, rating='r')
        listahan = list(api_response.data)
        giphy = random.choice(listahan)
        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giphy.id}/giphy.gif')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

keep_awake()
client.run(os.environ['blessings'])
