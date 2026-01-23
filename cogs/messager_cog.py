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

class Messager(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.hybrid_group(aliases=["msg", "m"], fallback="messager")
    async def messager(self, ctx: Context[commands.Bot]):
        """Messager commands category.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        """
        if ctx.invoked_subcommand is None:
            await ctx.send("""Messager commands for writing messages.
            Type `j:messager read` to get the last message.
            Type `j:messager write <message>` to write a message that's readable by anyone (no weird stuff please).
            Type `j:messager report` to report the latest message (and maybe ban the user if the reports are valid).
            Type `j:help messager` for further help.""")
        log.info(f"messager triggered by [{ctx.author.id}] at [{datetime.now()}]")

    @messager.command(aliases=["w", "override", "over"])
    async def write(self, ctx: Context[commands.Bot], *, messageWrite: str):
        """Writes a message to the messager.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        *messageWrite: str
            The messages to write (if you put multiple messages, they will be concatenated together)
        """
        with open(f"{getenv('BOT_ENV')}/jsonfiles/messager_ban.json") as bans:
            banlist = json.load(bans)
        if ctx.author.id in banlist:
            await ctx.send(
                "You are banned from writing to the messager.\nPlease DM <@703959508489207838> for further inquiries.")
            return

        if not messageWrite:
            await ctx.send("Must provide a message !")
            return
#        msg = ""
#        for s in messageWrite:
#            msg += s + " "
        with open(f"{getenv('BOT_ENV')}/jsonfiles/memory.json", "r") as mem:
            j = json.load(mem)
        j['messager_message'] = messageWrite
        j['messager_user'] = ctx.author.id
        with open("jsonfiles/memory.json", "w") as mem:
            json.dump(j, mem, indent=2)
        await ctx.send("Message written ! Use `j:messager read` to read it.")
        log.info(f"messager write triggered by [{ctx.author.id}] at [{datetime.now()}] with arg1 [{messageWrite}]")

    @messager.command(aliases=["r", "show", "see", "s"])
    async def read(self, ctx: Context[commands.Bot]):
        """Reads the messager's message.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        """
        with open(f"{getenv('BOT_ENV')}/jsonfiles/memory.json") as f:
            mem = json.load(f)
        emb = Embed(color=Color.dark_blue(), title=mem['messager_message'],
                    description=f"This message was written by <@{mem['messager_user']}>")
        await ctx.send(embed=emb)

    @messager.command()
    async def report(self, ctx: Context[commands.Bot]):
        """Sends a report of the latest message to Arinone.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        """
        with open(f"{getenv('BOT_ENV')}/jsonfiles/messager_ban.json") as bans:
            banlist = json.load(bans)
        if ctx.author.id in banlist:
            await ctx.send(
                "You are banned from writing to the messager.\nPlease DM <@703959508489207838> for further inquiries.")
            return

        with open(f"{getenv('BOT_ENV')}/jsonfiles/memory.json") as f:
            mem = json.load(f)
        if mem['messager_user'] == 0 or mem['messager_user'] is None:
            await ctx.send("There's no messages to report !")
            return

        ari = await self.bot.fetch_user(703959508489207838)
        emb = Embed(color=Color.dark_blue(), title=mem['messager_message'],
                    description=f"This message was written by <@{mem['messager_user']}>")
        await ari.send(f"New report from <@{ctx.author.id}> !!", embed=emb)

        mem['messager_message'] = "No messages for now…"
        mem['messager_user'] = 0

        with open(f"{getenv('BOT_ENV')}/jsonfiles/memory.json", "w") as f:
            json.dump(mem, f, indent=2)

        await ctx.send(
            "Report submitted for the latest message ! The suspicious message has been cancelled just in case.\n**Any false reports and/or mass reports will result in a ban from the messager service.**")

    @messager.command()
    async def ban(self, ctx: Context[commands.Bot], user: User):
        """Arinone-only command for banning users from the Messager.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        user: discord.User
            The user to ban
        """
        if ctx.author.id == 703959508489207838:
            with open(f"{getenv('BOT_ENV')}/jsonfiles/messager_ban.json") as f:
                banlist: list[int] = json.load(f)

            if not user.id in banlist:
                banlist.append(user.id)
            else:
                await ctx.send(f"User <@{user.id}> is already banned !")
                return

            with open(f"{getenv('BOT_ENV')}/jsonfiles/messager_ban.json", "w") as f:
                json.dump(banlist, f, indent=2)
            await ctx.send(f"User <@{user.id}> successfully banned from the Messager.")
        else:
            await ctx.interaction.delete_original_response()

    @messager.command(aliases=["uban"])
    async def unban(self, ctx: Context[commands.Bot], user: User):
        """Arinone-only command for unbanning users from the Messager.

        Parameters
        ----------
        ctx: commands.Context
            The context of the command invocation
        user: discord.User
            The user to unban
        """
        if ctx.author.id == 703959508489207838:
            with open(f"{getenv('BOT_ENV')}/jsonfiles/messager_ban.json") as f:
                banlist: list[int] = json.load(f)

            if user.id in banlist:
                banlist.remove(user.id)
            else:
                await ctx.send(f"User <@{user.id}> isn't even banned !")
                return

            with open(f"{getenv('BOT_ENV')}/jsonfiles/messager_ban.json", "w") as f:
                json.dump(banlist, f, indent=2)
            await ctx.send(f"User <@{user.id}> successfully unbanned from the Messager.")
        else:
            await ctx.interaction.delete_original_response()

async def setup(bot):
    await bot.add_cog(Messager(bot))
    log.info(f"Cog added : messager_cog")