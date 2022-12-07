import os
import pyrogram
from config import Config
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from pyrogram import Client, filters, enums
from pyrogram.types import ChatPermissions
from pyrogram.types import (Message, InlineQuery, InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent,
                            InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery)
from Userbot import bot as stats
from Userbot.helpers.database import (
    get_served_users,
    add_served_user,
    remove_served_user,
    get_served_chats,
    add_served_chat,
    remove_served_chat
)

from datetime import datetime
from time import time
import psutil
from psutil._common import bytes2human


async def _human_time_duration(seconds):
	if seconds == 0:
		return 'inf'
	parts = []
	for unit, div in TIME_DURATION_UNITS:
		amount, seconds = divmod(int(seconds), div)
		if amount > 0:
			parts.append('{} {}{}'
				.format(amount, unit, "" if amount == 1 else "s"))
	return ', '.join(parts)


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
	('week', 60 * 60 * 24 * 7),
	('day', 60 * 60 * 24),
	('hour', 60 * 60),
	('min', 60),
	('sec', 1)
)

@stats.on_message(filters.private & filters.command("ping") & filters.user(Config.OWNER))
async def get_uptime(_, m: Message):
	current_time = datetime.utcnow()
	uptime_sec = (current_time - START_TIME).total_seconds()
	uptime = await _human_time_duration(int(uptime_sec))
	start = time()
	delta_ping = time() - start
	await m.reply_text(
		f"**💠 | Uptime :** `{uptime}`\n"
		f"**💠 | Ping :** `{delta_ping * 1000:.3f} ms`"
		)


async def generate_sysinfo(workdir):
    info = {
        'boot': (datetime.fromtimestamp(psutil.boot_time())
                 .strftime("%Y-%m-%d %H:%M:%S"))
    }
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    info['cpu'] = (
        f"{psutil.cpu_percent(interval=1)}% "
        f"({psutil.cpu_count()}) "
        f"{cpu_freq}"
    )
    vm = psutil.virtual_memory()
    sm = psutil.swap_memory()
    info['ram'] = (f"{bytes2human(vm.total)}, "
                   f"{bytes2human(vm.available)} available")
    info['swap'] = f"{bytes2human(sm.total)}, {sm.percent}%"
    du = psutil.disk_usage(workdir)
    dio = psutil.disk_io_counters()
    info['disk'] = (f"{bytes2human(du.used)} / {bytes2human(du.total)} "
                    f"({du.percent}%)")
    if dio:
        info['disk io'] = (f"R {bytes2human(dio.read_bytes)} | "
                           f"W {bytes2human(dio.write_bytes)}")
    nio = psutil.net_io_counters()
    info['net io'] = (f"TX {bytes2human(nio.bytes_sent)} | "
                      f"RX {bytes2human(nio.bytes_recv)}")
    sensors_temperatures = psutil.sensors_temperatures()
    if sensors_temperatures:
        temperatures_list = [
            x.current
            for x in sensors_temperatures['coretemp']
        ]
        temperatures = sum(temperatures_list) / len(temperatures_list)
        info['temp'] = f"{temperatures}\u00b0C"
    info = {f"{key}:": value for (key, value) in info.items()}
    max_len = max(len(x) for x in info)
    return ("```"
            + "\n".join([f"{x:<{max_len}} {y}" for x, y in info.items()])
            + "```")

@stats.on_message(filters.private & filters.command("sys") & filters.user(Config.OWNER))
async def get_sysinfo(client, m):
    response = "**🚧 System Information 🚧**\n"
    m_reply = await m.reply_text(f"{response}`...`")
    response += await generate_sysinfo(client.workdir)
    await m_reply.edit_text(response)


@stats.on_message(filters.command("stats") & filters.user(Config.OWNER))
async def stats(_, message):
    m = await message.reply_text(text=f"Getting Stats...")
    served_chats = len(await get_served_chats())
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    served_users = len(await get_served_users())
    served_users = []
    users = await get_served_users()
    for user in users:
        served_users.append(int(user["bot_users"]))

    await m.edit(
        text=f"""
**🍀 Chats Stats 🍀**

🙋‍♂️ Users : `{len(served_users)}`
👥 Groups : `{len(served_chats)}`
🚧 Total users & groups : {int((len(served_chats) + len(served_users)))} """)
