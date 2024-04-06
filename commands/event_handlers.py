import os

from discord.ext import commands


class EventHandlers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(int(os.environ['BOT_CHANNEL']))
        await channel.send(f"Bot is ready. Logged in as {self.bot.user}")
        await self.bot.sync_commands()


def setup(bot):
    bot.add_cog(EventHandlers(bot))
