# Imports
from discord.ext import commands
import logging
import json
from datetime import datetime
from discord import File, Embed, Color, User, Status
from discord.ext import commands
from discord.ext.commands.context import Context
from os import getenv

log = logging.getLogger("jonathan_bot")

class BotCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command()
    async def ping(self, ctx: Context[commands.Bot]):
        """Checks if the bot responds.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        """
        await ctx.message.reply(f"Pong !", mention_author=True)
        log.info(f"ping triggered by [{ctx.message.author.id}] at [{datetime.now()}]")

    @commands.hybrid_command()
    async def dance(self, ctx: Context[commands.Bot]):
        """Make me dance !

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        """
        await ctx.send(file=File(f"{getenv("BOT_ENV")}/media/jonathan_dance.gif"))
        log.info(f"dance triggered by [{ctx.message.author.id}] at [{datetime.now()}]")

async def setup(bot):
    await bot.add_cog(BotCog(bot))
    log.info(f"Cog added : general_cog")