# WIP: discordpy-logging-handler

Forward Discord bot logs to Discord Text channel.

## Usage

```python
import logging

import discord
from discordpy_logging_handler import DiscordBotHandler


LOG_TEXT_CHANNEL_ID = 1111111111111

logger = logging.getLogger(__name__)


class MyClient(discord.Client):
    async def on_ready(self):
        logger.info('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        logger.info('Message from {0.author}: {0.content}'.format(message))


client = MyClient()
client.run('my token goes here')

log_channel = client.get_channel(LOG_TEXT_CHANNEL_ID)
logger.setLevel(logging.DEBUG)

handler = DiscordBotHandler(log_channel)
handler.setLevel(logging.INFO)

# add ch to logger
logger.addHandler(handler)
```

