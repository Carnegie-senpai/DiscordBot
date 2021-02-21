import re

async def message_on_string(message,trigger,response):
    if (re.search(trigger,message.content)):
        await message.channel.send(response)

async def emoji_on_string(message,trigger,emoji):
    if (re.search(trigger,message.content)):
        if (len(emoji) > 1 and not re.search(r"<:.*:.*>",emoji) ):
            for i in emoji:
                await message.add_reaction(i)
        else:
            await message.add_reaction(emoji)
