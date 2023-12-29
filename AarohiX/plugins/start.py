import asyncio
import random
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch

import config
from config import BANNED_USERS, MUSIC_BOT_NAME
from AarohiX import app
from strings import get_string
from AarohiX.utils.decorators.language import LanguageStart
from config.config import OWNER_ID
from strings import get_command, get_string
from AarohiX import Telegram, YouTube, app
from AarohiX.misc import SUDOERS
from AarohiX.plugins.playlist import del_plist_msg
from AarohiX.plugins.sudoers import sudoers_list
from AarohiX.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from AarohiX.utils.decorators.language import LanguageStart
from AarohiX.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

loop = asyncio.get_running_loop()

SHALINI_PICS = [
"https://telegra.ph/file/c4896c1bc28dbda543e9a.jpg",
"https://telegra.ph/file/04ec410a5e098a31ef05c.jpg",
"https://telegra.ph/file/6d91dbc82b9985dd7f5bd.jpg", 
"https://telegra.ph/file/742122358afbdce1812aa.jpg",
"https://telegra.ph/file/9992032cde0ebdc5ce22f.jpg",
"https://telegra.ph/file/b0678a2763abd78550cb1.jpg",
"https://telegra.ph/file/08aed3ff4207ab128599c.jpg",
"https://telegra.ph/file/012b897f0dc2cf5e46dd7.jpg",
"https://telegra.ph/file/28e8a842f83ef8a936a73.jpg",
"https://telegra.ph/file/b652fb712536b64644cd0.jpg",
"https://telegra.ph/file/80fb21d13da79f45a6b3c.jpg",
"https://telegra.ph/file/ebbdac8dbe121ad724a1a.jpg",
"https://telegra.ph/file/b5baf462b6afbfe11cfd8.jpg",
"https://telegra.ph/file/2a2c5d6e11611635813c8.jpg",
"https://telegra.ph/file/2952e480c6748f481acec.jpg",
"https://telegra.ph/file/4c9c874eb27f47d1744ee.jpg",
"https://telegra.ph/file/71b4c5143532982fbf326.jpg",
"https://telegra.ph/file/0e7864982ddd768c0e268.jpg",
"https://telegra.ph/file/3dbbf7c02a601864333ff.jpg",
"https://telegra.ph/file/21b828d6f52395fee7347.jpg",
"https://telegra.ph/file/b1b4860b4bcc63ea06020.jpg",
"https://telegra.ph/file/efe8d6d5e451eaf2c823b.jpg",
"https://telegra.ph/file/6915fa51b93f102d728d1.jpg",
"https://telegra.ph/file/aac96626fff9e97719d99.jpg",
"https://telegra.ph/file/d9f451277fc14ab8fb046.jpg",
"https://telegra.ph/file/af76e0e0369877ff9ee96.jpg",
"https://telegra.ph/file/a62f55e1ee715c5fda49e.jpg",
"https://telegra.ph/file/e63fad358a31971d0226e.jpg",
"https://telegra.ph/file/d329dab2265ee38e8596c.jpg",
"https://telegra.ph/file/8e409dd00351e52c0b832.jpg",
"https://telegra.ph/file/d81edcb736dd1eb3e3f28.jpg",
"https://telegra.ph/file/c1e9ea3472d2e88e2cd9e.jpg",
"https://telegra.ph/file/fce7a6531e493d3f170d2.jpg",
"https://telegra.ph/file/dac47da8d3c34944d905e.jpg",
"https://telegra.ph/file/3db89104698f8c59c9f2f.jpg",
"https://telegra.ph/file/3ab1242f4c692cee890b3.jpg",
"https://telegra.ph/file/989a133f1a1fa91eef931.jpg",
"https://telegra.ph/file/2c14b613bfb4e21ddf66b.jpg",
"https://telegra.ph/file/67e09a6b45f9210db54a7.jpg",
"https://telegra.ph/file/d36acf08120d275c76555.jpg",
"https://telegra.ph/file/3f69614121059aba0aa53.jpg",
"https://telegra.ph/file/a884b01bfd9749edf1e44.jpg",
"https://telegra.ph/file/6c1b34786d6aa1427aa34.jpg"
"https://telegra.ph/file/6255f3e1a0d1935d81686.jpg",
"https://telegra.ph/file/63f82e98e24c5a9c2dc2c.jpg",
"https://telegra.ph/file/8aa6c354fc55c8aa40e1e.jpg",
"https://telegra.ph/file/40c70455f620b8a1c5f2b.jpg",
"https://telegra.ph/file/638e6c6e615f75683c97e.jpg"
"https://telegra.ph/file/c49862ca13d5f96e1055f.jpg",
"https://telegra.ph/file/1538811747a6c3c26d0c7.jpg",
"https://telegra.ph/file/5dc97f410e8886477f45c.jpg",
"https://telegra.ph/file/df6d158f8cd3a82d1aa81.jpg",
"https://telegra.ph/file/78ab7d6fcae20817167bb.jpg",
"https://telegra.ph/file/6a33f6c47069cdcb6699b.jpg",
"https://telegra.ph/file/3b415bcf9ef3f3c5f71c1.jpg",
"https://telegra.ph/file/fc150e19584ceb9532b84.jpg",
"https://telegra.ph/file/52b4f1556b87806118651.jpg",
"https://telegra.ph/file/31f7ce3848156e77521f7.jpg",
"https://telegra.ph/file/dc3210c66a61143fe134d.jpg",
"https://telegra.ph/file/2102f3b08150b2355fa55.jpg",
"https://telegra.ph/file/3d3d19956d3f62717b7b3.jpg",
"https://telegra.ph/file/282229aa4ad14450f19f4.jpg",
"https://telegra.ph/file/c3e4a11ddc59c29c896b5.jpg",
"https://telegra.ph/file/f2ecb3cc334cb184ceb0a.jpg"
]

@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            await message.reply_sticker("CAACAgUAAxkBAAELEPVljxNb43qQnQ-Qijz9zJqCNAABpCsAAmoOAALtUdlXavPd0orPxhk0BA")
            return await message.reply_photo(
                       random.choice(SHALINI_PICS),
                       caption=_["help_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard
            )
        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])
        if name[0:3] == "sta":
            m = await message.reply_text(
                f"🥱 ɢᴇᴛᴛɪɴɢ ʏᴏᴜʀ ᴩᴇʀsᴏɴᴀʟ sᴛᴀᴛs ғʀᴏᴍ {config.MUSIC_BOT_NAME} sᴇʀᴠᴇʀ."
            )
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"🔗[ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ](https://t.me/MUSIC_WORLD_SH) ** ᴩʟᴀʏᴇᴅ {count} ᴛɪᴍᴇs**\n\n"
                    else:
                        msg += f"🔗 [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(
                    None, get_stats
                )
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <code>sᴜᴅᴏʟɪsᴛ</code>\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀɴᴀᴍᴇ:** {sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                return await Telegram.send_split_text(message, lyrics)
            else:
                return await message.reply_text(
                    "ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇᴛ ʟʏʀɪᴄs."
                )
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name[0:3] == "inf":
            m = await message.reply_text("💖")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[
                    0
                ]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
✨**🍃ᴛʀᴀᴄᴋ ɪɴғᴏʀɴᴀᴛɪᴏɴ ᴏғ ʜᴇᴀᴠᴇɴ🍃**✨

❤‍🔥 **ᴛɪᴛʟᴇ:** {title}

⏳ **ᴅᴜʀᴀᴛɪᴏɴ:** {duration} ᴍɪɴᴜᴛᴇs
👀 **ᴠɪᴇᴡs:** `{views}`
❣️ **ᴩᴜʙʟɪsʜᴇᴅ ᴏɴ:** {published}
🎥 **ᴄʜᴀɴɴᴇʟ:** {channel}
📎 **ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ:** [ᴠɪsɪᴛ ᴄʜᴀɴɴᴇʟ]({channellink})
🔗 **ʟɪɴᴋ:** [ᴡᴀᴛᴄʜ ᴏɴ ʏᴏᴜᴛᴜʙᴇ]({link})


|| ᴍᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ [ᴅɪʟ❣️](https://t.me/Honey_Singh_121) 🥀 ||

ᴀɪᴍ[💖] sᴇᴀʀᴄʜ ᴩᴏᴡᴇʀᴇᴅ ʙʏ {config.MUSIC_BOT_NAME}"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🍃•ʏᴏᴜᴛᴜʙᴇ•🍃", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="🍁•sᴜᴩᴩᴏʀᴛ[ᴅɪʟ❣️]🍁•", url="https://t.me/LOVE_FEELINGS_WILL"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <code>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</code>\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀɴᴀᴍᴇ:** {sender_name}",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        out = private_panel(_, app.username, OWNER)
        if config.START_IMG_URL:
            try:
                await message.reply_sticker("CAACAgUAAxkBAAELEPVljxNb43qQnQ-Qijz9zJqCNAABpCsAAmoOAALtUdlXavPd0orPxhk0BA")
                await message.reply_photo(
                    random.choice(SHALINI_PICS),
                    caption=_["start_2"].format(
                        config.MUSIC_BOT_NAME
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            except:
                await message.reply_text(
                    _["start_2"].format(config.MUSIC_BOT_NAME),
                    reply_markup=InlineKeyboardMarkup(out),
                )
        else:
            await message.reply_text(
                _["start_2"].format(config.MUSIC_BOT_NAME),
                reply_markup=InlineKeyboardMarkup(out),
            )
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ.\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀɴᴀᴍᴇ:** {sender_name}",
            )


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def testbot(client, message: Message, _):
    OWNER = OWNER_ID[0]
    out = start_pannel(_, app.username, OWNER)
    return await message.reply_photo(
               random.choice(SHALINI_PICS),
               caption=_["start_1"].format(
            message.chat.title, config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )


welcome_group = 2


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**ᴩʀɪᴠᴀᴛᴇ ᴍᴜsɪᴄ ʙᴏᴛ**\n\nᴏɴʟʏ ғᴏʀ ᴛʜᴇ ᴄʜᴀᴛs ᴀᴜᴛʜᴏʀɪsᴇᴅ ʙʏ ᴍʏ ᴏᴡɴᴇʀ, ʀᴇǫᴜᴇsᴛ ɪɴ ᴍʏ ᴏᴡɴᴇʀ's ᴩᴍ ᴛᴏ ᴀᴜᴛʜᴏʀɪsᴇ ʏᴏᴜʀ ᴄʜᴀᴛ ᴀɴᴅ ɪғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴡᴀɴᴛ ᴛᴏ ᴅᴏ sᴏ ᴛʜᴇɴ ғᴜ*ᴋ ᴏғғ ʙᴇᴄᴀᴜsᴇ ɪ'ᴍ ʟᴇᴀᴠɪɴɢ."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != "supergroup":
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                OWNER = OWNER_ID[0]
                out = start_pannel(_, app.username, OWNER)
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            return
        except:
            return
