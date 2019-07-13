# Zgodne z CherryBot 0.12-1
import discord

async def guild_info(self, ctx, guild: discord.Guild):
    embed = discord.Embed(
        colour=discord.Colour.dark_red()
    )

    embed.set_author(name="Informacje o serwerze")
    embed.add_field(name="Nazwa serwera:", value=guild.name, inline=False)
    embed.add_field(name="ID serwera:", value=guild.id, inline=False)
    embed.add_field(name="Dane właściela:", value="Nick: {}, ID: {}".format(guild.owner, guild.owner_id), inline=False)
    await ctx.send(embed=embed)