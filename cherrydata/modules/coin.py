# Zgodne z CherryBot 0.13-4
import random

async def coin(self, ctx):
    sides = ["orzeł", "reszka"]
    side = random.choice(sides)

    if side == "orzeł":
        await ctx.send("Wypadł orzeł")
    else:
        await ctx.send("Wypadła reszka")
