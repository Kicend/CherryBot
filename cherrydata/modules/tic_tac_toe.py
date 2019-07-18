# Zgodne z CherryBot 0.14-4
import discord

async def tic_tac_toe(self, ctx, member: discord.Member):
    id_db = []

    guild = ctx.message.guild
    if id_db == []:
        id = 0
        id_db.append(id)
        await guild.create_text_channel("ttt board {}".format(id))
    else:
        id = len(id_db) + 1
        id_db.append(id)
        await guild.create_text_channel("ttt board {}".format(id))