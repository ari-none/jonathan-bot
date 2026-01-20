# Imports
import commandFunctions as cmdf
import discord
import logging
from datetime import datetime
from discord import File
from discord.ext import commands
from discord.ext.commands.context import Context
from dotenv import load_dotenv
from os import getenv

# Setting up logger
logging.basicConfig(filename='jonathan_bot.log', level=logging.INFO)
log = logging.getLogger("jonathan_bot")
log.info(f"Jonathan bot script started at [{datetime.now()}]\n\n")

# Loading environment variables
load_dotenv(".env")

# Bot config
bot_cmdPrefix = "j:"
bot_intents = discord.Intents.default()
bot_intents.members = True
bot_intents.message_content = True
bot_desc = """Jonathan Bolbynsky bot for random stuff
Made by Arinone"""

# Bot setup
bot = commands.Bot(command_prefix=bot_cmdPrefix, description=bot_desc, intents=bot_intents)

@bot.event
async def on_ready():
    assert bot.user is not None
    print("Bot successfully connected")
    log.info("Bot connected :")
    log.info(f"User : [{bot.user}]")
    log.info(f"ID : [{bot.user.id}]")

#### Uncategorized ####
@bot.command()
async def ping(ctx: Context):
    """Checks if the bot responds."""
    await ctx.message.reply(f"Pong ! Responsive as (nearly) always, {ctx.message.author}", mention_author=True)
    log.info(f"ping triggered by [{ctx.message.author.id}] at [{datetime.now()}]")

@bot.command()
async def roll(ctx: Context, dices: int = 1, faces: int = 20):
    """Rolls dices."""
    result = cmdf.diceroll(dices, faces)
    await ctx.send(result)
    log.info(f"roll triggered by [{ctx.message.author.id}] at [{datetime.now()}] arg1 [{dices}] arg2 [{faces}]")

@bot.command()
async def dance(ctx: Context):
    """Make me dance !"""
    await ctx.send(file=File("./media/jonathan_dance.gif"))
    log.info(f"dance triggered by [{ctx.message.author.id}] at [{datetime.now()}]")

@bot.command()
async def tips(ctx: Context):
    """Gives random Aced Beyond tips alongside some real world tips."""
    result = cmdf.tips()
    await ctx.send(result)

@bot.command()
async def token(ctx: Context):
    """Grabs this bot's token."""
    await ctx.message.reply("Fuh nah :broken_heart:\nYou ain't getting no tokens blud :pray::pray:", mention_author=True, file=File("./media/eeveegun.jpg"))
    log.info(f"token triggered by [{ctx.message.author.id}] at [{datetime.now()}]")

bot.run(getenv("DISCORD_TOKEN"))