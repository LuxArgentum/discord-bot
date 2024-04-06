import os

import discord

from modals.quiet_time import QuietTimeModal
from modals.share_scripture import ShareScriptureModal

port = int(os.environ.get('PORT', 5000))  # Default to 5000 for local testing

bot = discord.Bot()
bot.auto_sync_commands = True

bot.load_extension('commands.event_handler')
bot.load_extension('commands.community_commands')
bot.load_extension('commands.announcement_commands')
bot.load_extension('commands.spiritual_reflection')

bot.run(os.environ["DISCORD_TOKEN"])
