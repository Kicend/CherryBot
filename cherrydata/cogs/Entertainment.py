import asyncio
import random
from random import randrange
from discord.ext import commands
from cherrydata.modules.rsp import rsp
from cherrydata.modules.coin import coin

class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["kostka"])
    async def dice(self, ctx, boki):
        "Komenda na kostkę do gry"
        b = int(boki)
        if b == 3:
            await ctx.send("Widziałeś kiedyś kostkę trzyścienną?")

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

    @commands.command(aliases=["zgadywanka"])
    async def guess(self, ctx):
        """Odgadnij liczbę"""
        numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

        await ctx.send("Odgadnij liczbę od 1 do 10. Masz tylko 5 sekund.")
        cho = random.choice(numbers)

        try:
            msg = await self.bot.wait_for("message", timeout=5)
            if ctx.author.bot:
                return None
            elif msg.content.startswith(numbers):
                if msg.content == cho:
                    await ctx.send("Zgadłeś")
                else:
                    await ctx.send("Nie zgadłeś. Niestety")
        except asyncio.TimeoutError:
            await ctx.send("Czas minął. To była liczba {}".format(cho))

def setup(bot):
    bot.add_cog(Entertainment(bot))