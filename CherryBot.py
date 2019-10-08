import asyncio
import discord
from discord.ext import commands
from itertools import cycle

# Import konfiguracji bota
from cherrydata.config import config

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config.commands_prefix),
                   description='CherryBot wersja {}'.format(config.wersja))

bot.remove_command("help")

bot_channel = bot.get_channel(config.bot_channel)

# Funkcja zwracająca opóźnienie bota
async def ping():
    return round(bot.latency * 1000)

@bot.event
async def on_connect():
    print("Bot pomyślnie połączył się z Discordem\nTrwa wczytywanie danych...")
    for cog in config.__cogs__:
        try:
            bot.load_extension(cog)
        except:
            print("Nie udało się załadować rozszerzenia")

@bot.event
async def on_ready():
    print('Zalogowany jako {0} ({0.id})'.format(bot.user))
    print('-------------------------------------------------------')
    status = ["CherryBot {}".format(config.wersja), "!help"]
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
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Nie podałeś wymaganego argumentu")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("Nie mam uprawnień do wykonania tej komendy")

bot.run(config.TOKEN)
