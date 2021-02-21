from util.globals import CLIENT
import time

@CLIENT.event
async def on_ready():
    print("We have logged in as {0.user} at {1.tm_hour}:{1.tm_min}".format(
        CLIENT, time.localtime(time.time())))
