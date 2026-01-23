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

class Technical(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.hybrid_group(aliases=["tech", "t"], fallback="technical")
    async def technical(self, ctx: Context[commands.Bot]):
        """Technical commands category.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        """
        if ctx.invoked_subcommand is None:
            await ctx.send("Technical commands for use by Arinone. Type `j:help technical` for further help.")
        log.info(f"technical triggered by [{ctx.author.id}] at [{datetime.now()}]")

    @technical.command(aliases=["sync", "csync", "treesync"])
    async def commandsync(self, ctx: Context[commands.Bot]):
        """Synchronises slash commands if sent by Arinone.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        """
        if ctx.author.id == 703959508489207838:
            await ctx.send("Syncing slash commands. Expect results to come within some time.")
            await self.bot.tree.sync()
        else:
            await ctx.send("Nuh uh, only Arinone can tell me to sync commands.", delete_after=15)
        log.info(f"technical commandsync triggered by [{ctx.author.id}] at [{datetime.now()}]")

    @technical.command()
    async def token(self, ctx: Context[commands.Bot]):
        """Grabs this bot's token.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        """
        await ctx.reply("Fuh nah :broken_heart:\nYou ain't getting no tokens blud :pray::pray:", mention_author=True, file=File(f"{getenv('BOT_ENV')}/media/eeveegun.jpg"))
        log.info(f"token triggered by [{ctx.author.id}] at [{datetime.now()}]")

    @commands.command(aliases=["say", "s"], hidden=True)
    async def messageas(self, ctx: Context, *messageWrite: str):
        msg = ""
        if ctx.author.id == 703959508489207838:
            for s in messageWrite:
                msg += s + " "
            await ctx.send(msg)
        await ctx.interaction.delete_original_response()
        log.info(f"messageas triggered by [{ctx.author.id}] at [{datetime.now()}] with args [{msg}]")

async def setup(bot):
    await bot.add_cog(Technical(bot))
    log.info(f"Cog added : technical_cog")