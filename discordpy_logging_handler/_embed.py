import discord

from ._datetime import aware_now


# 共通で利用するカスタム embed を返します
def get_custum_embed() -> discord.Embed:
    embed = discord.Embed()
    embed.timestamp = aware_now()

    return embed
