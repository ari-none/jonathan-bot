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

def coolness_rd(user: User) -> str:
    # Yes it's rigged.
    preval = r.gauss(mu=75, sigma=40)  # center at 75
    val = max(0, min(100, round(preval)))

    # val = r.randint(0, 100) --Old code (true "random")
    if val == 100:
        return "[100%] The coolest user you'll ever see :sunglasses:"
    elif val >= 75:
        return f"[{val}%] {user.display_name} is really cool ! :star2:"
    elif val >= 50:
        return f"[{val}%] {user.display_name} is pretty cool actually :kissing_smiling_eyes:"
    elif val >= 30:
        return f"[{val}%] I guess {user.display_name} is somewhat okay :neutral_face:"
    elif val >= 15:
        return f"[{val}%] {user.display_name} ain't cool."
    elif val >= 1:
        return f"[{val}%] {user.display_name} REALLY ain't cool."
    else:
        return f"[{val}%] {user.display_name} ! GET YOUR BITCH ASS OUT—"

def localcoolness(user: User) -> tuple[Embed, bool]:
    if not user:
        return Embed(), False # Empty embed for failing return

    emb = Embed(color=Color.green(), title="Coolness meter")

    # Special user cases (well it's supposed to be a bot for friends ; so I thought that kind of function would be cool
    # I mean I don't think that's specifically against any TOS or anything)
    match user.id:
        case 1:
            emb.description = "Value"
            return emb, True
        case 1463098594016886969:
            emb.description = f"[∞%] It's me. No one's cooler than I am :sunglasses:"
            return emb, True
        case 877550294785986571:
            emb.description = f"[0%] No comment."
            return emb, True
        case 703959508489207838:
            emb.description = f"[100%] It's Arinone. Who could hate such a cute jolteon ?~ Aight ok I'll stop acting corny. Or not :upside_down:"
            return emb, True
        case 1221056132504621152:
            emb.description = f"[15%] It's Pandoro, the funny italian guy ! I gave him a 15% because he forgot to put pineapple & chicken on my pizza :face_with_symbols_over_mouth:"
            return emb, True
        case 812837395493027921:
            emb.description = f"[100%] Forob cool. Forob nimble. Forob quick. :fire:"
            return emb, True
        case 1080187557498851478:
            emb.description = f"[100%] Funny wheel guy. I like your vids. Also don't worry about the haters, they're as unintelligent as rooms fetuses."
            return emb, True
        case 1334941225538686996:
            emb.description = f"[100%] Really cool, please make my shop's music theme for Aced Beyond :pray::pray:"
            return emb, True
        case 1268111519909154919:
            emb.description = f"[50%] Could've been cooler if you could properly type in my commands with the correct syntax :confused:"
            return emb, True
        case _:
            emb.description = coolness_rd(user)
            return emb, True

class Rating(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

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
        emb, success = localcoolness(user)
        if success:
            await ctx.send(embed=emb)
        else:
            await ctx.send("You must mention an user in order to rate them !", delete_after=15)
        log.info(f"coolness triggered by [{ctx.author.id}] at [{datetime.now()}] with arg1 [{user.id}]")

async def setup(bot):
    await bot.add_cog(Rating(bot))
    log.info(f"Cog added : rating_cog")