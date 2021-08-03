from pyrogram import filters
from pyrogram.types import ForceReply

from bot.screenshotbot import ScreenShotBot


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("mscht"))
)
async def _(c, m):
    await m.answer()
    dur = m.message.text.markdown.split("\n")[-1]
    await m.message.delete(True)
    await c.send_message(
        m.from_user.id,
        f"#manual_screenshot\n\n{dur}\n\nNow Send Your List Of Seconds Separated By `,`(comma).\nEg: `0,10,40,60,120`."
        "\nThis Will Generate Screenshots At 0, 10, 40, 60, And 120 Seconds. \n\n"
        "• The List Can Have A Maximum Of 10 Valid Positions\n"
        "• The Positions Has To Be Greater Than Or Equal To 0, Or Less Than The Video Length In Order To Be Valid",
        reply_to_message_id=m.message.reply_to_message.message_id,
        reply_markup=ForceReply(),
    )
