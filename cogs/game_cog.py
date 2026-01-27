# Imports
import logging
from datetime import datetime
from discord import Embed, Color, User
from discord.ext import commands
from discord.ext.commands.context import Context

import random as r
from .extensions import coolness

log = logging.getLogger("jonathan_bot")

# Odd how Lua has a clamp function but not python for some reason
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
        faces = clamp(faces, 1, 999999999) # I lied ! It's actually clamped !!!
        result: Embed = diceroll(dices, faces)
        await ctx.send(embed=result)
        log.info(f"roll triggered by [{ctx.author.id}] at [{datetime.now()}] arg1 [{dices}] arg2 [{faces}]")

    @commands.hybrid_command(aliases=["cool"])
    async def coolness(self, ctx: Context[commands.Bot], user: User):
        """Tests how cool a user is.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        user: discord.User
            The user to rate
        """
        emb, success = coolness.localcoolness(user)
        if success:
            await ctx.send(embed=emb)
        else:
            await ctx.send("You must mention an user in order to rate them !", delete_after=15)
        log.info(f"coolness triggered by [{ctx.author.id}] at [{datetime.now()}] with arg1 [{user.id}]")

async def setup(bot):
    await bot.add_cog(Games(bot))
    log.info(f"Cog added : game_cog")