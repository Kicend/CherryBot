# Zgodne z CherryBot 0.12-7
import random

async def coin(self, ctx):
    sides = ["orzeł", "reszka"]
    side = random.choice(sides)

    if side == "orzeł":
        await ctx.send("Wypadł orzeł")
    else:
        await ctx.send("Wypadła reszka")
