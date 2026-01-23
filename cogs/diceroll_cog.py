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

def diceroll(dices: int, faces: int) -> str:
    dices = max(dices, 1)
    faces = max(faces, 1)
    resultString = f"## Dice roll (d{faces}) :\n\n"
    for dice in range(dices):
        roll = r.randint(1, faces)
        resultString += f"**Die {dice+1}** : `{roll}`\n"
    return  resultString

class DiceCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.hybrid_command(aliases=["dice", "diceroll", "rolldice"])
    async def roll(self, ctx: Context[commands.Bot], dices: int = 1, faces: int = 20):
        """Rolls dices.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        dices: int = 1
            The number of dice to roll (defaults to 1)
        faces: int = 20
            The number of faces a die would have (defaults to 20 faces ; aka an icosahedron)
        """
        result = diceroll(dices, faces)
        await ctx.send(result)
        log.info(f"roll triggered by [{ctx.author.id}] at [{datetime.now()}] arg1 [{dices}] arg2 [{faces}]")

async def setup(bot):
    await bot.add_cog(DiceCog(bot))
    log.info(f"Cog added : diceroll_cog")