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
quotes = ["Get out of the matrix","So, you were bornt to feel nice?","Stop! You are geting comfortable!", "Unexpected events occur frequently. Be Alert !Expect the unexpected !!","You will gap in your comfort zone!", "🤞 Trying then fail is better than failing to try", "🐸 Eat the Frog Conquer the struggling tasks like a pro with the Eat the Frog strategy.", "⏲️ 20 second rule; Ikk vaari shuru kar k ta'an dekh technique (for 20 sec)", "⏲️ 3, 2, 1 rule Kill procrastination by moving into action within 3 seconds.", "🚀 Move before you crave for any motivation", "0% Motivation 100% Discipline", "Sugoi! Push past the 40% potential governors barrier.", "Procrastination steals your Time; seize it back with dominance. Procrastination is the thief of Time, your enemy. (Dominate it, before it takes charge on yourself)", "☘️ Dream ↑  Efforts ↑ ( D ∝ E) As your dreams rise, let your efforts soar.", "You must ACT!  Indecision is the enemy; decisive action is the key.", "⚡ Put ENERGY, Get RESULTS Invest your energy, harvest incredible results.", "✂️ Cut fkin' distractions Achievement demands focus; eliminate distractions ruthlessly.", "The harder the battle, the sweeter the victory.", "FEAR is temporary, REGRET is permanent", "🎇 I submit to a higher power; they are acting through me.", "✨ Your worship directs the manifestation process.", "💖 As higher power says, as one worships me, that is how I manifest to them."]

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
    embed_colors=[0x64748b, 0xfed7aa, 0xf97316, 0xfef3c7, 0xfbbf24, 0x22c55e, 0x0d9488, 0x22d3ee, 0x0ea5e9, 0x8b5cf6, 0xf9a8d4, 0xf472b6, 0xfda4af]
    channel_id=1148275606635696208 #pc-config
    channel = client.get_channel(channel_id)
    choice = randint(0, len(embed_colors)-1)
    embedtry=discord.Embed(title="Finished 45m Pomodoro", description=f"{quotes[choice]} {mention}", color=embed_colors[choice])
    embedtry.set_footer(text=f"Embed Hex: {hex(embed_colors[choice])}", icon_url=None)
    await channel.send(embed=embedtry)

client.run(DISCORD_TOKEN)
print("Success!")
