import discord
from discord.ext import commands
import requests
import json

bot = commands.Bot(command_prefix=';')

closure_response = requests.get('https://api.bunnyslippers.dev/closures/')
closure_json = closure_response.json()
tfr_response = requests.get('https://api.bunnyslippers.dev/tfrs/')
tfr_json = tfr_response.json()

@bot.command()
async def closures(ctx):
    embed=discord.Embed(title="Current Starbase Closures")
    
    for i in range(len(closure_json)):
        embed.add_field(name=f"{closure_json[i]['date']}", value=f"{closure_json[i]['time']}", inline=True)

    await ctx.send(embed=embed)

@bot.command()
async def tfr(ctx):
    tfr_embed=discord.Embed(title="Current Starbase TFR's")
    
    for i in range(len(tfr_json)):
        tfr_embed.add_field(name=f"{tfr_json[i]['startDate']}", value=f"{tfr_json[i]['altitude']}", inline=True)

    await ctx.send(embed=tfr_embed)

@bot.command()
async def cams(ctx):
    cams_embed=discord.Embed(title="All available LabPadre cameras.", description="example ;cam <name of camera>")
    
    cams_embed.add_field(name="1", value="rover-2", inline=True)
    cams_embed.add_field(name="2", value="lab", inline=True)
    cams_embed.add_field(name="3", value="nerdle", inline=True)
    cams_embed.add_field(name="4", value="plex", inline=True)
    cams_embed.add_field(name="5", value="sentinel", inline=True)
    cams_embed.add_field(name="6", value="r-roost", inline=True)
    cams_embed.add_field(name="7", value="sapphire", inline=True)

    await ctx.send(embed=cams_embed)

@bot.command()
async def cam(ctx, cam):
    f = open('cams.json')

    data = json.load(f)
    
    await ctx.send(data[f"{cam}"])

bot.run('OTUzMzY1NjIzOTUyNTA2OTQw.YjDg7Q.SYVE5XftUt3tXrnaXRBHTtkq_Do')