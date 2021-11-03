import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import requests
import json
import time
import datetime

# configuring discord bot
PREFIX = ("$")
client = commands.Bot(command_prefix = PREFIX, description = 'Hi')

# bot status
@client.event
async def on_ready():
    while True:
        # defining vitex api
        url = "https://vitex.vite.net/api/v1/exchange-rate?tokenSymbols=VITC-000"
        # connecting to the api
        response = requests.get(url)
        # setting up parsing
        response = requests.get(url)
        data = response.text
        parsed = json.loads(data)
        data = parsed["data"]
        type(data)
        usdRate = data[0]['usdRate']
        time.sleep(1)
        localtime = time.asctime( time.localtime(time.time()) )
        # changing status
        await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = str(usdRate) + "$"))
        # printing VITC value!
        print("<===============Made by:5am===============>")
        print("VITC's price @ " + str(localtime) + " is $" + str(usdRate))

client.run('token')
