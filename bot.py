import os

import discord

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print("Logged on as {0}!".format(self.user))
#
#
# client = MyClient()
# client.run(os.environ["DISCORD_TOKEN"])

bot = discord.Bot()
bot.auto_sync_commands = True


@bot.event
async def on_ready():
    channel = bot.get_channel(1212927556911767645)
    await channel.send('Bot is now running!\n'
                       f'Current Time: {discord.utils.utcnow()}')
    await bot.sync_commands()


@bot.slash_command(name='hello', description='Say hello!', guild_ids=[1212927555330383912])
async def hello(command_context):
    await command_context.respond(f'Hello, {command_context.author.name}!', ephemeral=True)


@bot.slash_command(name='announcement', description='Make an announcement!', guild_ids=[1212927555330383912])
async def announcement(command_context, announcement_message: discord.Option(str, "Enter your announcement")):
    await command_context.respond(f'@everyone\n'
                                  f'\n'
                                  f'{announcement_message}')


bot.run(os.environ["DISCORD_TOKEN"])
