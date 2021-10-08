### Bot file goes here. You can either upload your own or simply replace this file.
### If you upload your own file or rename the .py, make sure to change the directory location in our Procfile.

# For Heroku, make sure your .py includes the following.
import discord
from discord.ext import commands
import asyncio
import os # import the OS details, including our hidden bot token
leaf2 = os.environ.get('leaf2') # fetch the token from Heroku's "OS" running the bot. make sure the name matches the one you've used on Heroku
client = discord.Client()

bot = commands.Bot(command_prefix='Leaf.')



async def my_background_task():
    channel = client.get_channel(895809139006132277) # replace with target channel id
   while True:
        await channel.send("s.fish")
        await asyncio.sleep(300) # or 300 if you wish for it to be 5 minutes

@client.event
async def on_ready():
    bot.loop.create_task(my_background_task())

# Include this at the end of your code. Instead of bot, you may have "discord.Client()" "commands.Bot()" etc, or whatever you have defined these.
client.run(leaf2) # make sure your token variable matches the token defined above
