import re

from pyrogram import Client, enums, types
from pyrogram.types import (
    Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
)
from plugins import Database

async def bot_handler(client: Client, msg: Message):
    if re.search(r"^[\/]bot(\s|\n)*$", msg.text):
        return await msg.reply("*Cara penggunaan command*\n\nEX : `/bot <on|off>`\nContoh : `/bot on`", quote=True, parse_mode=enums.ParseMode.MARKDOWN)

    if not (x := re.search(r"^[\/]bot\s*(on|off|<on>|<off>)$", msg.text)):
        return await msg.reply("*Cara penggunaan command*\n\nEX : `/bot <on|off>`\nContoh : `/bot on`", quote=True, parse_mode=enums.ParseMode.MARKDOWN)
    status = x[1]
    my_db = Database(msg.from_user.id)
    db_bot = my_db.get_data_bot(client.id_bot)
    if status in ['on', '<on>']:
        if db_bot.bot_status:
            return await msg.reply(
                text='ā<i>Terjadi kesalahan, bot saat ini dalam kondisi aktif</i>', quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        await my_db.bot_handler(status)
        return await msg.reply(
            text='Saat ini status bot telah <b>AKTIF</b> ā', quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    else:
        if not db_bot.bot_status:
            return await msg.reply(
                text='ā<i>Terjadi kesalahan, bot saat ini dalam kondisi tidak aktif</i>', quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        await my_db.bot_handler(status)
        return await msg.reply(
            text='Saat ini status bot telah <b>TIDAK AKTIF</b> ā', quote=True,
            parse_mode=enums.ParseMode.HTML
        )


async def setting_handler(client: Client, msg:types.Message):
    db = Database(msg.from_user.id).get_data_bot(client.id_bot)
    pesan = (
        "<b>š Menfess User\n\nā = AKTIF\nā = TIDAK AKTIF</b>\n"
        + "______________________________\n\n"
    )
    photo = ["AKTIF", "ā"] if db.kirimchannel.photo else ["TIDAK AKTIF", "ā"]
    video = ["AKTIF", "ā"] if db.kirimchannel.video else ["TIDAK AKTIF", "ā"]
    voice = ["AKTIF", "ā"] if db.kirimchannel.voice else ["TIDAK AKTIF", "ā"]
    status_bot = "AKTIF" if db.bot_status else "TIDAK AKTIF"
    pesan += f"šø Foto = <b>{photo[0]}</b>\n"
    pesan += f"š„ Video = <b>{video[0]}</b>\n"
    pesan += f"š¤ Voice = <b>{voice[0]}</b>\n\n"
    pesan += f'š°Status bot: <b> {status_bot}</b>'
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton('šø', callback_data='no'), InlineKeyboardButton(photo[1], callback_data='photo')],
        [InlineKeyboardButton('š„', callback_data='no'), InlineKeyboardButton(video[1], callback_data='video')],
        [InlineKeyboardButton('š¤', callback_data='no'), InlineKeyboardButton(voice[1], callback_data='voice')],
        [InlineKeyboardButton(status_bot, callback_data='status_bot')]
    ])
    await msg.reply(pesan, quote=True, parse_mode=enums.ParseMode.HTML, reply_markup=markup
    )

async def photo_handler_inline(client: Client, query: CallbackQuery):
    msg = query.message
    inline_keyboard = msg.reply_markup.inline_keyboard[0][1].text
    my_db = Database(msg.from_user.id)
    if inline_keyboard in ['ā', 'ā']:
        pesan = "<b>š Menfess User\n\nā = AKTIF\nā = TIDAK AKTIF</b>\n"
        pesan += "______________________________\n\n"
        if inline_keyboard == 'ā':
            await my_db.photo_handler('ā', client.id_bot)
        else:
            await my_db.photo_handler('ā', client.id_bot)

        db = my_db.get_data_bot(client.id_bot)
        photo = ["TIDAK AKTIF", "ā"] if not db.kirimchannel.photo else ["AKTIF", "ā"]
        video = ["TIDAK AKTIF", "ā"] if not db.kirimchannel.video else ["AKTIF", "ā"]
        voice = ["TIDAK AKTIF", "ā"] if not db.kirimchannel.voice else ["AKTIF", "ā"]
        status_bot = "TIDAK AKTIF" if not db.bot_status else "AKTIF"
        pesan += f"šø Foto = <b>{photo[0]}</b>\n"
        pesan += f"š„ Video = <b>{video[0]}</b>\n"
        pesan += f"š¤ Voice = <b>{voice[0]}</b>\n\n"
        pesan += f"š°Status bot: <b>{status_bot}</b>"
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('šø', callback_data='no'), InlineKeyboardButton(photo[1], callback_data='photo')],
            [InlineKeyboardButton('š„', callback_data='no'), InlineKeyboardButton(video[1], callback_data='video')],
            [InlineKeyboardButton('š¤', callback_data='no'), InlineKeyboardButton(voice[1], callback_data='voice')],
            [InlineKeyboardButton(status_bot, callback_data='status_bot')]
        ])
        await msg.edit(pesan, parse_mode=enums.ParseMode.HTML, reply_markup=markup)
    
async def video_handler_inline(client: Client, query: CallbackQuery):
    msg = query.message
    inline_keyboard = msg.reply_markup.inline_keyboard[1][1].text
    my_db = Database(msg.from_user.id)
    if inline_keyboard in ['ā', 'ā']:
        pesan = "<b>š Menfess User\n\nā = AKTIF\nā = TIDAK AKTIF</b>\n"
        pesan += "______________________________\n\n"
        if inline_keyboard == 'ā':
            await my_db.video_handler('ā', client.id_bot)
        else:
            await my_db.video_handler('ā', client.id_bot)

        db = my_db.get_data_bot(client.id_bot)
        photo = ["TIDAK AKTIF", "ā"] if not db.kirimchannel.photo else ["AKTIF", "ā"]
        video = ["TIDAK AKTIF", "ā"] if not db.kirimchannel.video else ["AKTIF", "ā"]
        voice = ["TIDAK AKTIF", "ā"] if not db.kirimchannel.voice else ["AKTIF", "ā"]
        status_bot = "TIDAK AKTIF" if not db.bot_status else "AKTIF"
        pesan += f"šø Foto = <b>{photo[0]}</b>\n"
        pesan += f"š„ Video = <b>{video[0]}</b>\n"
        pesan += f"š¤ Voice = <b>{voice[0]}</b>\n\n"
        pesan += f'š°Status bot: <b>{status_bot}</b>'
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('šø', callback_data='no'), InlineKeyboardButton(photo[1], callback_data='photo')],
            [InlineKeyboardButton('š„', callback_data='no'), InlineKeyboardButton(video[1], callback_data='video')],
            [InlineKeyboardButton('š¤', callback_data='no'), InlineKeyboardButton(voice[1], callback_data='voice')],
            [InlineKeyboardButton(status_bot, callback_data='status_bot')]
        ])
        await msg.edit(pesan, parse_mode=enums.ParseMode.HTML, reply_markup=markup)

async def voice_handler_inline(client: Client, query: CallbackQuery):
    msg = query.message
    inline_keyboard = msg.reply_markup.inline_keyboard[2][1].text
    my_db = Database(msg.from_user.id)
    if inline_keyboard in ['ā', 'ā']:
        pesan = "<b>š Menfess User\n\nā = AKTIF\nā = TIDAK AKTIF</b>\n"
        pesan += "______________________________\n\n"
        if inline_keyboard == 'ā':
            await my_db.voice_handler('ā', client.id_bot)
        else:
            await my_db.voice_handler('ā', client.id_bot)

        db = my_db.get_data_bot(client.id_bot)
        photo = ["TIDAK AKTIF", "ā"] if not db.kirimchannel.photo else ["AKTIF", "ā"]
        video = ["TIDAK AKTIF", "ā"] if not db.kirimchannel.video else ["AKTIF", "ā"]
        voice = ["TIDAK AKTIF", "ā"] if not db.kirimchannel.voice else ["AKTIF", "ā"]
        status_bot = "TIDAK AKTIF" if not db.bot_status else "AKTIF"
        pesan += f"šø Foto = <b>{photo[0]}</b>\n"
        pesan += f"š„ Video = <b>{video[0]}</b>\n"
        pesan += f"š¤ Voice = <b>{voice[0]}</b>\n\n"
        pesan += f'š°Status bot: <b>{status_bot}</b>'
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('šø', callback_data='no'), InlineKeyboardButton(photo[1], callback_data='photo')],
            [InlineKeyboardButton('š„', callback_data='no'), InlineKeyboardButton(video[1], callback_data='video')],
            [InlineKeyboardButton('š¤', callback_data='no'), InlineKeyboardButton(voice[1], callback_data='voice')],
            [InlineKeyboardButton(status_bot, callback_data='status_bot')]
        ])
        await msg.edit(pesan, parse_mode=enums.ParseMode.HTML, reply_markup=markup)

async def status_handler_inline(client: Client, query: CallbackQuery):
    msg = query.message
    inline_keyboard = msg.reply_markup.inline_keyboard[3][0].text
    my_db = Database(msg.from_user.id)
    if inline_keyboard in ['AKTIF', 'TIDAK AKTIF']:
        pesan = "<b>š Menfess User\n\nā = AKTIF\nā = TIDAK AKTIF</b>\n"
        pesan += "______________________________\n\n"
        if inline_keyboard == 'AKTIF':
            await my_db.bot_handler('off')
        else:
            await my_db.bot_handler('on')

        db = my_db.get_data_bot(client.id_bot)
        photo = ["TIDAK AKTIF", "ā"] if not db.kirimchannel.photo else ["AKTIF", "ā"]
        video = ["TIDAK AKTIF", "ā"] if not db.kirimchannel.video else ["AKTIF", "ā"]
        voice = ["TIDAK AKTIF", "ā"] if not db.kirimchannel.voice else ["AKTIF", "ā"]
        status_bot = "TIDAK AKTIF" if not db.bot_status else "AKTIF"
        pesan += f"šø Foto = <b>{photo[0]}</b>\n"
        pesan += f"š„ Video = <b>{video[0]}</b>\n"
        pesan += f"š¤ Voice = <b>{voice[0]}</b>\n\n"
        pesan += f'š°Status bot: <b>{status_bot}</b>'
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('šø', callback_data='no'), InlineKeyboardButton(photo[1], callback_data='photo')],
            [InlineKeyboardButton('š„', callback_data='no'), InlineKeyboardButton(video[1], callback_data='video')],
            [InlineKeyboardButton('š¤', callback_data='no'), InlineKeyboardButton(voice[1], callback_data='voice')],
            [InlineKeyboardButton(status_bot, callback_data='status_bot')]
        ])
        await msg.edit(pesan, parse_mode=enums.ParseMode.HTML, reply_markup=markup)