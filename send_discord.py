import discord
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

async def send_discord_message(message):
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        channel = client.get_channel(DISCORD_CHANNEL_ID)
        await channel.send(message)
        await client.close()

    await client.start(DISCORD_TOKEN)
