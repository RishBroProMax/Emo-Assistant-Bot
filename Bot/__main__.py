from time import sleep
from config import Config
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, CallbackQuery, InlineQuery, InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
from requests import get,post
import asyncio
import logging
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
import requests
from Bot import LOG
from Bot.database.addusers import AddUserToDatabase, AddChatToDatabase
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram import Client, filters
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

async def main_startup():
    await app.start()
    logging.info("Emo Assistant Bot Alive..")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(main_startup())
