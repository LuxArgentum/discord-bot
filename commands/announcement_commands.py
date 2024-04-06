import discord
import os

from discord.ext import commands


class AnnouncementCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='announcement', description='Make an announcement!',
                            guild_ids=[os.environ['SERVER_ID']])
    @discord.default_permissions(manage_messages=True)
    async def announcement(self, ctx, announcement_message: discord.Option(str, "Enter your announcement")):
        await ctx.respond(f'@everyone\n'
                          f'\n'
                          f'{announcement_message}')


def setup(bot):
    bot.add_cog(AnnouncementCommands(bot))
