import os
from pyrogram import Client, filters

bot = Client(
    "BotNameHere",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


@bot.on_message(filters.forwarded)
async def forward(bot, message):
await message.delete()


bot.run()
