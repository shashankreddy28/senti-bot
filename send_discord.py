import discord
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

async def send_discord_message(message, channel_name="stock-sentiment"):
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        target_channel = None
        for guild in client.guilds:
            for channel in guild.text_channels:
                if channel.name == channel_name:
                    target_channel = channel
                    break
            if target_channel:
                break

        if not target_channel:
            # If the specific channel is not found, send to the first available text channel
            for guild in client.guilds:
                for channel in guild.text_channels:
                    target_channel = channel
                    break
                if target_channel:
                    break
        
        if target_channel:
            await target_channel.send(message)
        else:
            print(f"Could not find any text channel to send message to.")

        await client.close()

    await client.start(DISCORD_TOKEN)
