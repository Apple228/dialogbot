from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.default.answer_for_man import answer_men_1, answer_men_2, answer_men_3_4, answer_men_5_6_7_voice, \
    answer_men_6_voice, answer_men_7_voice, answer_men_8_voice, answer_men_9_voice, answer_men_10_voice, \
    answer_men_11_voice, answer_men_12_voice, answer_men_13_voice, answer_men_14_15_voice, answer_men_5_6_7, \
    answer_men_6, answer_men_7, answer_men_8, answer_men_10_11, answer_men_9, answer_men_12_13, answer_men_14, \
    answer_men_15, answer_men_16, answer_men_17
from keyboards.default.final import final

from loader import dp, db, sa


@dp.callback_query_handler(text="man")
async def answer_men(call: CallbackQuery):
    await db.update_user_sex(sex="Мужской", telegram_id=call.from_user.id)
    await call.message.answer(text="Привет! Меня зовут Аня. Кажется сегодня мне повезло :)", reply_markup=answer_men_1)
    await sa.add_line(username=call.from_user.username,
                      from_bot="Привет! Меня зовут Аня. Кажется сегодня мне повезло :)",
                      from_user="Парень")


@dp.message_handler(text="Привет:) Случилось что-то хорошее?")
async def answer_men(message: types.Message):
    await message.answer(text="Ну конечно! Наше с тобой знакомство! Разве это не удача?", reply_markup=answer_men_2)
    await sa.add_line(username=message.from_user.username,
                      from_bot="Ну конечно! Наше с тобой знакомство! Разве это не удача?",
                      from_user="Привет:) Случилось что-то хорошее?")


@dp.message_handler(text="Возможно:) тогда расскажи мне о себе?")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIFwWEKRloS9oTh3ovU8A79eCIaXjbFAAL_EQACLjT5SyB1Xy9nwDFMIAQ",
                            reply_markup=answer_men_3_4)  # female_01
    await sa.add_line(username=message.from_user.username, from_bot="female_01",
                from_user="Возможно:) тогда расскажи мне о себе?")


@dp.message_handler(text="У тебя очень приятный голос :)")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIFw2EKRnsPH5EYzNe0F8cuWUrEZe6uAAIBEgACLjT5S4WGOVfffUESIAQ",
                            reply_markup=answer_men_5_6_7_voice)  # female_02
    await sa.add_line(username=message.from_user.username,
                      from_user="У тебя очень приятный голос :)",
                      from_bot = "female_02")


@dp.message_handler(text="Жила в Париже и Лондоне")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIFxWEKRreB1cqctnXkfte7AoLs6Z2rAAICEgACLjT5S4LqXX7_mqjfIAQ",  # female_03
                            reply_markup=answer_men_6_voice)
    await sa.add_line(username=message.from_user.username,
                      from_user="Жила в Париже и Лондоне" ,
                      from_bot = "female_03")


@dp.message_handler(text="Прыгала с парашютом")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIFx2EKRtv52TGqISDQncauwJH5SIKmAAIFEgACLjT5S5Rdjbs7OC7DIAQ",  # female_04
                            reply_markup=answer_men_7_voice)
    await sa.add_line(username=message.from_user.username,
                      from_user="Прыгала с парашютом",
                      from_bot="female_04")



@dp.message_handler(text="Ни разу не была в кино за последние 5 лет")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIFyWEKR20HBeCAhWDoWGGREyZ5UEqFAAIGEgACLjT5SxQMSW5NVf2YIAQ",  # female_05
                            reply_markup=answer_men_8_voice)

    await sa.add_line(username=message.from_user.username,
                      from_user="Ни разу не была в кино за последние 5 лет",
                      from_bot="female_05")



@dp.message_handler(text="Я подумаю :) Но что там с фактами, Париж?")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF0mEKR56qxyfL5jfmd3SEoRmu9E-vAAIHEgACLjT5S54Fxrlqf84DIAQ",  # female_06

                            reply_markup=answer_men_9_voice)

    await sa.add_line(username=message.from_user.username,
                      from_user="Я подумаю :) Но что там с фактами, Париж?",
                      from_bot="female_06")



@dp.message_handler(text="Ого, очень круто! Расскажи мне про Париж?")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF2GEKSSaXileJopm1grZTBUYUw5xcAAIIEgACLjT5SwRlUZh_7V-tIAQ")  # female_07
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF2mEKST81pTbtTL16FuLS_iS1RwQ0AAIKEgACLjT5S43nsKBxsKHOIAQ",  # female_08
                            reply_markup=answer_men_10_voice)

    await sa.add_line(username=message.from_user.username,
                      from_user="Ого, очень круто! Расскажи мне про Париж?",
                      from_bot="female_07 female_08")



@dp.message_handler(text="Наоборот! Расскажешь мне про Париж?")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF2GEKSSaXileJopm1grZTBUYUw5xcAAIIEgACLjT5SwRlUZh_7V-tIAQ")  # female_07
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF2mEKST81pTbtTL16FuLS_iS1RwQ0AAIKEgACLjT5S43nsKBxsKHOIAQ",  # female_08
                            reply_markup=answer_men_10_voice)

    await sa.add_line(username=message.from_user.username,
                      from_user="Наоборот! Расскажешь мне про Париж?",
                      from_bot="female_07 female_08")



@dp.message_handler(text="Ого, неожиданно! Расскажешь?")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF2GEKSSaXileJopm1grZTBUYUw5xcAAIIEgACLjT5SwRlUZh_7V-tIAQ")  # female_07
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF2mEKST81pTbtTL16FuLS_iS1RwQ0AAIKEgACLjT5S43nsKBxsKHOIAQ",  # female_08
                            reply_markup=answer_men_10_voice)

    await sa.add_line(username=message.from_user.username,
                      from_user="Ого, неожиданно! Расскажешь?",
                      from_bot="female_07 female_08")



@dp.message_handler(text="Кажется, ты была не очень занята учебой:)")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF3GEKSZJ09-_1gqqrxUeTGXlzjF0SAAINEgACLjT5SxGk843mcYsPIAQ",
                            reply_markup=answer_men_11_voice)  # female_09
    await sa.add_line(username=message.from_user.username,
                      from_user="Кажется, ты была не очень занята учебой:)",
                      from_bot="female_09")


@dp.message_handler(text="Что именно ты изучала?")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF3mEKSak4Bq9grL3aG_fAfqunqnxBAAIPEgACLjT5S9Bv8x_0uRMsIAQ",
                            reply_markup=answer_men_12_voice)  # female_10

    await sa.add_line(username=message.from_user.username,
                      from_user="Что именно ты изучала?",
                      from_bot="female_10")



@dp.message_handler(text="А теперь ты вернулась в Россию? Почему?")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF4GEKScv_ZbGhEmJxKSK-_MfFfF46AAIREgACLjT5S7i8XzDiG5YgIAQ")
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF4mEKSfwRAkUQKodjDFi5aVEsPRlqAAISEgACLjT5S7sAAdRbSaGTGyAE",
                            reply_markup=answer_men_13_voice)  # female_12

    await sa.add_line(username=message.from_user.username,
                      from_user="А теперь ты вернулась в Россию? Почему?",
                      from_bot="female_11 female_12")



@dp.message_handler(text="Мне бы хотелось больше путешествовать")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF5GEKShW4uYe4QGru48zd5xBo1VFMAAITEgACLjT5SwqkFRIZRiY-IAQ")
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF5mEKSiFqIq0xaQh4utY7wcT7VzlOAAIUEgACLjT5S4f785I0LKKFIAQ",
                            reply_markup=answer_men_14_15_voice)  # female_14

    await sa.add_line(username=message.from_user.username,
                      from_user="Мне бы хотелось больше путешествовать",
                      from_bot="female_13 female_14")



@dp.message_handler(text="Не удобно сейчас слушать, давай текстом?")
async def answer_men(message: types.Message):
    await message.answer(text="Хорошо, давай текстом. Хотя мне кажется, что голосовые более живые и искренние.")
    await message.answer(text=" Итак, факты обо мне : \n"
                              " – Я жила в Париже и Лондоне. \n"
                              " – Прыгала с парашютом. \n"
                              " – Ни разу не была в кино за последние 5 лет. \n"
                              " Один из них неправда, как думаешь какой?", reply_markup=answer_men_5_6_7)
    await sa.add_line(username=message.from_user.username,
                      from_user="Не удобно сейчас слушать, давай текстом?",
                      from_bot=" Итак, факты обо мне :  – Я жила в Париже и Лондоне.   – Прыгала с парашютом.   – Ни разу не была в кино за последние 5 лет. Один из них неправда, как думаешь какой?")


@dp.message_handler(text="Жила в Париже и Лондоне.")
async def answer_men(message: types.Message):
    await message.answer(text="Нет, Париж - правда, Лондон тоже. Жила там несколько лет во время учебы.",
                         reply_markup=answer_men_6)
    await sa.add_line(username=message.from_user.username,
                      from_user="Жила в Париже и Лондоне.",
                      from_bot="Нет, Париж - правда, Лондон тоже. Жила там несколько лет во время учебы.")



@dp.message_handler(text="Прыгала с парашютом.")
async def answer_men(message: types.Message):
    await message.answer(text="Хаха, а ты молодец! Неужели это так легко угадать?",
                         reply_markup=answer_men_7)
    await sa.add_line(username=message.from_user.username,
                      from_user="Прыгала с парашютом.",
                      from_bot="Хаха, а ты молодец! Неужели это так легко угадать?")



@dp.message_handler(text="Ни разу не была в кино за последние 5 лет.")
async def answer_men(message: types.Message):
    await message.answer(
        text="Нет, это чистая правда! Очень люблю кино, но как-то все время не до этого. Может исправим это как-нибудь?)",
        reply_markup=answer_men_8)
    await sa.add_line(username=message.from_user.username,
                      from_user="Ни разу не была в кино за последние 5 лет.",
                      from_bot="Нет, это чистая правда! Очень люблю кино, но как-то все время не до этого. Может исправим это как-нибудь?)")


@dp.message_handler(text="Я подумаю :) Но что там с фактами, Париж?")
async def answer_men(message: types.Message):
    await message.answer(text="Нет, я не прыгала с парашютом, а в Париже действительно жила.",
                         reply_markup=answer_men_9)
    await sa.add_line(username=message.from_user.username,
                      from_user="Я подумаю :) Но что там с фактами, Париж?",
                      from_bot="Нет, я не прыгала с парашютом, а в Париже действительно жила.")



@dp.message_handler(text="Ого, очень круто!  Расскажи мне про Париж?")
async def answer_men(message: types.Message):
    await message.answer(text="Ты уверен, что против голосовых? Это довольно долгий рассказ :)",
                         reply_markup=answer_men_10_11)
    await sa.add_line(username=message.from_user.username,
                      from_user="Ого, очень круто!  Расскажи мне про Париж?",
                      from_bot="Ты уверен, что против голосовых? Это довольно долгий рассказ :)")


@dp.message_handler(text="Наоборот!  Расскажешь мне про Париж?")
async def answer_men(message: types.Message):
    await message.answer(text="Ты уверен, что против голосовых? Это довольно долгий рассказ :)",
                         reply_markup=answer_men_10_11)
    await sa.add_line(username=message.from_user.username,
                      from_user="Наоборот!  Расскажешь мне про Париж?",
                      from_bot="Ты уверен, что против голосовых? Это довольно долгий рассказ :)")


@dp.message_handler(text="Ого, неожиданно! Расскажешь?")
async def answer_men(message: types.Message):
    await message.answer(text="Ты уверен, что против голосовых? Это довольно долгий рассказ :)",
                         reply_markup=answer_men_10_11)
    await sa.add_line(username=message.from_user.username,
                      from_user="Ого, неожиданно! Расскажешь?",
                      from_bot="Ты уверен, что против голосовых? Это довольно долгий рассказ :)")



@dp.message_handler(text="Ладно, давай голосовыми :)")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF2GEKSSaXileJopm1grZTBUYUw5xcAAIIEgACLjT5SwRlUZh_7V-tIAQ")  # female_07
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF2mEKST81pTbtTL16FuLS_iS1RwQ0AAIKEgACLjT5S43nsKBxsKHOIAQ",  # female_08
                            reply_markup=answer_men_10_voice)
    await sa.add_line(username=message.from_user.username,
                      from_user="Ладно, давай голосовыми :)",
                      from_bot="female_07 female_08")


@dp.message_handler(text="Уверен, лучше текстом.")
async def answer_men(message: types.Message):
    await message.answer(text="Точно? Лучше один раз услышать, чем прочесть :)",
                         reply_markup=answer_men_12_13)
    await sa.add_line(username=message.from_user.username,
                      from_user="Уверен, лучше текстом.",
                      from_bot="Точно? Лучше один раз услышать, чем прочесть :)")


@dp.message_handler(text="Уговорила, рассказывай уже!")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF2GEKSSaXileJopm1grZTBUYUw5xcAAIIEgACLjT5SwRlUZh_7V-tIAQ")  # female_07
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIF2mEKST81pTbtTL16FuLS_iS1RwQ0AAIKEgACLjT5S43nsKBxsKHOIAQ",  # female_08
                            reply_markup=answer_men_10_voice)
    await sa.add_line(username=message.from_user.username,
                      from_user="Уговорила, рассказывай уже!",
                      from_bot="female_07 female_08")


@dp.message_handler(text="Точно, я люблю читать:)")
async def answer_men(message: types.Message):
    await message.answer(
        text="Хорошо, договорились. Так вот Париж, я поехала туда по обмену во время учебы, а потом не смогла расстаться с этим городом. Париж очень красивый и очень свободный. И знаешь, французы совсем не такие как мы, особенно молодежь. Кажется, что им все дозволено и они не видят смысла отказывать себе в удовольствиях.")
    await message.answer(
        text="А еще я почти не говорила по-французски когда приехала. А английский считается в Париже очень дурным тоном :) Лучше сказать 2 фразы на очень плохом французском, чем свободно общаться на чистом английском.",
        reply_markup=answer_men_14)
    await sa.add_line(username=message.from_user.username,
                      from_user="Точно, я люблю читать:)",
                      from_bot="А еще я почти не говорила по-французски когда приехала. А английский считается в Париже очень дурным тоном :) Лучше сказать 2 фразы на очень плохом французском, чем свободно общаться на чистом английском.")



@dp.message_handler(text="Кажется, ты была не очень занята учебой:)")
async def answer_men(message: types.Message):
    await message.answer(text="Возможно. Хотя учебы тоже было довольно много", reply_markup=answer_men_15)

    await sa.add_line(username=message.from_user.username,
                      from_user="Кажется, ты была не очень занята учебой:)",
                      from_bot="Возможно. Хотя учебы тоже было довольно много")


@dp.message_handler(text="Что именно ты изучала?")
async def answer_men(message: types.Message):
    await message.answer(
        text="Чего я только не изучала, там же не как у нас. Там ты сам составляешь себе программу и выбираешь предметы. Очень интересно, но от выбора глаза разбегаются. Скучаю немножко по студенчеству.",
        reply_markup=answer_men_16)
    await sa.add_line(username=message.from_user.username,
                      from_user="Что именно ты изучала?",
                      from_bot=" Чего я только не изучала, там же не как у нас. Там ты сам составляешь себе программу и выбираешь предметы. Очень интересно, но от выбора глаза разбегаются. Скучаю немножко по студенчеству.")


@dp.message_handler(text="А теперь ты вернулась в Россию? Почему?")
async def answer_men(message: types.Message):
    await message.answer(text="Соскучилась:) Пока вернулась на несколько месяцев, а дальше посмотрим.")
    await message.answer(text="Что о себе расскажешь? Где бы ты хотел жить?", reply_markup=answer_men_17)
    await sa.add_line(username=message.from_user.username,
                      from_user="А теперь ты вернулась в Россию? Почему?",
                      from_bot="Что о себе расскажешь? Где бы ты хотел жить?")


@dp.message_handler(text="Мне бы хотелось больше путешествовать :)")
async def answer_men(message: types.Message, state: FSMContext):
    await message.answer(text="Хороший ответ :) Я бы тоже хотела увидеть больше")
    await sa.add_line(username=message.from_user.username,
                      from_user="Мне бы хотелось больше путешествовать :)",
                      from_bot="Хороший ответ :) Я бы тоже хотела увидеть больше")
    await message.answer("Продолжение следует...")
    await message.answer(
        "Надеемся тебе понравился этот небольшой чат, хочешь узнать первым когда будет доступна полная версия?",
        reply_markup=final)
