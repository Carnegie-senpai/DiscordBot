from util.globals import CLIENT

@CLIENT.command()
async def error(ctx):
    if ctx.author.id == 236949806386380801:
        raise Exception("Manually thrown error for testing.")
