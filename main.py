# Imports
import os
import sys

import commandFunctions as cmdf
import discord
import logging
from datetime import datetime
from discord import File, Embed, Color, User, Status
from discord.ext import commands
from discord.ext.commands.context import Context
from dotenv import load_dotenv
from os import getenv

# Setting up logger
logging.basicConfig(filename=f'logs/jonathan_bot_{datetime.now()}.log', level=logging.INFO)
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
    await bot.change_presence(status=Status.online, activity=discord.Streaming(name="j:help", url="https://www.roblox.com/communities/875621560/Litany-Studios#!/about"))
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

@bot.command(aliases=["dice", "diceroll", "rolldice"])
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

@bot.command(aliases=["tip"])
async def tips(ctx: Context):
    """Gives random Aced Beyond tips alongside some real world tips."""
    result = cmdf.tips()
    await ctx.send(result)
    log.info(f"tips triggered by [{ctx.message.author.id}] at [{datetime.now()}]")

@bot.command()
async def token(ctx: Context):
    """Grabs this bot's token."""
    await ctx.message.reply("Fuh nah :broken_heart:\nYou ain't getting no tokens blud :pray::pray:", mention_author=True, file=File("./media/eeveegun.jpg"))
    log.info(f"token triggered by [{ctx.message.author.id}] at [{datetime.now()}]")

# @bot.command()
# async def embedtest(ctx: Context):
#     """Testing embeds"""
#     emb = Embed(color=Color.from_rgb(255, 255, 0), title="Embed test", description="A test embed, with a cute eevee pic there")
#     emb.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic0.gamerantimages.com%2Fwordpress%2Fwp-content%2Fuploads%2F2025%2F02%2Fpokemon-eevee-standard-shiny.jpg&f=1&nofb=1&ipt=37238d99e1282e95d67e98b6e965908e2de51bf865fa704ec900b111ab48f553")
#     await ctx.send(embed=emb)

@bot.command(aliases=["cool"])
async def coolness(ctx: Context, user:User):
    """Tests how cool a user is."""
    emb, success = cmdf.coolness(user)
    if success:
        await ctx.send(embed=emb)
    else:
        await ctx.send("You must mention an user in order to rate them !")
    log.info(f"coolness triggered by [{ctx.message.author.id}] at [{datetime.now()}] with arg1 [{user.id}]")



#### Technical ####
@bot.group(aliases=["tech", "t"])
async def technical(ctx: Context):
    """Technical commands category."""
    if ctx.invoked_subcommand is None:
        await ctx.send("Technical commands for use by Arinone. Type `j:help technical` for further help.")
    log.info(f"technical triggered by [{ctx.message.author.id}] at [{datetime.now()}]")

@technical.command(aliases=["goodnight", "night", "s"])
async def sleep(ctx: Context):
    """Puts me to sleep if sent by Arinone."""
    if ctx.message.author.id == 703959508489207838:
        await bot.change_presence(status=Status.offline)
        await ctx.send("Oh ok, good night unc Ari.")
        exit()
    else:
        await ctx.send("Nuh uh, only Arinone can tell me to go to sleep.")
    log.info(f"sleep triggered by [{ctx.message.author.id}] at [{datetime.now()}]")

@technical.command(aliases=["reboot", "r"])
async def restart(ctx: Context):
    """Makes me restart if sent by Arinone."""
    if ctx.message.author.id == 703959508489207838:
        await bot.change_presence(status=Status.idle)
        await ctx.send("Oh ok, see you again unc Ari.")
        os.execv(sys.executable, ['python'] + sys.argv)
    else:
        await ctx.send("Nuh uh, only Arinone can tell me to restart.")
    log.info(f"restart triggered by [{ctx.message.author.id}] at [{datetime.now()}]")



bot.run(getenv("DISCORD_TOKEN"))