import os
import pyrogram
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import Message, User 

Bot = Client(
    "Instant-Caption-Adder",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

CAPTION = os.environ.get("CAPTION", None)

# Better to add caption through config vars / app.json


@Bot.on_message(filters.media)
async def caption(bot, message):
    chat_id = message.chat.id
    if CAPTION:
        caption = CAPTION
    else:
        caption = await get_caption(bot, message)
        if caption is True:
            return
        await message.copy(chat_id=chat_id, caption=caption, reply_to_message_id=message.message_id)


async def get_caption(bot, message):
    caption = await bot.ask(message.chat.id, "Send a caption for the media or send /cancel for cancelling this process")
    if not caption.text:
        await caption.reply("No caption found", quote=True)
        return await get_caption(bot, message)
    if caption.text.startswith("/cancel"):
        await caption.reply("Process cancelled", quote=True)
        return True
    else:
        return caption.text

@Bot.on_message(filters.regex("http") | filters.regex("www") | filters.regex("t.me"))
async def nolink(bot,message):
	try:
		await message.delete()
	except:
		return


@Bot.on_message(filters.command(["ban"]))
async def ban(bot, message):
    chatid = message.chat.id
    if message.reply_to_message:
        admins_list = await bot.get_chat_members(
            chat_id=chatid, filter="administrators"
        )
        admins = []
        for admin in admins_list:
            id = admin.user.id
            admins.append(id)
        userid = message.from_user.id
        if userid in admins:
            user_to_ban = message.reply_to_message.from_user.id
            if user_to_ban in admins:
                await message.reply(text="Think he is Admin, Can't Ban Admins")
            else:
                try:
                    await bot.kick_chat_member(chat_id=chatid, user_id=user_to_ban)
                    await message.reply_text(
                        f"Bye {message.reply_to_message.from_user.mention}"
                    )
                except Exception as error:
                    await message.reply_text(f"{error}")
        else:
            await message.reply_text("Nice try, But wrong move..")
            return
    else:
        return


Bot.run()


