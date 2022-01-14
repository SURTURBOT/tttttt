# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#

import asyncio

from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from userbot.plugins.sql_helper.gvar_sql import *
from userbot.utils import admin_cmd, sudo_cmd

from . import legend_mention

SUDO_WALA = Config.SUDO_USERS
lg_id = Config.LOGGER_ID






@bot.on(admin_cmd("wspam (.*)"))
@bot.on(sudo_cmd(pattern="wspam (.*)", allow_sudo=True))
async def spam(event):
    wspam = str("".join(event.text.split(maxsplit=1)[1:]))
    message = wspam.split()
    await event.delete()
    for word in message:
        await event.respond(word)
    if lg_id:
        if event.is_private:
            await event.client.send_message(
                lg_id,
                "#WSPAM\n"
                + f"Word Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with : `{message}`",
            )
        else:
            await event.client.send_message(
                lg_id,
                "#WSPAM\n"
                + f"Word Spam was executed successfully in {legend_mention} chat with : `{message}`",
            )




CmdHelp("spam").add_command(
    "spam", "<number> <text>", "Sends the text 'X' number of times.", "spam 99 hello"
).add_command(
    "mspam",
    "<reply to media> <number>",
    "Sends the replied media (gif/ video/ sticker/ pic) 'X' number of times",
    "mspam 100 <reply to media>",
).add_command(
    "dspam",
    "<delay> <spam count> <text>",
    "Sends the text 'X' number of times in 'Y' seconds of delay",
    "dspam 5 100 hello",
).add_command(
    "bigspam",
    "<count> <text>",
    "Sends the text 'X' number of times. This what LEGENDBOT iz known for. The Best BigSpam Ever",
    "bigspam 5000 hello",
).add_command(
    "cspam",
    "<sentence>",
    "Spam the chat with every letter in given sentence as new message",
    "cspam LEGENDBOT IS OP",
).add_command(
    "wspam",
    "<sentence>",
    "Spams the chat with every word in given sentence as new message",
    "wspam LEGENDBOT IS OP",
).add()
