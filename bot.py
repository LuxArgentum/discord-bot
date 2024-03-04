import discord
from discord.ext import commands
import config


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("$hello"):
            await message.channel.send("Hello World!")


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot()


# Add the guild ids in which the slash command will appear.
# If it should be in all, remove the argument, but note that
# it will take some time (up to an hour) to register the
# command if it's for all guilds.
@bot.slash_command(name="first_slash", guild_ids=[1212927555330383912/1212927556911767643])
async def first_slash(ctx):
    await ctx.respond("You executed the slash command!")


client = MyClient(intents=intents)
client.run(config.discord_token)
