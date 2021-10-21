from util.globals import CLIENT
import commands.music_helpers
@CLIENT.command()
async def play(ctx, *, arg):
    await ctx.send("play")

# @CLIENT.command()
# def stop(ctx, *, arg):
#     pass

# @CLIENT.command()
# def queue(ctx, *, arg):
#     pass

# @CLIENT.command()
# def clear(ctx, *, arg):
#     pass

# @CLIENT.command()
# def remove(ctx, *, arg):
#     pass