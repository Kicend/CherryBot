import asyncio
import threading
import warnings
import discord
import psutil
import os
import time
from os import listdir
from os.path import isfile, join
from discord.ext import commands
from discord.ext.commands import has_permissions
from itertools import cycle
from random import randrange
from random import randint

# Moduły importowane z katalogu cherrydata
from cherrydata.modules.help import pomocy
from cherrydata.modules.rsp import rsp
from cherrydata.modules.user import user
from cherrydata.modules.coin import coin

# Import konfiguracji bota
from cherrydata.config.config import Config

"""
Zostanie to przerzucone do API
# Dodatki importowane z katalogu cherrydata
addons_path = "cherrydata/addons"
addons = [f for f in listdir(addons_path) if isfile(join(addons_path, f))]
"""

# Listy do przechowywania danych
channels = []
commands_db = ("!help", "!pomocy", "!report", "!zgłoszenie", "!user", "!reload", "!resources", "!config",
               "!moneta", "!coin", "!pkn", "!rsp", "!kostka", "!dice", "!clear", "!guild")
type_1_report_db = {}
type_2_report_db = {}
type_3_report_db = {}
type_4_report_db = {}

# Komunikaty
CONTENT = "Podaj treść zaczynając znakiem &"

# Typy zgłoszeń
CATEGORY_1 = Config.CATEGORY_1
CATEGORY_2 = Config.CATEGORY_2
CATEGORY_3 = Config.CATEGORY_3
CATEGORY_4 = Config.CATEGORY_4

# Parametry bota
TOKEN = Config.TOKEN
wersja = "0.13-4"
boot_date = time.strftime("%H:%M %d.%m.%Y UTC")

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["pomocy"])
    async def help(self, ctx, los=1):
        "Komenda do wywołania pomocy"
        await pomocy(self, ctx, los=los, wersja=wersja)

    @commands.command()
    @has_permissions(manage_messages=True)
    async def user(self, ctx, user_ext_info: discord.Member):
        "Komenda do uzyskiwania informacji o użytkowniku oznaczając go (@nick, nick lub id)"
        await user(self, ctx, user_ext_info)

    @commands.command(aliases=["zgłoszenie"])
    async def report(self, ctx):
        "Komenda do zgłaszania przeznaczona dla użytkowników"
        warnings.simplefilter("ignore", RuntimeWarning)
        ctx.channel = ctx.message.author

        await ctx.channel.send("Jaki typ zgłoszenia chcesz wysłać?\n"
                            "1 - Błąd gry\n"
                            "2 - Propozycja zmiany\n"
                            "3 - Problem z botem\n"
                            "4 - Inne\n")

        await ctx.channel.send("Wpisz numer kategorii")

        async def answer_1():
            @bot.event
            async def on_message(ctx):
                if ctx.content.startswith("&"):
                    if ctx.author.bot:
                        return
                    else:
                        message_value = ctx.content
                        if message_value in commands_db:
                            print("To była komenda")
                            await bot.process_commands(message_value)
                        else:
                            bug_channel = bot.get_channel(Config.bug_channel)
                            embed = discord.Embed(
                                colour=discord.Colour.dark_red()
                            )
                            and_position = message_value.index("&")
                            message_value_clear = message_value[and_position+1:]
                            embed.set_author(name="Zgłoszenie typu {}".format(type_1_report_db.pop(ctx.author)))
                            embed.add_field(name="Treść:", value=message_value_clear, inline=False)
                            embed.add_field(name="Zgłosił:", value="{}\nID: {}".format(ctx.author, ctx.author.id), inline=False)
                            await bug_channel.send(embed=embed)
                            await ctx.channel.send("Zgłoszenie zostało przesłane. Jeżeli chcesz wysłać kolejne wpisz !report.\n"
                                                   "Możesz to zrobić na serwerze lub na DM ze mną")
                elif ctx.content.startswith("!"):
                    await bot.process_commands(ctx)

        async def answer_2():
            @bot.event
            async def on_message(ctx):
                if ctx.content.startswith("&"):
                    if ctx.author.bot:
                        return
                    else:
                        message_value = ctx.content
                        if message_value in commands_db:
                            print("To była komenda")
                            await bot.process_commands(message_value)
                        else:
                            bug_channel = bot.get_channel(Config.bug_channel)
                            embed = discord.Embed(
                                colour=discord.Colour.dark_red()
                            )
                            and_position = message_value.index("&")
                            message_value_clear = message_value[and_position+1:]
                            embed.set_author(name="Zgłoszenie typu {}".format(type_2_report_db.pop(ctx.author)))
                            embed.add_field(name="Treść:", value=message_value_clear, inline=False)
                            embed.add_field(name="Zgłosił:", value="{}\nID: {}".format(ctx.author, ctx.author.id), inline=False)
                            await bug_channel.send(embed=embed)
                            await ctx.channel.send("Zgłoszenie zostało przesłane. Jeżeli chcesz wysłać kolejne wpisz !report.\n"
                                                   "Możesz to zrobić na serwerze lub na DM ze mną")
                elif ctx.content.startswith("!"):
                    await bot.process_commands(ctx)

        async def answer_3():
            @bot.event
            async def on_message(ctx):
                if ctx.content.startswith("&"):
                    if ctx.author.bot:
                        return
                    else:
                        message_value = ctx.content
                        if message_value in commands_db:
                            print("To była komenda")
                            await bot.process_commands(message_value)
                        else:
                            bug_channel = bot.get_channel(Config.bug_channel)
                            embed = discord.Embed(
                                colour=discord.Colour.dark_red()
                            )
                            and_position = message_value.index("&")
                            message_value_clear = message_value[and_position+1:]
                            embed.set_author(name="Zgłoszenie typu {}".format(type_3_report_db.pop(ctx.author)))
                            embed.add_field(name="Treść:", value=message_value_clear, inline=False)
                            embed.add_field(name="Zgłosił:", value="{}\nID: {}".format(ctx.author, ctx.author.id), inline=False)
                            await bug_channel.send(embed=embed)
                            await ctx.channel.send("Zgłoszenie zostało przesłane. Jeżeli chcesz wysłać kolejne wpisz !report.\n"
                                                   "Możesz to zrobić na serwerze lub na DM ze mną")
                elif ctx.content.startswith("!"):
                    await bot.process_commands(ctx)

        async def answer_4():
            @bot.event
            async def on_message(ctx):
                if ctx.content.startswith("&"):
                    if ctx.author.bot:
                        return
                    else:
                        message_value = ctx.content
                        if message_value in commands_db:
                            print("To była komenda")
                            await bot.process_commands(message_value)
                        else:
                            bug_channel = bot.get_channel(Config.bug_channel)
                            embed = discord.Embed(
                                colour=discord.Colour.dark_red()
                            )
                            and_position = message_value.index("&")
                            message_value_clear = message_value[and_position+1:]
                            embed.set_author(name="Zgłoszenie typu {}".format(type_4_report_db.pop(ctx.author)))
                            embed.add_field(name="Treść:", value=message_value_clear, inline=False)
                            embed.add_field(name="Zgłosił:", value="{}\nID: {}".format(ctx.author, ctx.author.id), inline=False)
                            await bug_channel.send(embed=embed)
                            await ctx.channel.send("Zgłoszenie zostało przesłane. Jeżeli chcesz wysłać kolejne wpisz !report.\n"
                                                   "Możesz to zrobić na serwerze lub na DM ze mną")
                elif ctx.content.startswith("!"):
                    await bot.process_commands(ctx)

        def type_1():
            type_1_report_db[ctx.author]=CATEGORY_1
            answer_1()

        def type_2():
            type_2_report_db[ctx.author]=CATEGORY_2
            answer_2()

        def type_3():
            type_3_report_db[ctx.author]=CATEGORY_3
            answer_3()

        def type_4():
            type_4_report_db[ctx.author]=CATEGORY_4
            answer_4()

        thread_1 = threading.Thread(target=type_1())
        thread_2 = threading.Thread(target=type_2())
        thread_3 = threading.Thread(target=type_3())
        thread_4 = threading.Thread(target=type_4())

        @bot.event
        async def on_message(ctx):
            if ctx.content.startswith("1"):
                await ctx.channel.send(CONTENT)
                thread_1.start()
                await answer_1()
            elif ctx.content.startswith("2"):
                await ctx.channel.send(CONTENT)
                thread_2.start()
                await answer_2()
            elif ctx.content.startswith("3"):
                await ctx.channel.send(CONTENT)
                thread_3.start()
                await answer_3()
            elif ctx.content.startswith("4"):
                await ctx.channel.send(CONTENT)
                thread_4.start()
                await answer_4()
            elif ctx.content.startswith("!"):
                await bot.process_commands(ctx)

    """
    @commands.command()
    @has_permissions(administrator=True)
    async def reload(self, ctx):
        "Komenda do odświeżenia pliku konfiguracji"
        await ctx.send("Konfiguracja bota została odświeżona")
    """

    @commands.command()
    @has_permissions(manage_messages=True)
    async def config(self, ctx):
        "Informacje o konfiguracji bota"
        embed = discord.Embed(
            colour=discord.Colour.dark_red()
        )

        embed.set_author(name="Informacje o konfiguracji bota")
        embed.add_field(name="Kanał do wysyłania zgłoszeń przez bota", value=Config.bug_channel, inline=False)
        embed.add_field(name="Kanał do pisania z botem", value=Config.bot_channel, inline=False)
        embed.add_field(name="Prefix", value=Config.commands_prefix, inline=False)

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
        server = bot.get_guild(591549514247176205)
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
        embed.add_field(name="Uruchomiony:", value=boot_date, inline=False)
        embed.add_field(name="Pomiar pulsu:", value="{} ms".format(round(bot.latency * 1000)), inline=False)
        embed.add_field(name="RAM:", value="{} MB".format(round(process.memory_info().rss / (1024 * 1024))), inline=False)
        embed.add_field(name="Wersja:", value=wersja, inline=False)
        embed.add_field(name="Biblioteka", value="discord.py 1.2.3", inline=False)
        embed.add_field(name="Autor:", value="Kicend#2690", inline=False)
        await ctx.send(embed=embed)

class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["kostka"])
    async def dice(self, ctx, boki):
        "Komenda na kostkę do gry"
        b = int(boki)
        if b == 3:
            await ctx.send("Widziałeś kiedyś kostkę 3 ścienną?")

        elif b == 2:
            await ctx.send("Rzuć se monetą, a nie głowę zawracasz")

        elif b == 1:
            await ctx.send("No bez jaj")

        else:
            a = str(randrange(1, b))

            await ctx.send("Kostka wskazuje {}".format(a))

    @commands.command(aliases=["pkn"])
    async def rsp(self, ctx, hand):
         "Papier, kamień, nożyce"
         await rsp(self, ctx, hand)

    @commands.command(aliases=["moneta"])
    async def coin(self, ctx):
        "Rzuć monetą"
        await coin(self, ctx)

    """
    @commands.command(aliases=["zgadywanka"])
    async def guess(self, ctx):
        numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

        await ctx.send("Odgadnij liczbę od 1 do 10. Masz tylko 5 sekund.")
        cho = str(randint(1, 10))

        @bot.event
        async def on_message(message):
            if message.author.bot == True:
                print("To ja")

            if message.content.startswith(numbers):
                if cho == message:
                    await ctx.send("Zgadłeś")
                else:
                    await ctx.send("Nie zgadłeś. Niestety")
    """

bot = commands.Bot(command_prefix=commands.when_mentioned_or(Config.commands_prefix),
                   description='CherryBot wersja {}'.format(wersja))

bot.remove_command("help")

bot_channel = bot.get_channel(Config.bot_channel)

# Funkcja zwracająca opóźnienie bota
async def ping():
    return round(bot.latency * 1000)

@bot.event
async def on_connect():
    print("Bot pomyślnie połączył się z Discordem\nTrwa wczytywanie danych...")

@bot.event
async def on_ready():
    print('Zalogowany jako {0} ({0.id})'.format(bot.user))
    print('-------------------------------------------------------')
    status = ["CherryBot {}".format(wersja), "!help"]
    msgs = cycle(status)
    cykl = 0
    while not bot.is_closed():
        current_status = next(msgs)
        game = discord.Game(current_status)
        await bot.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        if cykl == 2:
            game = discord.Game("Ping: {} ms".format(await ping()))
            await bot.change_presence(status=discord.Status.online, activity=game)
            await asyncio.sleep(5)
            cykl = 0
        else:
            cykl += 1

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Nie masz uprawnień do wykonania tej komendy")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Nie podałeś wymaganego argumentu")

bot.add_cog(Utilities(bot))
bot.add_cog(Entertainment(bot))
bot.run(TOKEN)

