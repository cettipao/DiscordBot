import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">",description = "El primer Bot de CettiPao")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")



bot.run('NzE3NzY3ODgzMTQ4NDkyOTMw.XtfJhw.Edlzp5w1dliDdsJh6OroyOELAwo')