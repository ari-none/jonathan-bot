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
def localtips() -> str:
    rtip1 = tipsList["game"][r.randint(0, len(tipsList["game"]) - 1)]
    rtip2 = tipsList["real"][r.randint(0, len(tipsList["real"]) - 1)]

    result = f"""## ——Gameplay Tips——
    ```{rtip1}```
    ## ——Real world Tips——
    ```{rtip2}```"""

    return result

class TipsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.hybrid_command(aliases=["tip"])
    async def tips(self, ctx: Context[commands.Bot]):
        """Gives random Aced Beyond tips alongside some real world tips.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        """
        result = localtips()
        await ctx.send(result)
        log.info(f"tips triggered by [{ctx.author.id}] at [{datetime.now()}]")

async def setup(bot):
    await bot.add_cog(TipsCog(bot))
    log.info(f"Cog added : tips_cog")