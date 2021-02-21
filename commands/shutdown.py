#from util.globals import CLIENT, BLAZE
import util.globals
@util.globals.CLIENT.command()
async def shutdown(ctx):
    print("called shutdown")
    print(ctx.author.id)
    if ctx.author.id == 236949806386380801:
        print('shutting down')
        util.globals.BLAZE = False
        await util.globals.CLIENT.logout()
