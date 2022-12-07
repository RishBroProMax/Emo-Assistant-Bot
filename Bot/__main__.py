import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from Bot import bot as app
from plugins import*
from main import BOTS, START, HELP

@app.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://telegra.ph/file/c4ea3761bb73bab726334.jpg",caption=START,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="</> ємσ вσт ∂єνσℓσρєʀѕ", url="t.me/EmoBotDevolopers"), InlineKeyboardButton(text="💠Github💠", url="https://github.com/RishBroProMax")],[InlineKeyboardButton(text="☘️Devoloper☘️", url="https://t.me/ImRishmika")]]))

@app.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/c4ea3761bb73bab726334.jpg",caption=HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="</> ємσ вσт ∂єνσℓσρєʀѕ", url="t.me/EmoBotDevolopers")]]))

@app.on_message(filters.command("bots"))
async def bots(bot, message):
  await message.reply_photo("https://telegra.ph/file/c4ea3761bb73bab726334.jpg",caption=BOTS,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="</> ємσ вσт ∂єνσℓσρєʀѕ", url="t.me/EmoBotDevolopers")]]))


