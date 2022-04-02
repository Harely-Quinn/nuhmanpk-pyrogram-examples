import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

Bot = Client(
    "Pyrogram-example-bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_BUTTON = InlineKeyboardMarkup(
        [[
      InlineKeyboardButton("Souce", url="https://github.com/vivek-tp/Tg-Bot"),
      InlineKeyboardButton("Support", url="https://t.me/OpensourceTG")
        ]]
    ) 
@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_sticker("CAACAgIAAxkBAAEIg21iSJYE6EDjPiUHyGjsbyVP4PQNBwAC6gcAAkb7rASUHp5Nfp3HaCME")
    await update.reply_text(
        f""" Hai {update.from_user.mention} am just a pyrogram example bot""", 
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    
    )

Bot.run()
