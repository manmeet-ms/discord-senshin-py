# MADE FOR GITHUB ACITONS
import time
import os
import discord
from  random import randint
from requests import get
from bs4 import BeautifulSoup
import asyncio
# from dotenv import load_dotenv
# load_dotenv()
# DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50', 'Accept-Language': 'en-US, en;q=0.5',}
quotes = [
"🧠 You have power over your mind",
"✨ Your worship directs the manifestation process.",
"🌌 The higher power says, as one worships me, that is how I manifest to them.",
"🎇 I submit to a higher power; they are acting through me.",
"📆 A pinch of hardwork everyday, can put you years ahead of your life",
"🏆 The harder the battle, the sweeter the victory.",
"🚫 0% Motivation 100% Discipline",
"👀 Unexpected events occur frequently. Be Alert! Expect the unexpected.",
"💻 You have to get out of the matrix",
"So, you were born to feel nice?",
"🛋️ You will gap in your comfort zone!",
"🤞 Trying then fail is better than failing to try",
"🐸 Eat the Frog Conquer the struggling tasks like a pro with the Eat the Frog strategy.",
"⏲️ Just start it for 20 second rule",
"⏲️ 3, 2, 1 rule Kill procrastination by moving into action within 3 seconds.",
"🚀 Move before you crave for any motivation",
"🚧 Push past the 40% potential brain governors\' barrier.",
"⏰ Procrastination steals your Time; seize it back with dominance",
"☘️ Dream ↑  Efforts ↑ (D ∝ E) As your dreams rise, soar your efforts.",
"🚶‍♂️ Indecision is the enemy; You must ACT!",
"⚡ Put ENERGY, Get RESULTS.",
"✂️ Cut fkin' distractions; achievement demands focus.",
"Fear/Doubt/Hesistation is temporary, REGRET is permanent",
]
# Discord starts 
intent=discord.Intents.default()
client=discord.Client(intents=intent)


@client.event
async def on_ready():
    print(f'Logged in As {client.user}')
    try:
        await send_message()
    except Exception as e:
        print(e)
    finally:
        await client.close() # To close the connection after out job is done whether successfully or not

async def send_message():
    global quotes
    mention='<@788713878963748876>'
    #embed_colors=[0x64748b, 0xfed7aa, 0xf97316, 0xfef3c7, 0xfbbf24, 0x22c55e, 0x0d9488, 0x22d3ee, 0x0ea5e9, 0x8b5cf6, 0xf9a8d4, 0xf472b6, 0xfda4af]
    channel_id=1148275606635696208 #pc-config
    channel = client.get_channel(channel_id)
    choice = randint(0, len(embed_colors)-1)
    embedtry=discord.Embed(description=f"{quotes[choice]} {mention}", color=0xfed7aa)

    embedtry.set_footer(text=f"Pomodoro Duration: 45m\nEmbed Hex: {hex(embed_colors[choice])}", icon_url=None)
    await channel.send(embed=embedtry)

client.run(DISCORD_TOKEN)
print("Success!")
