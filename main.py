# Imports
import os
import sys

import discord
import logging
import json
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
bot_intents.guilds = True
bot_intents.guild_typing = True
bot_intents.integrations = True
bot_desc = """Jonathan Bolbynsky bot for random stuff
Made by Arinone"""

class BotUser(commands.Bot):
    async def setup_hook(self):
        with open("jsonfiles/cogs.json", "r") as f:
            cogs: list[str] = json.load(f)
            for cog in cogs:
                await self.load_extension(cog)

bot = BotUser(command_prefix=bot_cmdPrefix, intents=bot_intents, description=bot_desc)
bot.run(getenv("BOT_TOKEN"))