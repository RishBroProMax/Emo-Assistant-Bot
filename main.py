from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


API_ID = '14055090'
API_HASH = 'a46f7b439d0afa45b7a69fc450f754e9'
BOT_TOKEN = '5715378157:AAF9kdjlzO6zaEvQHVDIunKOYce3PzFQH6c'

app = Client(
  "bot",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN
)

START = """
👋Hello.. \n\n I m Assistant Bot Of Rishmika Sandanu. \n Send /help For Get All Commands.\n\n 🔰Powerd By @EmoBotDevolopers \n ❤️Credits :- @ImRishmika
"""

HELP = """
**All Commands**

/start
/help
"""

# Commands
@app.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://telegra.ph/file/79ee63a32d8e38842dfa0.jpg",caption=START,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="</> ємσ вσт ∂єνσℓσρєʀѕ", url="t.me/EmoBotDevolopers"), InlineKeyboardButton(text="💠Github💠", url="https://github.com/RishBroProMax")],[InlineKeyboardButton(text="☘️Devoloper☘️", url="https://t.me/ImRishmika")]]))

@app.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/79ee63a32d8e38842dfa0.jpg",caption=HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="</> ємσ вσт ∂єνσℓσρєʀѕ", url="t.me/EmoBotDevolopers")]]))


    
print("Bot Stated. Check Now")
app.run()
