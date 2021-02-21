import asyncio
import threading
import time
import discord
from commands import *
from events import *
from util import *
import util

print(discord.__version__)

# Creates a second thread then uses that thread for the utility described in blaze_it
def call_blaze():
    second_loop = asyncio.new_event_loop()
    second_loop.run_until_complete(blaze_it())

# Determines if the time is 4:20:00 am/pm and sends blaze it if it is. The thread them sleeps.
async def blaze_it():
    #global BLAZE
    print("blaze")
    while(util.globals.BLAZE):
        t = time.localtime(time.time())
        if ((t.tm_hour == 4 or t.tm_hour == 16) and t.tm_min == 20 and t.tm_sec == 0):
            asyncio.run_coroutine_threadsafe(discord.utils.get(
                CLIENT.get_all_channels(), name="general").send("Blaze it"), CLIENT.loop)
            time.sleep(2)
        elif (t.tm_hour == 20 and t.tm_min == 0 and t.tm_sec == 0):
            asyncio.run_coroutine_threadsafe(discord.utils.get(
                CLIENT.get_all_channels(), name="general").send("<@236949806386380801> you're a piece of shit, do something about it"), CLIENT.loop)
            time.sleep(2)
        time.sleep(0.5)

try:
    t = threading.Thread(target=call_blaze)
    t.start()
    CLIENT.loop.run_until_complete(CLIENT.start(
        open("token", "r").readline().strip()))
except Exception as e:
    log_error(e)
    t.join()
    CLIENT.loop.run_until_complete(CLIENT.logout())
    util.globals.BLAZE = False
    CLIENT.clear()
