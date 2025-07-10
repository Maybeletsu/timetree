import os, asyncio, pytz, datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv
import discord
from timetree import TimeTreeClient

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))
TT_TOKEN = os.getenv("TIMETREE_TOKEN")
TT_CAL_ID = os.getenv("TIMETREE_CALENDAR_ID")
TZ = pytz.timezone("Asia/Tokyo")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
scheduler = AsyncIOScheduler(timezone=TZ)

tt = TimeTreeClient(TT_TOKEN, TT_CAL_ID)

async def send_today_events():
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print("Channel not found!")
        return
    events = tt.get_today_events()
    if not events:
        await channel.send("今日は予定がありません。")
        return
    lines = ["**今日の予定**"]
    for ev in events:
        lines.append(f"• {ev['start']} – {ev['title']}")
    await channel.send("\n".join(lines))

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    # run at startup
    asyncio.create_task(send_today_events())

# schedule daily at 08:00
scheduler.add_job(lambda: asyncio.create_task(send_today_events()), "cron", hour=8, minute=0)
scheduler.start()

client.run(DISCORD_TOKEN)
