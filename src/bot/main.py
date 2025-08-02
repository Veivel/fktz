import os
import discord
from discord.ext import commands
from datetime import datetime, timezone
from dateutil.parser import isoparse
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('discord_timestamp_bot')

# Enable required intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix='!',
    intents=intents,
    help_command=None
)

@bot.event
async def on_message(message):
    """Log all messages for debugging"""
    # Only log messages that might be commands
    if message.content.startswith('!'):
        logger.info(f"Received message: {message.author} - {message.content}")
    
    # Process commands normally
    await bot.process_commands(message)
    
@bot.command(name='help')
async def help_cmd(ctx):
    with open('src/resources/tz.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
        
@bot.command(name='github')
async def help_cmd(ctx):
    response = (
        'https://github.com/'
    )
    await ctx.send(response)

@bot.command(name='ts')
async def timestamp_cmd(ctx, *, time_str: str):
    """
    Convert ISO8601 timestamp to Discord's formatted timestamp
    Usage: !ts <ISO8601_timestamp>
    Examples:
      !ts 2025-07-01T14:35:00Z
      !ts 1993-01-01T23:59:59+07:00
    """
    try:
        logger.info("Processing message.")
        
        if time_str[10] == " ":
            time_str = time_str[:10] + "T" + time_str[11:]
        time_str = time_str.replace(".", ":")
        time_str = time_str.replace(" ", "")
        time_str = time_str.strip()
        
        # Parse ISO8601 timestamp
        dt = isoparse(time_str)
        
        # If no timezone info, treat as UTC
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
            logger.info(f"Parsed naive datetime as UTC: {dt}")
        
        # Convert to Unix timestamp (seconds)
        unix_timestamp = int(dt.timestamp())
        
        # Create Discord timestamp formats
        long_format = f"<t:{unix_timestamp}:F>"
        relative_format = f"<t:{unix_timestamp}:R>"
        raw_format = f"`<t:{unix_timestamp}:F>`"
        
        # Create response with rendered timestamp and raw format
        response = (
            f"**Long Date/Time Format**: {long_format}\n"
            f"**Relative Format**: {relative_format}\n"
            f"**Raw Format**: {raw_format}\n\n"
            # f"**Tip for Raw Format:**\n"
            # f"- `F` = Long Date/Time\n"
            # f"- `R` = Relative Time\n"
            # f"- `d` = Short Date\n"
            # f"- `t` = Short Time\n"
            # f"- `T` = Long Time"
        )
        
        await ctx.send(response)
        
    except Exception as e:
        error_msg = (
            f"❌ Invalid timestamp format: `{str(e)}`. Please use ISO8601 format.\n\n"
            "**Examples**:\n"
            "```\n"
            "!ts 2025-07-01T14:35:00Z\n"
            "!ts 1993-01-01T23:59:59+07:00\n"
            "!ts 2030-12-31T08:30:00-05:00\n"
            "```"
        )
        await ctx.send(error_msg)

@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    logger.info(f'Invite URL: https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=3072&scope=bot')
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening,
        name="!ts <ISO8601>"
    ))

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('DISCORD_BOT_TOKEN')
    if token:
        bot.run(token)
    else:
        logger.error("DISCORD_BOT_TOKEN environment variable not set")
        print("Please set the DISCORD_BOT_TOKEN environment variable")