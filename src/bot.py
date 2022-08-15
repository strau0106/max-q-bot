import discord
from discord import app_commands
from discord.ext import commands
import json
import requests

MY_GUILD = discord.Object(id=804661686996566066)  

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)

closure_response = requests.get('https://api.bunnyslippers.dev/closures/')
closure_json = closure_response.json()
tfr_response = requests.get('https://api.bunnyslippers.dev/tfrs/')
tfr_json = tfr_response.json()

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.tree.command()
async def closures(interaction: discord.Interaction):
    embed=discord.Embed(title="Current Starbase Closures")
    
    for i in range(len(closure_json)):
        embed.add_field(name=f"{closure_json[i]['date']}", value=f"{closure_json[i]['time']}", inline=True)
        
    await interaction.response.send_message(embed=embed)

@client.tree.command()
async def tfr(interaction: discord.Interaction):
    tfr_embed=discord.Embed(title="Current Starbase TFR's")
    
    for i in range(len(tfr_json)):
        tfr_embed.add_field(name=f"{tfr_json[i]['startDate']}", value=f"{tfr_json[i]['altitude']}", inline=True)

    await interaction.response.send_message(embed=tfr_embed)

@client.tree.command()
async def cams(interaction: discord.Interaction):
    cams_embed=discord.Embed(title="All available LabPadre cameras.", description="example ;cam <name of camera>")

    cams_embed.add_field(name="1", value="rover-2", inline=True)
    cams_embed.add_field(name="2", value="lab", inline=True)
    cams_embed.add_field(name="3", value="nerdle", inline=True)
    cams_embed.add_field(name="4", value="plex", inline=True)
    cams_embed.add_field(name="5", value="sentinel", inline=True)
    cams_embed.add_field(name="6", value="r-roost", inline=True)
    cams_embed.add_field(name="7", value="sapphire", inline=True)

    await interaction.response.send_message(embed=cams_embed)

@client.tree.command()
async def starship(interaction: discord.Interaction):
    stats=discord.Embed(title="starship stats")

    stats.add_field(name="HEIGHT", value="50 m / 164 ft", inline=True)
    stats.add_field(name="DIAMETER", value="9 m / 30 ft", inline=True)
    stats.add_field(name="PROPELLANT CAPACITY", value="1200 t / 2.6 Mlb", inline=True)
    stats.add_field(name="THRUST", value="1500 tf / 3.2Mlbf", inline=True)
    stats.add_field(name="PAYLOAD CAPACITY", value="100-150 t orbit dependent", inline=True)

    await interaction.response.send_message(embed=stats)

@client.tree.command()
async def superheavy(interaction: discord.Interaction):
    shstats=discord.Embed(title="superheavy stats")

    shstats.add_field(name="HEIGHT", value="69 m / 230 ft", inline=True)
    shstats.add_field(name="DIAMETER", value="9 m / 30 ft", inline=True)
    shstats.add_field(name="PROPELLANT CAPACITY", value="3400 t / 6.8 Mlb", inline=True)
    shstats.add_field(name="THRUST", value="7590 tf / 17 Mlbf", inline=True)

    await interaction.response.send_message(embed=shstats)

@client.tree.command()
async def cam(interaction: discord.Interaction, cam):
    f = open('cams.json')

    data = json.load(f)
    
    await interaction.response.send_message(data[f"{cam}"])

@client.tree.command()
async def podcast(interaction: discord.Interaction):
    pdc = discord.Embed(title="Podcast Links")

    pdc.add_field(name='Spotify', value="https://open.spotify.com/show/6cpEJeskI1oJMO10WKsfIw", inline=True)
    pdc.add_field(name='Amazon Podcasts', value="https://music.amazon.com/podcasts/3864e73e-b105-439e-a738-bf228f3a913d/max-q", inline=True)
    pdc.add_field(name='Anchor', value="https://anchor.fm/maxqpodcast/episodes/", inline=True)
    pdc.add_field(name='Google Podcasts', value="https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy81MjhlYjdlNC9wb2RjYXN0L3Jzcw", inline=True)
    pdc.add_field(name='Apple Podcasts', value="https://podcasts.apple.com/us/podcast/max-q/id1624318242", inline=True)

    await interaction.response.send_message(embed=pdc)

@client.tree.command()
async def latest_episode(interaction: discord.Interaction):
    file = open('info.json')
    jsn = json.load(file)

    await interaction.response.send_message(jsn["latest-episode"])

    file.close()

client.run('')
