import discord
from discord.ext import commands, tasks

client = discord.Client()   
client= commands.Bot(command_prefix="none", self_bot=True)
client.remove_command("help")
token = "add_your_token"

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
