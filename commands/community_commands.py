import os

from discord.ext import commands


class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='hello', description='Say hello!', guild_ids=[os.environ['SERVER_ID']])
    async def hello(self, ctx):
        await ctx.respond(f'Hello, {ctx.user.mention}!', ephemeral=True)

    @commands.slash_command(name="prayer-request", description="Share your prayer request!",
                            guild_ids=[os.environ['SERVER_ID']])
    async def prayer_request(self, ctx):
        await ctx.respond("Prayer request command is not yet implemented.", ephemeral=True)

    # Evangelism Looking For Group
    @commands.slash_command(name="evangelism-lfg", description="Looking for group for evangelism!",
                            guild_ids=[os.environ['SERVER_ID']])
    async def evangelism_lfg(self, ctx):
        await ctx.respond("Evangelism LFG command is not yet implemented.", ephemeral=True)


def setup(bot):
    bot.add_cog(GeneralCommands(bot))
