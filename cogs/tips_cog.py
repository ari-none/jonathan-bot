# Imports
from discord.ext import commands
import logging
import json
from datetime import datetime
from discord import File, Embed, Color, User, Status
from discord.ext import commands
from discord.ext.commands.context import Context
from os import getenv
import random as r

log = logging.getLogger("jonathan_bot")

with open(f"{getenv('BOT_ENV')}/jsonfiles/tips.json", "r") as f:
    tipsList = json.load(f)

class TipsNFacts(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.hybrid_group(aliases=["tip"], fallback="tips")
    async def tips(self, ctx: Context[commands.Bot]):
        """Random tips/facts category.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        """
        await ctx.send("Category for giving out random tips & facts. Type `j:help tips` for more information.")
        log.info(f"tips triggered by [{ctx.author.id}] at [{datetime.now()}]")

    @tips.command(aliases=["aced", "ab"])
    async def acedbeyond(self, ctx: Context[commands.Bot]):
        """Gives a tip for the game Aced Beyond.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        """
        rtip = tipsList["acedbeyond"][r.randint(0, len(tipsList["acedbeyond"]) - 1)]
        result = f"""## ——Aced Beyond Gameplay Tips——
        ```{rtip}```"""
        await ctx.send(result)
        log.info(f"tips acedbeyond triggered by [{ctx.author.id}] at [{datetime.now()}]")

    # Holy shit Psychopomp reference
    @tips.command(aliases=["real", "life", "rl", "irl"])
    async def reallife(self, ctx: Context[commands.Bot]):
        """Gives a real life tip.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        """
        rtip = tipsList["reallife"][r.randint(0, len(tipsList["reallife"]) - 1)]
        result = f"""## ——Real life Tips——
            ```{rtip}```"""
        await ctx.send(result)
        log.info(f"tips reallife triggered by [{ctx.author.id}] at [{datetime.now()}]")

async def setup(bot):
    await bot.add_cog(TipsNFacts(bot))
    log.info(f"Cog added : tips_cog")