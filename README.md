# TimeTree Notice Bot (Python)

Fetches today's TimeTree events every morning at 08:00 (local timezone) and posts them to a specified Discord channel.

## Features
- Daily digest of events with start time, title, and URL
- Optional 10‑minute before-event reminders
- Configurable via environment variables
- Runs on plain Python or Docker

## Quick Start

```bash
git clone <your repo url>
cd TimeTree-NoticeBot
cp .env.example .env        # fill in the tokens
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python bot.py
```

### Environment variables (`.env`)

| Variable | Description |
|----------|-------------|
| `DISCORD_TOKEN` | Discord Bot token |
| `DISCORD_CHANNEL_ID` | Channel ID to post messages |
| `TIMETREE_TOKEN` | TimeTree API Personal Access Token |
| `TIMETREE_CALENDAR_ID` | Calendar ID |

### Docker

```bash
docker compose up -d
```

## Credit
Inspired by [watasuke102/TimeTree-NoticeBot](https://github.com/watasuke102/TimeTree-NoticeBot) (archived).
