import discord
from config import *
from discord.ext import commands

intents = discord.Intents.all();                                       
bot = commands.Bot(command_prefix=prefix, intents=intents, help_command=None);

@bot.event  
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Your Applications"));
    print(f"{bot.user} has logged in");

@bot.command()
async def apps(ctx):
    StaffEmbed = discord.Embed(description=f"[<@&{StaffRole}>]({StaffLink})", color=color);
    EmsEmbed = discord.Embed(description=f"[<@&{EmsRole}>]({EmsLink})", color=color);
    PoliceEmbed = discord.Embed(description=f"[<@&{PoliceRole}>]({PoliceLink})", color=color);
    embeds = [StaffEmbed, EmsEmbed, PoliceEmbed]
    for i in embeds:
        await ctx.send(embed=i);

bot.run(token)