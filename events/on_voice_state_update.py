from random import randrange

import discord
from util.globals import CLIENT, CURRENT_VOICE_CHANNEL
from util.log_error import log_error


@CLIENT.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    global CURRENT_VOICE_CHANNEL
    print(member)
    prob = randrange(0, 10)
    if(before.channel == None and prob == 0 and str(member) != "Shit-chan#7352"):
        try:
            soundbite = randrange(0, 11)
            CURRENT_VOICE_CHANNEL = await after.channel.connect()
            CURRENT_VOICE_CHANNEL.play(discord.FFmpegPCMAudio(source=open("./assets/"+str(soundbite)+".mp3","rb"),pipe=True))
            while (CURRENT_VOICE_CHANNEL.is_playing()):
                pass
            await CURRENT_VOICE_CHANNEL.disconnect()
        except Exception as e:
            log_error(e)
            print(e)
            await CURRENT_VOICE_CHANNEL.disconnect()
