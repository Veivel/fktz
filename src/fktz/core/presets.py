import discord


def get_help_text(pre):
    response = (
        f"- `{pre}tzhelp`: Show help on bot commands.\n"
        f"- `{pre}tzgithub`: Show a link to the GitHub page for the bot.\n"
        f"- `{pre}tzformats`: Show a guide for Discord Timestamp formats.\n"
        f"- `{pre}iso8601`: Show a guide for ISO8601 timestamps.\n"
        f"- `{pre}ts <ISO8601>`: Convert your ISO8601 timestamp into a Discord Timestamp."
    )
    return response


def get_formats_text():
    response = (
        f"Example of a raw Discord Timestamp: `<t:1754494260:R>`\n"
        f"`R` is the format.\n\n"
        f"**Available formats:**\n"
        f"- `F` = Long Date/Time\n"
        f"- `R` = Relative Time\n"
        f"- `d` = Short Date\n"
        f"- `t` = Short Time\n"
        f"- `T` = Long Time"
    )
    return response


def get_iso_8601_visual() -> discord.File:
    with open("src/fktz/resources/iso8601.png", "rb") as f:
        picture = discord.File(f)
        return picture


def get_source_code_link() -> str:
    return "https://github.com/Veivel/fktz"
