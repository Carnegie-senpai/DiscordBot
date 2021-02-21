from random import randrange
from util.globals import CLIENT, INSULTS

@CLIENT.command()
async def insult(ctx):
    global INSULTS
    await ctx.send("{} is a {}".format(str(ctx.author)[:-5], INSULTS[randrange(len(INSULTS))]))
