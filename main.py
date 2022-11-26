# Credits @ImDenuwan

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from news import LK


API_ID = '14055090'
API_HASH = 'a46f7b439d0afa45b7a69fc450f754e9'
BOT_TOKEN = '5889157468:AAEYpUCdl3MJry5cDGHr3eWjM-5Tv5YnXns'

# Start Massege

@bot.on_message(filters.command("start"))
async def start(_, m : Message):
    await m.reply_text("Hello.. \n\n I m Simple And Fast News Bot \n Send /help For Get All Commands.\n\n Powerd By @EmoBotDevolopers \n Credits :- @ImRishmika | @Denuwan or @ImDenuwan")

# Help Massege

@bot.on_message(filters.command("help"))
async def start(_, m : Message):
    await m.reply_text("🧩Commands \n\n /news - All News\n /sl - Sri Lankan News\n /masseges - Get Bot Information \n /bots - More Bots \n /about  - About Massege")

# About MAssege

@bot.on_message(filters.command("about"))
async def start(_, m : Message):
    await m.reply_text("✨ About Me \n\n 🧑‍💻Devoloper - @ImRishmika | @ImDenuwan \n\n 📡API - SD Bots Hiru News API \n\n 💻Host Sever - Raliway")

# More Bots

@bot.on_message(filters.command("bots"))
async def start(_, m : Message):
    await m.reply_text("Join @EmoBotDevolopers And Find More")


# ------------------ News Command ---------------------------

@bot.on_message(filters.command("news"))
async def news(_, m : Message):
    lol = await m.reply_text("Processing...")
    nw = LK()
    await lol.delete()
    await m.reply_photo(nw[0]['img_url'], caption=f"**📰 {nw[0]['Title']}**\n\n✍️ {nw[0]['Description']}.__[See more...]({nw[0]['Link']})__\n\n📅 {nw[0]['Date']}\n\n🔰 Powered By 🔰 :- HiruNews.lk \n ❤️ </> Emo Bot Devolopers", reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📰 View in Site 📰", url=nw[0]['Link'])
            ],
            [
                InlineKeyboardButton("</> Emo Bot Devolopers", url="t.me/EmoBotDevolopers")
            ]
        ]
    ))

# ---------------------- sl Command --------------------------

@bot.on_message(filters.command("sl"))
async def news(_, m : Message):
    lol = await m.reply_text("Getting Sri Lankan News...")
    nw = LK()
    await lol.delete()
    await m.reply_photo(nw[0]['img_url'], caption=f"**📰 {nw[0]['Title']}**\n\n✍️ {nw[0]['Description']}.__[See more...]({nw[0]['Link']})__\n\n📅 {nw[0]['Date']}\n\n🔰 Powered By ❤️ </> Emo Bot Devolopers", reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📰 View in Site 📰", url=nw[0]['Link'])
            ],
            [
                InlineKeyboardButton("</> Emo Bot Devolopers", url="t.me/EmoBotDevolopers")
            ]
        ]
    ))

# ----------------------- Masseges ------------------------

@bot.on_message(filters.command("masseges"))
async def start(_, m : Message):
    await m.reply_text("🔒Only Admin Can Use This Command")


print("Bot Stated. Check Now")
bot.run()
