from pyrogram import filters

from bot.screenshotbot import ScreenShotBot
from bot.database import Database


db = Database()


@ScreenShotBot.on_message(filters.private & filters.command("set_watermark"))
async def _(c, m):

    if len(m.command) == 1:
        await m.reply_text(
            text="Send Text Along With Watermark.\n Example : /set_watermark Hi "
            "NOTE :- Text Should Not Exceed 30 Characters",
            quote=True,
            parse_mode="markdown",
        )
        return

    watermark_text = " ".join(m.command[1:])
    if len(watermark_text) > 30:
        await m.reply_text(
            text=f"The watermark Text You Provided (__{watermark_text}__) Is `{len(watermark_text)}` "
            "Characters Long You cannot Set Watermark Text Greater Than 30 Characters",
            quote=True,
            parse_mode="markdown",
        )
        return

    await db.update_watermark_text(m.chat.id, watermark_text)
    await m.reply_text(
        text=f"You Have successfully Set __{watermark_text}__ As Your Watermark Text"
        "Use /settings To Change It",
        quote=True,
        parse_mode="markdown",
    )
