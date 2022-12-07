import re
from Userbot import bot
from io import BytesIO
from requests import get
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
from os import getenv
from PIL import Image, ImageDraw, ImageFont
import random
import requests
import shutil
from config import Config

repmark = InlineKeyboardMarkup(
      [
        [
        InlineKeyboardButton(text="💡 Bot 💡", url=f"http://t.me/{Config.BOT_USERNAME}") 
        ],
        [
         InlineKeyboardButton(text="⭕ Join ⭕", url=f"https://t.me/{Config.CHANNEL}")
        ]
      ]
    )

imgcaption = f"""

**☘️ Logo Created Successfully ✅**

"""


@bot.on_message(filters.command("xlogo") & ~filters.forwarded)
async def logomake(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Please give a text.\nEx:`/logo Sithija's Assistant` ")
    else:
        pass
    m = await message.reply('Designing your logo...wait!')
    await m.edit("Logo in processing...\n░░░░░░░░░░ 0%")
    await m.edit("Logo in processing...\n▇▇░░░░░░░░ 20%")
    await m.edit("Logo in processing...\n▇▇▇▇░░░░░░ 40%")
    await m.edit("Logo in processing...\n▇▇▇▇▇▇░░░░ 60%")
    await m.edit("Logo in processing...\n▇▇▇▇▇▇▇▇░░ 80%")
    await m.edit("Logo in processing...\n▇▇▇▇▇▇▇▇▇▇ 100%")
    await m.edit("📤 Uploading...")
    text = message.text.split(None, 1)[1]
    Image_STD = Image.open("./Userbot/resources/maskbg.jpg")
    Image_font = ImageFont.truetype("./Userbot/resources/Flashing.otf", 220)
    Image_font2 = ImageFont.truetype("./Userbot/resources/Flashing.otf", 100)
    Image_text = f"."
    Image_edit = ImageDraw.Draw(Image_STD)
    image_width, image_height = Image_STD.size
    Image_edit.text((600, 600), text, (255, 255, 255), anchor="mt", font = Image_font)
    Image_STD.save("masklogo.jpg")
    await message.reply_photo(
                photo=f"masklogo.jpg",
                caption=imgcaption,
                reply_markup = repmark,
            )
    await m.delete()

@bot.on_message(filters.command("mlogo") & ~filters.forwarded)
async def logomake(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Please give a text.\nEx:`/mlogo Sithija` ")
    else:
        pass
    m = await message.reply('Designing your logo...wait!')
    await m.edit("Logo in processing...\n\n[░░░░░░░░░░] 0%")
    await m.edit("Logo in processing...\n\n[▇▇░░░░░░░░] 20%")
    await m.edit("Logo in processing...\n\n[▇▇▇▇░░░░░░] 40%")
    await m.edit("Logo in processing...\n\n[▇▇▇▇▇▇░░░░] 60%")
    await m.edit("Logo in processing...\n\n[▇▇▇▇▇▇▇▇░░] 80%")
    await m.edit("Logo in processing...\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
    await m.edit("📤 Uploading...")
    text = message.text.split(None, 1)[1]
    img = Image.open("./Userbot/resources/maskbg.jpg")
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./Userbot/resources/Flashing.otf", 400)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="yellow")
    img.save("masklogo2.jpg")
    await message.reply_photo(
                photo=f"masklogo2.jpg",
                caption=imgcaption,
                reply_markup = repmark
            )
    await m.delete()

"""
@bot.on_message(filters.command("plogo") & ~filters.forwarded)
async def logomake(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Please give a text.\nEx:`/plogo hehe` ")
    else:
        pass
    m = await message.reply('Designing your logo...wait!')
    await m.edit("Logo in processing...\n\n[░░░░░░░░░░] 0%")
    await m.edit("Logo in processing...\n\n[▇▇░░░░░░░░] 20%")
    await m.edit("Logo in processing...\n\n[▇▇▇▇░░░░░░] 40%")
    await m.edit("Logo in processing...\n\n[▇▇▇▇▇▇░░░░] 60%")
    await m.edit("Logo in processing...\n\n[▇▇▇▇▇▇▇▇░░] 80%")
    await m.edit("Logo in processing...\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
    await m.edit("📤 Uploading...")
    text = message.text.split(None, 1)[1]
    img = Image.open("./Userbot/resources/20220404_091513.jpg")
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./Userbot/resources/The Humble.ttf", 370)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=4, stroke_fill="magenta")
    img.save("plogo.jpg")
    await message.reply_photo(
                photo=f"plogo.jpg",
                caption=imgcaption,
                reply_markup = repmark
            )
    await m.delete()
"""
