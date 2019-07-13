# Zgodne z CherryBot 0.12-7
import discord

async def pomocy(self, ctx, los, wersja):
    decyzja = int(los)
    embed = discord.Embed(
        colour=discord.Colour.dark_red()
    )

    if decyzja == 1:
        embed.set_author(name="Sekcja pomocy bota CherrySupport wersja {} strona 1/2".format(wersja))
        embed.add_field(name="!help", value="Wywołuje menu pomocy", inline=False)
        embed.add_field(name="!report", value="Narzędzie do zgłaszania", inline=False)
        embed.add_field(name="!guild", value="Informacje o serwerze", inline=False)
        embed.add_field(name="!kostka <liczba ścianek>", value="Kostka do gry", inline=False)
        embed.add_field(name="!pkn <papier, kamień lub nożyce>", value="Papier, kamień, nożyce", inline=False)
        embed.add_field(name="!moneta", value="Rzuć monetą", inline=False)

        await ctx.send(embed=embed)

    if decyzja == 2:
        embed.set_author(name="Sekcja pomocy bota CherrySupport wersja {} strona 2/2".format(wersja))
        embed.add_field(name="!user <@nick, nick lub id>", value="Uzyskiwanie informacji o użytkowniku (dla moderacji)", inline=False)
        embed.add_field(name="!reload", value="Odświeżenie konfiguracji bota (dla administracji)", inline=False)
        embed.add_field(name="!config", value="Informacje o konfiguracji bota (dla moderacji)", inline=False)
        embed.add_field(name="!clear <ilość> <osoba (opcjonalnie)>", value="Usuwanie historii czatu (dla moderacji)", inline=False)
        embed.add_field(name="!resources", value="Pokazuje zużycie zasobów przez bota (dla moderacji)", inline=False)

        await ctx.send(embed=embed)