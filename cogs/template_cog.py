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

class SuperCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.hybrid_command(aliases=["t"])
    async def template(self, ctx: Context[commands.Bot]):
        """Template command.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        """
        await ctx.reply("Template message invoked via template cog.")
        log.info(f"template triggered by [{ctx.author.id}] at [{datetime.now()}]")

async def setup(bot):
    await bot.add_cog(SuperCog(bot))
    log.info(f"Cog added : template_cog")