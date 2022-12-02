from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

API_ID = '14055090'
API_HASH = 'a46f7b439d0afa45b7a69fc450f754e9'
BOT_TOKEN = '5715378157:AAF9kdjlzO6zaEvQHVDIunKOYce3PzFQH6c'

bot = Client(
    "lol",
    api_id=API_ID,
    api_hash=API_HASH, 
    bot_token=BOT_TOKEN,
)

START = "👋Hello.. \n\n I m Assistant Bot Of Team Emo. \n Send /help For Get All Commands.\n\n 🔰Powerd By @EmoBotDevolopers \n ❤️Credits :- @ImRishmika"

# Start Massege

@bot.on.message(filters.command("start"))
async def start(bot, Message):
    await message.reply_photo("https://telegra.ph/file/79ee63a32d8e38842dfa0.jpg",captioin=start,reply_markup=InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="</> ємσ вσт ∂єνσℓσρєʀѕ", url="https://t.me/EmoBotDevolopers")
        ],
        [
            InlineKeyboardButton(text="⭕Subscribe Now ⭕", url="https://youtube.com/@Rish_Bro")
        ]
    ]
    )
  )


# Help Massege

@bot.on_message(filters.command("help"))
async def start(_, m : Message):
    await m.reply_text("🧩Commands \n\n /start - Start Message \n\n /help - Help Message \n\n /masseges - Get Bot Information \n /bots - More Bots \n /about  - About Massege")

# About MAssege

@bot.on_message(filters.command("about"))
async def start(_, m : Message):
    await m.reply_text("✨ About Me \n\n 🧑‍💻Devoloper - @ImRishmika \n\n 📡API - ImRishmika API \n\n 💻Host Sever - Raliway")

# More Bots

@bot.on_message(filters.command("bots"))
async def start(_, m : Message):
    await m.reply_text("🧩BOTS Stetus \n\n @emFsub_Bot ❌ \n\n @emURLBypasser ❌ \n\n @EmoAssistant_Bot ✅ \n\n @emAFK_Bot ❌ \n\n @MRCM_Scouts_Bot ✅ \n\n @ImRishmika_Bot ✅ \n\n @Katszuki_Bot  ❌  \n\n 3 Bots Are Running.. \n 4 Bots Are Downing")




@bot.on_message(filters.command("masseges"))
async def start(_, m : Message):
    await m.reply_text("🔒Only Admin Can Use This Command")


print("Bot Stated. Check Now")
bot.run()
