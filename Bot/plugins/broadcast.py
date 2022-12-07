import os
import pyrogram
from config import Config
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from pyrogram import Client, filters, enums
from pyrogram.types import ChatPermissions
from pyrogram.types import (Message, InlineQuery, InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent,
                            InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery)

from bot import bot as app
from bot.helpers.database import (
    get_served_users,
    add_served_user,
    remove_served_user,
    get_served_chats,
    add_served_chat,
    remove_served_chat
)

async def broadcast_messages(user_id, message):
    try:
        await message.forward(chat_id=user_id)
        return True, "Success"
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return await broadcast_messages(user_id, message)
    except InputUserDeactivated:
        await remove_served_user(user_id)
        return False, "Deleted"
    except UserIsBlocked:
        await remove_served_user(user_id)
        return False, "Blocked"
    except PeerIdInvalid:
        await remove_served_user(user_id)
        return False, "Error"
    except Exception as e:
        return False, "Error"

@app.on_message(filters.private & filters.command("bcast") & filters.user(Config.OWNER) & filters.reply)
async def broadcast_message(_, message):
    b_msg = message.reply_to_message
    chats = await get_served_users()
    m = await message.reply_text("𝙱𝚛𝚘𝚊𝚍𝚌𝚊𝚜𝚝𝚒𝚗𝚐 𝙿𝚕𝚞𝚐𝚒𝚗 𝙸𝚗𝚜𝚝𝚊𝚕𝚕𝚒𝚗𝚐..")
    for chat in chats:
        try:
            await broadcast_messages(int(chat['bot_users']), b_msg)
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await m.edit("𝙶𝚎𝚝𝚝𝚒𝚗𝚐 𝙱𝚌𝚊𝚜𝚝 𝚃𝚇𝚃..")
    await m.edit("𝚂𝚎𝚊𝚛𝚌𝚑𝚒𝚗𝚐 𝙱𝚘𝚝 𝚄𝚜𝚎𝚛𝚜.. ")
    await m.edit("𝚂𝚎𝚗𝚍𝚒𝚗𝚐..")
    await m.edit("𝙱𝚛𝚘𝚊𝚍𝚌𝚊𝚜𝚝 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚎𝚍 ✅️")

