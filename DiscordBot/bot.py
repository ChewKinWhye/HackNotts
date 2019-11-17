from discord.ext.commands import Bot
import random
import discord
import calcMinPrice

BOT_PREFIX = ("!")
TOKEN = "NjQ1NDIzMTg2ODMzMzA5NzEz.XdCYhg.cqsC3fSwJ_06m_vEYisNnIk-tAA"

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
    print(message.attachments[0].url)
    # channel = message.channel
    # name, price, comparison = calcMinPrice.main(message.attachments[0].url)
    # for i in range(len(name)):
    #     await channel.send(name[i]+" "+price)
    #     await channel.send(comparison[i])

client.run(TOKEN)