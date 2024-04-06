import os

import discord

from bot import bot


class QuietTimeModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Start Verse", placeholder="Book Chapter:Verse"))
        self.add_item(discord.ui.InputText(label="End Verse", placeholder="Book Chapter:Verse"))
        self.add_item(discord.ui.InputText(label="Additional Scriptures", required=False))
        self.add_item(discord.ui.InputText(label="Summary", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        user = interaction.user.display_name
        embed = discord.Embed(title=f"My Quiet Time", color=discord.Color.blurple())
        embed.author = discord.EmbedAuthor(name=user, icon_url=interaction.user.avatar.url)

        embed.add_field(name="Start Verse", value=self.children[0].value)
        embed.add_field(name="End Verse", value=self.children[1].value)
        embed.add_field(name="Additional Scriptures", value=self.children[2].value, inline=False)
        embed.add_field(name="Summary", value=self.children[3].value, inline=False)
        channel = bot.get_channel(int(os.environ['QUIET_TIME_CHANNEL']))
        await channel.send(embeds=[embed])
        await interaction.response.send_message("Your quiet time has been shared!", ephemeral=True)
