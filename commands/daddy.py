from util.globals import CLIENT

@CLIENT.command()
async def daddy(ctx, *, arg):
    print(ctx)
    await ctx.send(arg)
