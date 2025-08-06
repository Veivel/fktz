import os
import discord
from discord.ext import commands
from datetime import datetime, timezone
from dateutil.parser import isoparse
from dotenv import load_dotenv

from fktz.log import logger
from fktz.core.converter import convert_timestamp
from fktz.core.presets import (
    get_formats_text,
    get_help_text,
    get_iso_8601_visual,
    get_source_code_link,
)

intents = discord.Intents.default()
intents.message_content = True

COMMAND_PREFIX = "!"

fktz = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents, help_command=None)


@fktz.event
async def on_message(message):
    """Log all messages for debugging"""
    # Only log messages that might be commands
    if message.content.startswith(COMMAND_PREFIX):
        logger.info(f"Received message: {message.author} - {message.content}")

    # Process commands normally
    await fktz.process_commands(message)


@fktz.event
async def on_ready():
    logger.info(f"Logged in as {fktz.user.name} (ID: {fktz.user.id})")
    logger.info(
        f"Invite URL: https://discord.com/oauth2/authorize?client_id={fktz.user.id}&permissions=3072&scope=fktz"
    )
    await fktz.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=f"{COMMAND_PREFIX}tzhelp"
        )
    )


@fktz.command(name="tzhelp")
async def help_command(ctx):
    response = get_help_text(COMMAND_PREFIX)
    await ctx.send(response)


@fktz.command(name="tzformats")
async def formats_command(ctx):
    response = get_formats_text()
    await ctx.send(response)


@fktz.command(name="iso8601")
async def iso_8601_cmd(ctx):
    picture = get_iso_8601_visual()
    await ctx.send(file=picture)


@fktz.command(name="tzgithub")
async def source_link_cmd(ctx):
    response = get_source_code_link()
    await ctx.send(response)


@fktz.command(name="ts")
async def timestamp_cmd(ctx, *, time_str: str):
    pre = COMMAND_PREFIX
    
    try:
        logger.info("Processing message.")
        response = convert_timestamp(time_str)
        await ctx.send(response)

    except Exception as e:
        error_msg = (
            f"❌ Invalid timestamp format: `{str(e)}`. Please use ISO8601 format.\n\n"
            "**Examples**:\n"
            "```\n"
            f"{pre}ts 2025-07-01T14:35:00Z\n"
            f"{pre}ts 1993-01-01T23:59:59+07:00\n"
            f"{pre}ts 2030-12-31T08:30:00-05:00\n"
            "```"
        )
        await ctx.send(error_msg)


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("DISCORD_BOT_TOKEN")

    if token:
        fktz.run(token)
    else:
        logger.error("DISCORD_BOT_TOKEN environment variable not set")
