import psutil
import os
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from cherrydata.config import config
from cherrydata.modules.help import pomocy
from cherrydata.modules.user import user

# Listy do przechowywania danych
channels = []
type_1_report_db = {}
type_2_report_db = {}
type_3_report_db = {}
type_4_report_db = {}

# Typy zgłoszeń
CATEGORY_1 = config.CATEGORY_1
CATEGORY_2 = config.CATEGORY_2
CATEGORY_3 = config.CATEGORY_3
CATEGORY_4 = config.CATEGORY_4

# Komunikaty
CONTENT = "Podaj treść zaczynając znakiem &"

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["pomocy"])
    async def help(self, ctx, los=1):
        "Komenda do wywołania pomocy"
        await pomocy(self, ctx, los=los, wersja=config.wersja)

    @commands.command()
    @has_permissions(manage_messages=True)
    async def user(self, ctx, user_ext_info: discord.Member):
        "Komenda do uzyskiwania informacji o użytkowniku oznaczając go (@nick, nick lub id)"
        await user(self, ctx, user_ext_info)

    # @commands.command(aliases=["zgłoszenie"])
    # async def report(self, ctx):
        # "Komenda do zgłaszania przeznaczona dla użytkowników"

    @commands.command()
    @has_permissions(manage_messages=True)
    async def config(self, ctx):
        "Informacje o konfiguracji bota"
        embed = discord.Embed(
            colour=discord.Colour.dark_red()
        )

        embed.set_author(name="Informacje o konfiguracji bota")
        embed.add_field(name="Kanał do wysyłania zgłoszeń przez bota", value=config.bug_channel, inline=False)
        embed.add_field(name="Kanał do pisania z botem", value=config.bot_channel, inline=False)
        embed.add_field(name="Prefix", value=config.commands_prefix, inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int, member: discord.Member = None):
        "Komenda do czyszczenia historii czatu"
        deleted = await ctx.channel.purge(limit=amount, check=member)
        if len(deleted) == 1:
            await ctx.send("Usunięto {} wiadomość".format(len(deleted)))
        else:
            await ctx.send("Usunięto {} wiadomości".format(len(deleted)))

    @commands.command()
    async def guild(self, ctx):
        """Komenda do uzyskania informacji o serwerze"""
        server = self.bot.get_guild(591549514247176205)
        roles = [role for role in server.roles]
        embed = discord.Embed(
            colour=discord.Colour.dark_red()
        )

        embed.set_author(name="Informacje o serwerze")
        embed.set_thumbnail(url=server.icon_url)
        embed.add_field(name="Nazwa serwera:", value=server.name, inline=False)
        embed.add_field(name="ID serwera:", value=server.id, inline=False)
        embed.add_field(name="Dane właściciela:", value="Nick: {}, ID: {}".format(server.owner, server.owner_id), inline=False)
        embed.add_field(name="Role ({}):".format(len(roles)), value="".join([role.mention for role in roles]), inline=False)
        embed.add_field(name="Region serwera:", value=server.region, inline=False)
        embed.add_field(name="Serwer założony:", value=server.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Liczba użytkowników:", value=str(len(server.members)), inline=False)
        embed.set_footer(text="Prośba o dane od {}".format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx):
        """Komenda do sprawdzenia informacji o bocie"""
        process = psutil.Process(os.getpid())
        embed = discord.Embed(
            colour=discord.Colour.dark_red()
        )

        embed.set_author(name="Informacje o bocie")
        embed.add_field(name="Godność:", value="Nick: CherryBot#1453, ID: 596419695389966346", inline=False)
        embed.add_field(name="Uruchomiony:", value=config.boot_date, inline=False)
        embed.add_field(name="Pomiar pulsu:", value="{} ms".format(round(self.bot.latency * 1000)), inline=False)
        embed.add_field(name="RAM:", value="{} MB".format(round(process.memory_info().rss / (1024 * 1024))), inline=False)
        embed.add_field(name="Wersja:", value=config.wersja, inline=False)
        embed.add_field(name="Biblioteka", value="discord.py 1.2.3", inline=False)
        embed.add_field(name="Autor:", value="Kicend#2690", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Utilities(bot))
