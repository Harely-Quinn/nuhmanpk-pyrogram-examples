import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.types import *

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
async def start(bot, update):
    await update.reply_text(
        f"""<b>Hi 😉️!</b>

Kk Click On The Below Button For The Repo :)

Made by **@Amalbiju154** for Noob/Beginners Like Him!

Join **@NexaBotsUpdates**""",
 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Repo", url="www.google.com"
  )]])
)


START_TEXT = """Hello {},
I am a simple calculator telegram bot. Send me /calculator.

Made by @FayasNoushad"""
START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/FayasNoushad')
        ]
    ]
)
CALCULATE_TEXT = "Made by @FayasNoushad"
CALCULATE_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("DEL", callback_data="DEL"),
            InlineKeyboardButton("AC", callback_data="AC"),
            InlineKeyboardButton("(", callback_data="("),
            InlineKeyboardButton(")", callback_data=")")
        ],
        [
            InlineKeyboardButton("7", callback_data="7"),
            InlineKeyboardButton("8", callback_data="8"),
            InlineKeyboardButton("9", callback_data="9"),
            InlineKeyboardButton("÷", callback_data="/")
        ],
        [
            InlineKeyboardButton("4", callback_data="4"),
            InlineKeyboardButton("5", callback_data="5"),
            InlineKeyboardButton("6", callback_data="6"),
            InlineKeyboardButton("×", callback_data="*")
        ],
        [
            InlineKeyboardButton("1", callback_data="1"),
            InlineKeyboardButton("2", callback_data="2"),
            InlineKeyboardButton("3", callback_data="3"),
            InlineKeyboardButton("-", callback_data="-"),
        ],
        [
            InlineKeyboardButton(".", callback_data="."),
            InlineKeyboardButton("0", callback_data="0"),
            InlineKeyboardButton("=", callback_data="="),
            InlineKeyboardButton("+", callback_data="+"),
        ]
    ]
)


@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["calc", "calculate", "calculator"]))
async def calculate(bot, update):
    await update.reply_text(
        text=CALCULATE_TEXT,
        reply_markup=CALCULATE_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_callback_query()
async def cb_data(bot, update):
        data = update.data
        try:
            message_text = update.message.text.split("\n")[0].strip().split("=")[0].strip()
            message_text = '' if CALCULATE_TEXT in message_text else message_text
            if data == "=":
                text = float(eval(message_text))
            elif data == "DEL":
                text = message_text[:-1]
            elif data == "AC":
                text = ""
            else:
                text = message_text + data
            await update.message.edit_text(
                text=f"{text}\n\n{CALCULATE_TEXT}",
                disable_web_page_preview=True,
                reply_markup=CALCULATE_BUTTONS
            )
        except Exception as error:
            print(error)


@Bot.on_inline_query()
async def inline(bot, update):
    if len(update.data) == 0:
        try:
            answers = [
                InlineQueryResultArticle(
                    title="Calculator",
                    description=f"New calculator",
                    input_message_content=InputTextMessageContent(
                        text=CALCULATE_TEXT,
                        disable_web_page_preview=True
                    ),
                    reply_markup=CALCULATE_BUTTONS
                )
            ]
        except Exception as error:
            print(error)
    else:
        try:
            message_text = update.message.text.split("\n")[0].strip().split("=")[0].strip()
            data = message_text.replace("×", "*").replace("÷", "/")
            text = float(eval(data))
            answers = [
                InlineQueryResultArticle(
                    title="Answer",
                    description=f"Results of your input",
                    input_message_content=InputTextMessageContent(
                        text=f"{data} = {text}",
                        disable_web_page_preview=True
                    )
                )
            ]
        except:
            pass
    await update.answer(answers)

Bot.run()
