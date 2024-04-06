import os

from bot_instance import bot

bot.load_extension('commands.event_handler')
bot.load_extension('commands.community_commands')
bot.load_extension('commands.announcement_commands')
bot.load_extension('commands.spiritual_reflection')

bot.run(os.environ["DISCORD_TOKEN"])
