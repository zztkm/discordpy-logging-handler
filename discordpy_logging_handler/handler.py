import asyncio
import logging
import traceback

import discord
from discord import Color

from ._datetime import aware_now
from ._embed import get_custum_embed


class DiscordBotHandler(logging.Handler):
    def __init__(self, log_channel: discord.TextChannel) -> None:
        logging.Handler.__init__(self)
        self.log_channel = log_channel
        self.colors = {
            "DEBUG": Color.blue(),
            "INFO": Color.from_rgb(255, 255, 255),
            "WARNING": Color.from_rgb(255, 255, 0),
            "CRITICAL": Color.from_rgb(255, 255, 0),
            "ERROR": Color.red(),
        }

    def set_channel(self, log_channel: discord.TextChannel):
        self.log_channel = log_channel

    async def send_log(self, embed):
        await self.log_channel.send(embed=embed)

    def emit(self, record):
        try:
            timestamp = aware_now()
            embed = get_custum_embed()
            level = record.levelname
            logger_name = record.name
            msg = record.getMessage()
            log_body = f"{timestamp} | {level} | {logger_name} | {record.name}:{record.funcName}:{record.lineno} - {msg}"
            embed.color = self.colors[level]
            embed.add_field(name=record.levelname, value=f"```{log_body}```")
            asyncio.create_task(self.send_log(embed))
        except Exception as e:
            print(repr(e))
            print(traceback.format_exc())
            self.handleError(record)
