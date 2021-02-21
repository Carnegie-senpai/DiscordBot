from util.globals import CLIENT
from commands.wake_on_lan_helpers import send_wol

@CLIENT.command()
async def wake(ctx):
    if ctx.author.id == 236949806386380801:
        print("waking computer")
        await send_wol()
