# Imports
import os
import sys

# Even if some imports are unused, I'll leave those here just for convenience. There should be no issues memory wise.
# Testing dev branch with a pointless comment.
import discord
import logging
import json
from datetime import datetime
from discord import File, Embed, Color, User, Status
from discord.ext import commands
from discord.ext.commands import errors
from discord.ext.commands.context import Context
from dotenv import load_dotenv
from os import getenv

# Setting up logger
logging.basicConfig(filename=f'logs/jonathan_bot_{datetime.now()}.log', level=logging.INFO)
log = logging.getLogger("jonathan_bot")
log.info(f"Jonathan bot script started at [{datetime.now()}]\n\n")

# Loading environment variables
load_dotenv(".env")

# Pre-written bot config
bot_intents = discord.Intents.all()
bot_cmdPrefix = "j:"
bot_desc = """Jonathan Bolbynsky bot for random stuff
Made by Arinone"""

class BotUser(commands.Bot):
    async def setup_hook(self):
        with open("jsonfiles/cogs.json", "r") as f:
            cogs: list[str] = json.load(f)
            for cog in cogs:
                await self.load_extension(cog)

bot = BotUser(command_prefix=bot_cmdPrefix, intents=bot_intents, description=bot_desc)

# Global error handler so the console won't get spammed with errors here-and-there.
@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    emb = Embed(color=Color.from_rgb(15, 0, 0),
                title="Error occured !", description=f"""An error occured while typing the command `{ctx.command.name}` !
                If needed, you can always type `j:help {ctx.command.name}` to know how to properly use it.
                Or alternatively, you can always use slash commands as they're less likely to give you errors next time !""")
    emb.set_footer(text=f"Technical details : `{error}`")
    await ctx.send(embed=emb, delete_after=15)
    log.error(f"Error from command [{ctx.command.name}] by user [{ctx.author.id}] : \n\t[{error}]")

bot.run(getenv("BOT_TOKEN"))