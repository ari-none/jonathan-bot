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

def clamp(n, min_value, max_value):
    return max(min_value, min(n, max_value))

def diceroll(dices: int, faces: int) -> Embed:
    emb = Embed(title=f":game_die: Dice roll :game_die: ({dices}d{faces}) :", color=Color.dark_red())

    resultString = ""
    for dice in range(dices):
        roll = r.randint(1, faces)
        resultString += f"**:game_die: Die {dice+1}** : `{roll}`\n"
    emb.description = resultString
    return emb

class Games(commands.Cog):
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
            The number of dice to roll (clamped between 1 and 15, defaults to 1)
        faces: int = 20
            The number of faces a die would have (defaults to 20 faces ; aka an icosahedron)
        """
        dices = clamp(dices, 1, 15)
        faces = clamp(faces, 1, 999999999)
        result: Embed = diceroll(dices, faces)
        await ctx.send(embed=result)
        log.info(f"roll triggered by [{ctx.author.id}] at [{datetime.now()}] arg1 [{dices}] arg2 [{faces}]")

async def setup(bot):
    await bot.add_cog(Games(bot))
    log.info(f"Cog added : diceroll_cog")