import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageTooLong
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
import lyr
import time

app = Client(
    "my_bot",
    api_id="your api id", api_hash="your api hash",
    bot_token="your bot token"
)


@app.on_message(filters.text & filters.regex('/start'))
async def welcome(client, message):
    await message.reply("Hi! Send me a song name using /lyrics prefix and i'll send the lyrics. Simple as that!")

@app.on_message(filters.text & filters.command('lyrics', '/'))
async def cock(client, message):
    try:
        await message.reply("Fetching song lyrics...")
        current_song = message.text.replace("/lyrics", "")
        print (current_song)
        current_lyrics = lyr.lyrics(current_song)
        await message.reply(current_lyrics)
        await message.reply("You must wait 15 seconds before making another request or else daddy telegram will slap my ass ):")
        time.sleep(15)
        await message.reply("You can make another request")

    except FloodWait as e:
        await asyncio.sleep(e.value)
        
    except MessageTooLong:
        await message.reply("song lyrics are too long. Thats what she said.")



app.run()

