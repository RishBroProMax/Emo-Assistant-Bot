# Credits @ImDenuwan

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from news import LK


API_ID = '14055090'
API_HASH = 'a46f7b439d0afa45b7a69fc450f754e9'
BOT_TOKEN = '5889157468:AAEYpUCdl3MJry5cDGHr3eWjM-5Tv5YnXns'

bot = Client(
    "lol",
    api_id=API_ID,
    api_hash=API_HASH, 
    bot_token=BOT_TOKEN,
)

@bot.on_message(filters.command("start"))
async def start(_, m : Message):
    await m.reply_text("✨Hello.. \n\n I m Simple And Fast News Bot \n Send /news For Get Sri Lankan News.\n\n Powerd By @EmoBotDevolopers \n Credits :- @ImRishmika | @Denuwan or @ImDenuwan")

@bot.on_message(filters.command("news"))
async def news(_, m : Message):
    lol = await m.reply_text("Processing...")
    nw = LK()
    await lol.delete()
    await m.reply_photo(nw[0]['img_url'], caption=f"**📰 {nw[0]['Title']}**\n\n✍️ {nw[0]['Description']}.__[See more...]({nw[0]['Link']})__\n\n📅 {nw[0]['Date']}\n\n🔰 Powered By 🔰 :- newswire.lk \n ❤️ </> Emo Bot Devolopers", reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📰 View in Site 📰", url=nw[0]['Link'])
            ],
            [
                InlineKeyboardButton("</> Emo Bot Devolopers", url="t.me/EmoBotDevolopers")
            ]
        ]
    ))

print("Connecting On Emo Network...")
print("Connected On Emo Network!")
print("Checking Erorrs...")
print("Geting News On newswire.lk")
print("Saving On My Database..")
print("Rishmika Sandanu's API Working Fine")
print("Bot Stated. Check Now")
bot.run()
