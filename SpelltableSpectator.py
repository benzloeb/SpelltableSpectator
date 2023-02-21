#!/usr/bin/env python3
import discord
from discord.ext import commands
import re
import random

class MyClient(discord.Client):
    client = commands.Bot(command_prefix=".")

    @client.event
    async def on_ready(self):
        print("Bot is live")

    @client.event
    async def on_message(self, message):
        if not message.author.id == self.user.id:
            if "good bot" in message.content.lower() and not message.author.id == 737417839132278954:
                await message.reply("Good human")
            # Using Regex to find spelltable links
            match = re.search("(https:\/\/)?(www\.)??(beta.)?spelltable(.wizards)\.com\/game\/.{21}", message.content)
            # If there is a match
            if match:
                # Print spectate link in the channel it was sent in.
                if "https://" in match.string:
                    await message.channel.send("Spectate the game here:\n" + match.group() + "?spectate=true")
                else:
                    await message.channel.send("Spectate the game here:\nhttps://" + match.group() + "?spectate=true")
        if message.author.id == 268547439714238465 and random.random() < 0.01:
            await message.reply("Good bot")

client = MyClient()
client.run("ODA2NDA3MzQ4NTQ1MjU3NDc1.YBo_Xg.t-IIl71vbF_hBcttfiz9stphLE0")
