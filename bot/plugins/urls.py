import datetime

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..utils import Utilities
from ..screenshotbot import ScreenShotBot
from ..config import Config


@ScreenShotBot.on_message(
    filters.private
    & ((filters.text & ~filters.edited) | filters.media)
    & filters.incoming
)
async def _(c, m):

    if m.media:
        if not Utilities.is_valid_file(m):
            return
    else:
        if not Utilities.is_url(m.text):
            return

    snt = await m.reply_text(
        "**Please Wait...⏳**",
        quote=True,
    )

    if m.media:
        await snt.delete()
        file_link = await Utilities.generate_stream_link(m)
        snt = await m.reply_text(
            "**Processing...⏳**",
            quote=True,
        ) 
    else:
        file_link = m.text

    duration = await Utilities.get_duration(file_link)
    if isinstance(duration, str):
        await snt.edit_text("I Can't Open The File")
        log = await m.forward(Config.LOG_CHANNEL)
        await log.reply_text(duration, True)
        return

    btns = Utilities.gen_ik_buttons()

    if duration >= 600:
        btns.append([InlineKeyboardButton("Generate Sample Video", "smpl")])

    await snt.edit_text(
        text=f"__Select Your Desired Option .__\n\n**Total Duration :** `{datetime.timedelta(seconds=duration)}` (`{duration}s`)",
        reply_markup=InlineKeyboardMarkup(btns),
    )
