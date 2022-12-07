import os
from pyrogram import Client
from pyrogram.types import Message
from Bot.helpers.database import (
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


async def AddChatToDatabase(bot: Client, cmd: Message):
    if not await is_served_chat(cmd.chat.id):
        await add_served_chat(cmd.chat.id)

