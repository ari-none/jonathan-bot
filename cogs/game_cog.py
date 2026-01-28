# Imports
import logging
from datetime import datetime
from os import getenv
from typing import Literal, get_args

from discord import Embed, Color, User, File
from discord.ext import commands
from discord.ext.commands.context import Context

import random as r
from .extensions import coolness, rps

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

    @commands.hybrid_command(aliases=["rps"])
    async def rockpaperscissors(self, ctx: Context[commands.Bot],
                                choice: Literal["help", "rock", "paper", "scissors", "fennec", "gun", "water", "dude"]):
        """Plays a game of Rock Paper Scissors Fennec Gun Water Dude against Jonathan.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        choice: Literal["help", "rock", "paper", "scissors", "fennec", "gun", "water", "dude"]
            The choice (or help to send the RPS diagram)
        """
        if choice == "help":
            await ctx.send("Here's how the game works (via this extremely high quality diagram drawn by Arinone himself) !", file=File(f"{getenv('BOT_ENV')}/media/aris_rps.png"))
        else:
            bot_choice: str = rps.e_list[r.randint(1, len(rps.e_list))]

            title, desc, color = rps.rps(choice, bot_choice)

            emb = Embed(title=title, description=desc, color=color)
            await ctx.send(f"I chose the {bot_choice}.", embed=emb)
        log.info(f"rockpaperscissors triggered by [{ctx.author.id}] at [{datetime.now()}] with arg1 [{choice}]")

    @commands.hybrid_command(aliases=["rps"])
    async def minesweeper(self, ctx: Context[commands.Bot], rows: int, columns: int):
        """Generates a minesweeper grid (from 5x5 to 40x40).

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        rows: int
            The row length of the board (minimum 5, maximum 40)
        columns: int
            The column length of the board (minimum 5, maximum 40)
        """
        rows = clamp(rows, 5, 40)
        columns = clamp(columns, 5, 40)


        emb = Embed(title=f"Here's a {rows}x{columns} grid ! Play by unspoilering the cells. (If you hit a bomb, you lose.)",
                    description=desc, color=Color.light_gray())
        await ctx.send(f"I chose the {bot_choice}.", embed=emb)
        log.info(f"rockpaperscissors triggered by [{ctx.author.id}] at [{datetime.now()}] with arg1 [{choice}]")

async def setup(bot):
    await bot.add_cog(Games(bot))
    log.info(f"Cog added : game_cog")