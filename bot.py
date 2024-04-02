import os

import discord
from discord import default_permissions

port = int(os.environ.get('PORT', 5000))  # Default to 5000 for local testing

bot = discord.Bot()
bot.auto_sync_commands = True


# @bot.event
# async def on_ready():
#     channel = bot.get_channel(int(os.environ['BOT_CHANNEL']))
#     await channel.send('Bot is now running!\n'
#                        f'Current Time: {discord.utils.utcnow()}')
#     await bot.sync_commands()


@bot.slash_command(name='hello', description='Say hello!', guild_ids=[os.environ['SERVER_ID']])
async def hello(ctx):
    await ctx.respond(f'Hello, {ctx.user.mention}!', ephemeral=True)


@bot.slash_command(name='announcement', description='Make an announcement!', guild_ids=[os.environ['SERVER_ID']])
@default_permissions(manage_messages=True)
async def announcement(ctx, announcement_message: discord.Option(str, "Enter your announcement")):
    await ctx.respond(f'@everyone\n'
                      f'\n'
                      f'{announcement_message}')


class quiet_time_modal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Start Verse", placeholder="Book Chapter:Verse"))
        self.add_item(discord.ui.InputText(label="End Verse", placeholder="Book Chapter:Verse"))
        self.add_item(discord.ui.InputText(label="Additional Scriptures"))
        self.add_item(discord.ui.InputText(label="Summary", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        user = interaction.user.display_name
        embed = discord.Embed(title=f"My Quiet Time", color=discord.Color.blurple())
        embed.author = discord.EmbedAuthor(name=user, icon_url=interaction.user.avatar.url)

        embed.add_field(name="Start Verse", value=self.children[0].value)
        embed.add_field(name="End Verse", value=self.children[1].value)
        embed.add_field(name="Additional Scriptures", value=self.children[2].value, inline=False, required=False)
        embed.add_field(name="Summary", value=self.children[3].value, inline=False)
        channel = bot.get_channel(int(os.environ['QUIET_TIME_CHANNEL']))
        await channel.send(embeds=[embed])
        await interaction.response.send_message("Your quiet time has been shared!", ephemeral=True)


@bot.slash_command(name="quiet-time", description="Share your quiet time!", guild_ids=[os.environ['SERVER_ID']])
async def modal_slash(ctx: discord.ApplicationContext):
    modal = quiet_time_modal(title="Quiet Time")
    await ctx.send_modal(modal)


# @bot.slash_command(name="prayer-request", description="Share your prayer request!", guild_ids=[os.environ['SERVER_ID']])

class share_scripture_modal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Verse", placeholder="Book Chapter:Verse"))
        self.add_item(discord.ui.InputText(label="Scripture Text", placeholder="Copy & Paste the scripture here",
                                           style=discord.InputTextStyle.long))
        self.add_item(discord.ui.InputText(label="Summary", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        user = interaction.user.display_name
        embed = discord.Embed(title=f"My Quiet Time", color=discord.Color.blurple())
        embed.author = discord.EmbedAuthor(name=user, icon_url=interaction.user.avatar.url)

        embed.add_field(name="Verse", value=self.children[0].value)
        embed.add_field(name="Scripture", value=self.children[1].value, inline=False)
        embed.add_field(name="Summary", value=self.children[2].value, inline=False)
        await interaction.response.send(embeds=[embed])


@bot.slash_command(name="share-scripture", description="Share a scripture!", guild_ids=[os.environ['SERVER_ID']])
async def share_scripture(ctx: discord.ApplicationContext):
    modal = share_scripture_modal(title="Share Scripture")
    await ctx.send_modal(modal)


bot.run(os.environ["DISCORD_TOKEN"])
