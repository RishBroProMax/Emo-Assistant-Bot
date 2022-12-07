import os
from pyrogram import Client
from config import Config
from pyrogram.types import Message
from Userbot.helpers.database import (
    is_served_user,
    get_served_users,
    add_served_user,
    remove_served_user,
    is_served_chat,
    get_served_chats,
    add_served_chat,
    remove_served_chat
)

async def AddUserToDatabase(bot: Client, cmd: Message):
    if not await is_served_user(cmd.from_user.id):
        await add_served_user(cmd.from_user.id)
        if Config.LOG_GRP is not None:
            await bot.send_message(
                Config.LOG_GRP,
                f"""
**#NEW_USER**

📛 **NAME**   :[{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})
👤 **USER ID**:`{cmd.from_user.id}`

**[{Config.BOT_NAME} ✅](https://t.me/{Config.BOT_USERNAME})**
""",
                disable_web_page_preview=True
                )

async def AddChatToDatabase(bot: Client, cmd: Message):
    if not await is_served_chat(cmd.chat.id):
        await add_served_chat(cmd.chat.id)
        if Config.LOG_GRP is not None:
            await bot.send_message(
                Config.LOG_GRP,
                f"""
**#NEW_CHAT**

📛 **CHAT NAME**:[Link](tg://user?id={cmd.chat.id})
👤 **CHAT ID**  :`{cmd.chat.id}`

**[{Config.BOT_NAME} ✅](https://t.me/{Config.BOT_USERNAME})**
""",
                disable_web_page_preview=True
            )
