from util.globals import CLIENT
from commands.mock_helpers import mockify

@CLIENT.command()
async def mock(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(mockify(arg.strip()))