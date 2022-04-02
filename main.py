import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
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

@Bot.on_message(filters.private & filters.command(["love"]))
async def start(bot, update):
    await update.reply_sticker("CAACAgIAAxkBAAEIg3FiSJawE8qB_DosotXRQLGRQIzi_QAC8SQAAnQfywgLksg2NlGEmCME")
    await update.reply_text(
        f""" Hai {update.from_user.mention} am just a pyrogram example bot""", 
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )

@Bot.on_message(filters.command(["repo", "repo@Pyro_Tg_Bot"]) & filters.private)
async def repo(bot, update):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

Kk Click On The Below Button For The Repo :)

Made by **@Amalbiju154** for Noob/Beginners Like Him!

Join **@NexaBotsUpdates**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Repo", url="www.google.com"
                    )
                ]
            ]
        )
    )


Bot.run()
