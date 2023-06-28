#(©)hdmaxx

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>ᴅᴇᴠᴇʟᴏᴘᴇʀ:- <a href='tg://user?id={OWNER_ID}'>ꜱᴛᴀʀ ʙᴏʏ</a>\nʟᴀɴɢᴜᴀɢᴇ:- <code>ᴘʏᴛʜᴏɴ 3</code>\nʟɪʙʀᴀʀʏ:-<a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\nᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ:- <a href='https://t.me/hdmaxx'>ʜᴅᴍᴀxx</a>\nʀᴇǫᴜᴇꜱᴛ ɢʀᴏᴜᴘ :- <a href='https://t.me/hd_request'>ʜᴅ ʀᴇǫᴜᴇꜱᴛ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
