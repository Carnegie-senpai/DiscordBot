#while True:
#    print("hey")
import discord
print(discord.__version__)
from random import randrange
import threading
import schedule
import time
import asyncio
import concurrent.futures
from discord.ext import commands
import pickle
import io
import traceback


'''Todo plan:
    -Add a game role feature
        -Members can request new game roles be created
        -Members can request to be added or removed from game roles
    -Earrape troll command??
    -Strat roulette?
'''
Client = discord.Client()
client = commands.Bot(command_prefix = 'uwu ')
client.remove_command('help')

def log_error(e):
    log_file = open("shit_chan_error.txt","a")
    log_file.write("{0.tm_mon}/{0.tm_mday}/{0.tm_year} {0.tm_hour}:{0.tm_min}:{0.tm_sec}\n\n".format(time.localtime(time.time())))
    traceback.print_exc(file=log_file)
    log_file = open("shit_chan_error.txt","a")
    log_file.write("\n\n")
    log_file.close()

#Creates a second thread then uses that thread for the utility described in blaze_it
def call_blaze(client):
    second_loop = asyncio.new_event_loop()
    args = (client,second_loop)
    second_loop.run_until_complete(blaze_it([second_loop]))


#debug message that prints login time and username to console
@client.event
async def on_ready():
    print("We have logged in as {0.user} at {1.tm_hour}:{1.tm_min}".format(client,time.localtime(time.time())))

 


global current_voice_channel
global insults
global blaze
blaze = True

insults = ["cuck","weeb","liberal. Prepare to be roasted with FACTS and LOGIC",\
           "retard","absolute muffin","imbecile",\
           "literal dried piece of shit on the bottom of my shoe","cunt","scallywag",\
           "dumbass","boomer","republican","troglodyte",\
           "soggy white bread that's been left out for a few days","netherwart"]


#10% chance to play random sound clip when somebody joins a voice channel, if they previously have not been in a voice channel
@client.event
async def on_voice_state_update(member,before,after):
    global current_voice_channel
    print(member)
    prob = randrange(0,10)
    if(before.channel == None and prob == 0 and str(member) != "Shit-chan#7352"):
        try:
            soundbite = randrange(0,11)
            current_voice_channel = await after.channel.connect()
            current_voice_channel.play(discord.FFmpegPCMAudio("C:/Users/Nick/Desktop/DiscordBot/"+str(soundbite)+".mp3", executable="C:/ffmpeg-4.1.3-win64-static/bin/ffmpeg.exe"))
            while (current_voice_channel.is_playing()):
                pass
            await current_voice_channel.disconnect()
        except Exception as e:
            log_error(e)
            print(e)

def mockify(content):
    result = ""
    content = content.lower()
    for i in range(len(content)):
        if i%2 == 0:
            result += content[i]
        else:
            result += str(content[i]).upper()
    return result

#Determines if the time is 4:20:00 am/pm and sends blaze it if it is. The thread them sleeps.
async def blaze_it(l):
    loop = l[0]
    print("blaze")
    while(blaze):
        t = time.localtime(time.time())
        if ((t.tm_hour == 4 or t.tm_hour == 16) and t.tm_min == 20 and t.tm_sec == 0):
            asyncio.run_coroutine_threadsafe(discord.utils.get(client.get_all_channels(),name="general").send("Blaze it"),client.loop)
            time.sleep(2)
        time.sleep(0.5)

def drop_an_f(message):
    drop = message.find("drop")
    f = message.find("f")
    chat = message.find("chat")
    return drop < f < chat and drop != -1 and f != -1 and chat != -1

async def custom_process(ctx,message):
    print(message)

#Triggers on every message. If the message contains 'testbot' with any
#Capitalization it should respond 'testbot is a cuck'
#If the message contains 'drop an f in chat' as determined by drop_an_f it should
#reply with 'F'
#If the message contains an e it should add the clout emoji as a reaction
#Also calls the process_commands function which is a built in method to handle commands
@client.event
async def on_message(message):
    print(message.author)
    print(message.channel.id)
    global insults
    await client.process_commands(message)
    message.content = message.content.lower()
    if (message.content.find("testbot") != -1 or message.content.find("<@416768458122985473>") != -1) and not message.author.bot:
        await message.channel.send("TestBot is a cuck")
    elif drop_an_f(message.content):
        await message.channel.send("F")
    elif message.content.strip() == "e" and not message.author.bot:
        for i in range(len(client.emojis)):
            if client.emojis[i].name == "Clout":
                await message.add_reaction(client.emojis[i])
                break
    else:
        print(message.content)

#Repeated back whatever the original message said
@client.command()
async def daddy(ctx,*, arg):
    print(ctx)
    await ctx.send(arg)

#Sends an insult randomly selected from a list
@client.command()
async def insult(ctx):
    global insults
    await ctx.send("{} is a {}".format(ctx.author,insults[randrange(len(insults))]))

#The mock command which calls mockify to actually modify the text.
#Deletes the message that contains the command that triggered this call.
@client.command()
async def mock(ctx,*,arg):
    await ctx.message.delete()
    await ctx.send(mockify(arg.strip()))


global game
global side
global gametype
game = None
side = None
gametype = None

async def siege_strats(ctx):
    global game
    global side
    global gametype
    strats = {"attack": {"secure":["a1","a2"],"hostage":["a1","a2"],"bomb":["a1","a2"]},"defense": {"secure":["d1","d2"],"hostage":["d1","d2"],"bomb":["d1","d2"]}}
    await ctx.send(strats[side][gametype][randrange(0,len(strats[side][gametype]))])
    if side == "attack":
        side = "defense"
    else:
        side = "attack"
    return
    
async def csgo_strats(ctx):
    global game
    global side
    global gametype
    strats = {"attack": {"bomb":["a1","a2"]},"defense": {"bomb":["d1","d2"]}}
    await ctx.send(strats[side][gametype][randrange(0,len(strats[side][gametype]))])
    return


def verify_arguments(arg1,arg2,arg3):
    if (arg1 == None or arg1.lower() in ["siege","csgo","done","swap"]) and (arg2 == None or arg2.lower() in ["attack","defense"]) and (arg3 == None or arg3.lower() in ["hostage","bomb","secure"]):
        return False
    return True


#Strat command that should theoretically act as a strat roulette.
#Poor framework currently, not operational though should only need
#strats added
@client.command()
async def strat(ctx,arg=None,arg2=None,arg3=None):
    global game
    global side
    global gametype
    print("called strat")
    if (verify_arguments(arg,arg2,arg3)):
        await ctx.send("I didn't recognise one of your arguments")
    if arg == "done":               #resets the state to default for when game finishes
        print("finished game")
        game = None
        side = None
        gametype = None
    elif arg and arg.lower() == "swap":         #To swap sides on csgo, taken care of automatically for siege
        print("swapped sides")
        if side == "attack":
            side = "defense"
        else:
            side = "attack"
    elif game and side and gametype:#If it is already setup then just return a strat instead
        print("picking strat")
        if (game == "csgo"):
            await csgo_strats(ctx)
        elif (game == "siege"):
            await siege_strats(ctx)
        return
    else:
        if arg and arg2 and arg3 and arg.lower() == "siege" : #sets up the siege strat roulette
            print("setup siege roulette")
            game = "siege"
            side = arg2.lower()
            gametype = arg3.lower()
        elif arg and arg2 and arg.lower() == "csgo":         #sets up the csgo strat roulette
            print("setup csgo roulette")
            game = "csgo"
            side = arg2.lower()
            gametype = "bomb"
        else:                       #Default error
            await ctx.send("I couldn't process the first argument daddy.")
            return
        

#Prints general useful statement about commands if no argument or specific information if the name
#of a command is supplied. Also accepts syntax to explain the syntax of the explanations
@client.command()
async def help(ctx,arg=None):
    print(arg)
    if arg==None:
        await ctx.send("```Check your capitlization first! It matters!\ndaddy: I'll repeat back what you say to you\ninsult: I'll insult you\nmock: I'll mock whatever you say\nstrat: Used for strat roulette\nhelp: I'll help you. If you need more specific help with a command type 'uwu help *command*', or if you want help understanding my syntax type 'uwu help syntax'```")
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

#shutsdown the bot
@client.command()
async def shutdown(ctx):
    global blaze
    print("called shutdown")
    print(ctx.author.id)
    if ctx.author.id == 236949806386380801:
        print('shutting down')
        blaze = False
        await client.logout()

#causes an error for testing purposes

@client.command()
async def error(ctx):
    if ctx.author.id == 236949806386380801:
        raise Exception("Manually thrown error for testing.")


try:
    t = threading.Thread(target=call_blaze,args=[client])
    t.start()
    client.loop.run_until_complete(client.start("Mjk2MjAxMTA2NjEzMjA3MDQx.XPndFw.g-gMDqJHsVLul5x2WMlFMT-LuO0"))
except Exception as e:
    log_error(e)
    t.join()
    client.loop.run_until_complete(client.logout())
    blaze = False
    client.clear()
       # del client, Client
       # Client = discord.Client()
       # client = commands.Bot(command_prefix = 'uwu ')
       # client.remove_command('help')
