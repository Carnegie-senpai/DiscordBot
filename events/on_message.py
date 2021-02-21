from util.globals import CLIENT, INSULTS
from events.on_message_helpers import message_on_string, emoji_on_string
from random import randrange

@CLIENT.event
async def on_message(message):
    print(message.author)
    print(message.channel.id)
    global INSULTS
    await CLIENT.process_commands(message)
    message.content = message.content.lower()
    if (message.content.find("testbot") != -1 or message.content.find("<@416768458122985473>") != -1) and not message.author.bot:
        await message.channel.send("TestBot is a {}".format(INSULTS[randrange(len(INSULTS))]))
    await emoji_on_string(message,r"(.*gme.*)|(.*gamestop.*)|(.*game stop.*)","💎👐")
    await emoji_on_string(message,r"^e$","<:Clout:333845251511025684>")
    await message_on_string(message,r'drop.*f.*chat',"F")
    #Shitty puns
    await message_on_string(message,r"exactly","Who's Zack Lee?")
    await message_on_string(message,r'(yeah.*sure)|(yea.*sure)',"Who's Yasher?")
    await message_on_string(message,r"actually","Who's Ashley?")
    print(message.content)
