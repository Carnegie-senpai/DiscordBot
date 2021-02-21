from util.globals import CLIENT

# Prints general useful statement about commands if no argument or specific information if the name
# of a command is supplied. Also accepts syntax to explain the syntax of the explanations
@CLIENT.command()
async def help(ctx, arg=None):
    print(arg)
    if arg == None:
        await ctx.send("```Check your capitalization first! It matters!\ndaddy: I'll repeat back what you say to you\ninsult: I'll insult you\nmock: I'll mock whatever you say\nstrat: Used for strat roulette\nhelp: I'll help you. If you need more specific help with a command type 'uwu help *command*', or if you want help understanding my syntax type 'uwu help syntax'```")
    elif arg == "insult":
        await ctx.send("```To use type 'uwu insult'\nI will then send you a random insult.```")
    elif arg == "daddy":
        await ctx.send("```To use type 'uwu daddy ...'\nAnything you type after daddy I will repeat back to you.```")
    elif arg == "mock":
        await ctx.send("```To use type 'uwu mock ...'\nAnything you type after mock I will mock you with.```")
    elif arg == "strat":
        await ctx.send("```This command is complicated.\n\tTo setup a strat roulette game type 'uwu strat **game** **side** *gamemode*' gamemode is only required for siege.\n\t\tgame = siege/csgo\n\t\tside = attack/defense\n\t\tgamemode = bomb/hostage/secure\n\tOnce the game is setup call 'uwu strat' to get a strat\n\tTo end a game 'uwu strat done'\n\tTo manually swap sides (necessary for csgo) type 'uwu strat swap'```")
    elif arg == "help":
        await ctx.send("```To use type 'help *command*'\nI will help you with that command.```")
    elif arg == "syntax":
        await ctx.send("```*text* = An optional argument.\n**text** = A required argument.\n... = A string of any length.```")
