from datetime import timezone
from dateutil.parser import isoparse

from fktz.log import logger


def convert_timestamp(time_str: str):
    """
    Convert ISO8601 timestamp to Discord's formatted timestamp
    Usage: !ts <ISO8601_timestamp>
    Examples:
    !ts 2025-07-01T14:35:00Z
    !ts 1993-01-01T23:59:59+07:00
    """
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
    )
    return response
