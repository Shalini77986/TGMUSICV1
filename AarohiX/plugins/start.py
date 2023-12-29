import random
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import BANNED_USERS, MUSIC_BOT_NAME
from AarohiX import app
from strings import get_string
from AarohiX.utils.decorators.language import LanguageStart

YUMI_PICS = [
    "https://telegra.ph/file/6c885935e50762da25472.jpg",
    "https://telegra.ph/file/bf8ea432e132ec30cb0c2.jpg",
    "https://telegra.ph/file/30250b09029076698e4b2.jpg",
    "https://telegra.ph/file/bce5cfde2ed72fe655e69.jpg",
    "https://telegra.ph/file/92f3de73c8a0c541dd672.jpg",
    "https://telegra.ph/file/7145ff6c8877f27bf64ca.jpg",
    "https://telegra.ph/file/d82e218980ec409672c68.jpg",
    "https://telegra.ph/file/43693df3a30172b954632.jpg",
    "https://telegra.ph/file/30b92f86ea0a712f4d0ed.jpg",
    "https://telegra.ph/file/8cc5b6fe5a047a1ce1cbd.jpg",
    "https://telegra.ph/file/e2c2fb24469b1b19a0866.jpg",
    "https://telegra.ph/file/46b596a04f9db8041a9d1.jpg",
    "https://telegra.ph/file/549ad9de7da164636e201.jpg",
    "https://telegra.ph/file/2eb793749061146a6037c.jpg",
    "https://telegra.ph/file/7ce0ef5e9216273b8bc27.jpg",
    "https://telegra.ph/file/66a8e54145c27468f0c69.jpg",
    "https://telegra.ph/file/da416ecfcc3e50973172e.jpg",
    "https://telegra.ph/file/0708854fe104da9e1445e.jpg",
    "https://telegra.ph/file/48aa2e6b48a32efaf7017.jpg",
    "https://telegra.ph/file/920b88f2d2b0ccb4e648c.jpg",
    "https://telegra.ph/file/fda8146fd6b22f9637733.jpg",
    "https://telegra.ph/file/5417d79b1eea8d122008f.jpg",
    "https://telegra.ph/file/a43806329815ecc6c2aa3.jpg",
    "https://telegra.ph/file/7c4bf50287cc170d167c4.jpg"
]

@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS & ~filters.edited)
@LanguageStart
async def str(client, message: Message, _):
    await message.reply_photo(
        random.choice(YUMI_PICS),
        caption=_["start_2"].format(MUSIC_BOT_NAME),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★ Add Me ★", url=f"https://t.me/Shalinixmusicbot?startgroup=true")
                ],
                [
                     InlineKeyboardButton(
                        "ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper")
                ],
                [
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/ShaliniMusicBotSh"),
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/music_world_sh"),
                ],    
                [
                     InlineKeyboardButton(
                      "💞ᴍᴀɪɴᴛᴀɪɴᴇʀ💞", url=f"https://t.me/shalini_shalu_69")
                ]
            ]
        )
)
