import discord
from discord.ext import commands, tasks

client = discord.Client()   
client= commands.Bot(command_prefix="none", self_bot=True)
client.remove_command("help")
token = "mfa.y2VE6KWz0lauLfy2fXW6eUiO9nhCrSCQeZdq4cE4BEiQVatbGCKyAQ_MCn_h3c1Uf25vXWtpAGv2KL-okU5A"

whitelist = "whitelist.txt"

file = open(whitelist, 'r')

@client.event
async def on_connect():
    for guild in client.guilds:
       for line in file:
           if guild.id != line:
                try: 
                    await guild.leave()
                except:
                    print("Cannot leave server")

client.run(token, reconnect=True, bot=False)