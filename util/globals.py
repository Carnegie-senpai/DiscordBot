from discord.ext import commands
global CURRENT_VOICE_CHANNEL
global INSULTS
global BLAZE
global CLIENT

CLIENT = commands.Bot(command_prefix='uwu ')
CLIENT.remove_command('help')
BLAZE = True

INSULTS = ["cuck", "weeb", "liberal. Prepare to be roasted with FACTS and LOGIC",
           "retard", "absolute muffin", "imbecile",
           "literal dried piece of shit on the bottom of my shoe", "cunt", "scallywag",
           "dumbass", "boomer", "republican", "troglodyte",
           "soggy white bread that's been left out for a few days", "netherwart",
           "coward with paper hands", "smelly boi"]

CURRENT_VOICE_CHANNEL = None