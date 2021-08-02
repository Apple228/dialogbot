from aiogram.types import CallbackQuery

from keyboards.inline.answer_men import answer_men_1, answer_men_2, answer_men_3_4, answer_men_5, \
    answer_men_6_7_8_voice, answer_men_9_voice, answer_men_10_voice, answer_men_11_voice, answer_men_12_voice
from loader import dp, db


@dp.callback_query_handler(text="man")
async def answer_men(call: CallbackQuery):
    await db.update_user_sex(sex="Мужской", telegram_id=call.from_user.id)
    await call.message.answer(text="Привет! Меня зовут Аня. Кажется сегодня мне повезло :)", reply_markup=answer_men_1)

@dp.callback_query_handler(text="answer_men_1")
async def answer_men(call: CallbackQuery):
    await call.message.answer(text=" Ну конечно! Наше с тобой знакомство! Разве это не удача?", reply_markup=answer_men_2)


@dp.callback_query_handler(text="answer_men_2")
async def answer_men(call: CallbackQuery):
    await dp.bot.send_voice(call.from_user.id, "AwACAgIAAxkBAAIEuGEHt9pYzwlgiY5sh4_KfsbIS6vrAAL_EQACLjT5SyB1Xy9nwDFMIAQ",
                      reply_markup=answer_men_3_4)   #Male_01.ogg

@dp.callback_query_handler(text="answer_men_3")
async def answer_men(call: CallbackQuery):
    await dp.bot.send_voice(call.from_user.id, "AwACAgIAAxkBAAIEjmEHmXmZdK1DhgJa5zfjrb-cKZQrAAIVDgACBSBASIHouXa9GNSxIAQ",
                      reply_markup=answer_men_5)   #Male_02 .ogg


@dp.callback_query_handler(text="answer_men_4")
async def answer_men(call: CallbackQuery):
    await call.message.answer(text=" Хорошо, давай текстом. Хотя мне кажется, что голосовые более живые и искренние.")
    await call.message.answer(text=" Итак, факты обо мне :"
                                   "– Я жил в Париже и Лондоне."
                                   "– Прыгал с парашютом."
                                   " – Прыгал с парашютом."
                                   "Один из них неправда, как думаешь какой?", reply_markup=answer_men_5)


@dp.callback_query_handler(text="answer_men_5_voice")
async def answer_men(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=answer_men_6_7_8_voice)

@dp.callback_query_handler(text="answer_men_6_voice")
async def answer_men(call: CallbackQuery):
    await dp.bot.send_voice(call.from_user.id,
                            "AwACAgIAAxkBAAIEj2EHnJcn_M0q_7lcwqM5Volxx0wGAAIdDgACBSBASLY8U0PPq2U4IAQ",
                            reply_markup=answer_men_9_voice)  # Male_03.ogg


@dp.callback_query_handler(text="answer_men_7_voice")
async def answer_men(call: CallbackQuery):
    await dp.bot.send_voice(call.from_user.id,
                            "AwACAgIAAxkBAAIElWEHoWp8_ku08g3Dp-kBOUwTp6F9AAI8DgACBSBASD672ZJmQiqOIAQ",
                            reply_markup=answer_men_10_voice)  # Male_04.ogg

@dp.callback_query_handler(text="answer_men_10_voice")
async def answer_men(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=answer_men_11_voice)


@dp.callback_query_handler(text="answer_men_8_voice")
async def answer_men(call: CallbackQuery):
    await dp.bot.send_voice(call.from_user.id,
                            "AwACAgIAAxkBAAIEmGEHojz4YjFRWzudO4Ybz5uiZSh6AAI_DgACBSBASLZd1LH9pvz2IAQ",
                            reply_markup=answer_men_12_voice)  # Male_05.ogg



