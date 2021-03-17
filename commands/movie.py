from util.globals import CLIENT
from commands.movie_helper import run_model

@CLIENT.command()
async def movie(ctx, *, arg):
    await ctx.send(str(run_model(arg.strip())))