from discord.ext.commands import Bot
from Unimpt import calcMinPrice

BOT_PREFIX = ("-")
TOKEN = "NjQ1MzI1NTM0Mzg0ODgxNjk0.XdA_sQ.yhG-em45ojN6kX6XURvVyz1ycno"

client = Bot(command_prefix=BOT_PREFIX)


#event upload image
@client.event
async def on_message(message):
    # print(message.attachments)
    channel = message.channel
    name, price, comparison = calcMinPrice.main(message.attachments[0].url)
    for i in range(len(name)):
        await channel.send(name[i]+" "+price[i])
        await channel.send(comparison[i])
    
client.run(TOKEN)