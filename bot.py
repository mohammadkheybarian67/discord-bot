import discord
import os
from discord.ext import commands

TOKEN =os.getenv("MTQzNDI1NzMxMTcxNDY0Mzk2OA.GzTJsG.HFD4nKqvvpN231g6UHt9u6V_6k9Hm9X5DFkbIE")
bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
@bot.event
async def on_ready():
    print(f"{bot.user} وارد شد")

@bot.command()
async def سلام(ctx):
    await ctx.send("سلام!حالت چطوره؟")
bot.run(TOKEN)