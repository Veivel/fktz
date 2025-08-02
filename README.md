# fktz

A simple solution to working with [Discord Timestamps](https://gist.github.com/LeviSnoot/d9147767abeef2f770e9ddcd91eb85aa). Because f*ck timezones.

Running an international team over Discord, I got tired of manually making timestamps every time we had an event or a meeting. I also found all the existing bots tiresome: some required everyone in the team to set their timezones, while others were unnecessarily complex. Not the "quick and easy" solutions I had hoped for. 

So I built fktz; you only need to supply a ISO-8601 timestamp and the bot will do the rest for you.

## Invite Link

https://discord.com/oauth2/authorize?client_id=1401163863960850473&permissions=3072&scope=bot

## Usage

Example command: `!ts 2025-12-30T23:59:59+04:00`
![example timezone](/docs/tz.png)

Timezone is relative to UTC, for example: `+04:30`, `-07:00`, `+00:00`

## Build from Source

If you prefer running the bot from the source code over inviting the discord bot through the invite link above, you may do so:

#### Running with uv

1. Run `uv venv`

2. Run `source .venv/bin/activate/`

3. Run `uv sync`

4. Populate `.env` secrets

5. Run `python3 src/bot/main.py`

#### Running with Docker

1. Run `docker compose up`