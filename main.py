# Imports
import commandFunctions as cmdf
import discord
import logging
from discord import File
from discord.ext import commands
from discord.ext.commands.context import Context
from dotenv import load_dotenv
from os import getenv

# Setting up logger
logging.basicConfig(filename='jonathan_bot.log', level=logging.INFO)
log = logging.getLogger("jonathan_bot")

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
    log.info("Bot connected :")
    log.info(f"User : {bot.user}")
    log.info(f"ID : {bot.user.id}")

#### Uncategorized ####
@bot.command()
async def ping(ctx: Context):
    """Checks if the bot responds."""
    await ctx.message.reply(f"Pong ! Responsive as (nearly) always, {ctx.message.author.name}", mention_author=True)

@bot.command()
async def roll(ctx: Context, dices: int = 1, faces: int = 20):
    """Rolls dices."""
    result = cmdf.diceroll(dices, faces)
    await ctx.send(result)

@bot.command()
async def dance(ctx: Context):
    await ctx.send(file=File("./media/jonathan_dance.gif"))

@bot.command()
async def token(ctx: Context):
    """Grabs this bot's token."""
    await ctx.message.reply("Fuck you twin :broken_heart:", mention_author=True)

bot.run(getenv("DISCORD_TOKEN"))