import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='!')

closure_response = requests.get('https://api.bunnyslippers.dev/closures/')
closure_json = closure_response.json()

@bot.command()
async def closures(ctx):
    embed=discord.Embed(title="Current Starbase Closures")
    
    for i in range(len(closure_json)):
        embed.add_field(name=f"{closure_json[i]['date']}", value=f"{closure_json[i]['time']}", inline=True)

    await ctx.send(embed=embed)

bot.run('OTUzMzY1NjIzOTUyNTA2OTQw.YjDg7Q.SYVE5XftUt3tXrnaXRBHTtkq_Do')