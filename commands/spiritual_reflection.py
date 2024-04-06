import os

from discord.ext import commands
from modals.quiet_time import QuietTimeModal
from modals.share_scripture import ShareScriptureModal


class SpiritualReflectionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="quiet-time", description="Share your quiet time!",
                            guild_ids=[os.environ['SERVER_ID']])
    async def quiet_time(self, ctx):
        modal = QuietTimeModal(title="Quiet Time")
        await ctx.send_modal(modal)

    @commands.slash_command(name="share-scripture", description="Share a scripture!",
                            guild_ids=[os.environ['SERVER_ID']])
    async def share_scripture(self, ctx):
        modal = ShareScriptureModal(title="Share Scripture")
        await ctx.send_modal(modal)


def setup(bot):
    bot.add_cog(SpiritualReflectionCog(bot))
