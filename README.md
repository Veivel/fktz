![](/docs/logo.png)
# <p align="center"> fktz </p>

A simple solution to working with [Discord Timestamps](https://gist.github.com/LeviSnoot/d9147767abeef2f770e9ddcd91eb85aa). Because f*ck timezones.

Running an international team over Discord, I got tired of manually making timestamps every time we had an event or a meeting. I also found all the existing bots tiresome: some required everyone in the team to set their timezones, while others were unnecessarily complex. Not the "quick and easy" solutions I had hoped for. 

So I built fktz; you only need to supply a ISO-8601 timestamp and the bot will do the rest for you.

## Invite Link

You can invite the bot to your Discord Server [here](https://discord.com/oauth2/authorize?client_id=1401163863960850473&permissions=3072&scope=bot).

## Usage

Command format: `!ts <ISO8601>`, example: `!ts 2025-12-30T23:59:59+04:00`. 

Timezone is offset relative to UTC, for example: `+04:00`, `-07:30`, `+00:00`. See [this wikipedia page](https://en.wikipedia.org/wiki/List_of_UTC_offsets) to find what your UTC offset is.

The visual below breaks down an ISO8601 timestamp.

![example timezone](/docs/tz.png)

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