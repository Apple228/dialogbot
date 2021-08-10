from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.answer_for_woman import answer_women_1, answer_women_2, answer_women_3_4, \
    answer_women_5_6_7_voice, answer_women_6_voice, answer_women_7_voice, answer_women_8_voice, answer_women_9_voice, \
    answer_women_10_voice, answer_women_11_voice, answer_women_12_voice, answer_women_13_voice, \
    answer_women_14_15_voice, answer_women_5_6_7, answer_women_6, answer_women_7, answer_women_8, answer_women_9, \
    answer_women_10_11, answer_women_12_13, answer_women_14, answer_women_16, answer_women_17, answer_women_15
from keyboards.default.final import delete, final
from loader import dp, db, sa


@dp.callback_query_handler(text="woman")
async def enter_sex(call: CallbackQuery):
    await db.update_user_sex(sex="Женский", telegram_id=call.from_user.id)
    await call.message.answer(text="Привет! Меня зовут Андрей. Кажется сегодня мне повезло :)",
                              reply_markup=answer_women_1)
    await sa.add_line(username=call.from_user.username,
                      from_user="Девушка",
                      from_bot="Привет! Меня зовут Андрей. Кажется сегодня мне повезло :)")


@dp.message_handler(text="Привет:) Случилось что-то хорошее?")
async def answer_men(message: types.Message):
    await message.answer(text="Ну конечно! Наше с тобой знакомство! Разве это не удача?", reply_markup=answer_women_2)
    await sa.add_line(username=message.from_user.username,
                      from_bot="Ну конечно! Наше с тобой знакомство! Разве это не удача?",
                      from_user="Привет:) Случилось что-то хорошее?")


@dp.message_handler(text="Возможно:) тогда расскажи мне о себе?")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG7GEKZHQHKIcKB26-0unPe9x6NOcpAAILDgACIPMJSA1TJAJbuRyMIAQ",
                            reply_markup=answer_women_3_4)  # male_01
    await sa.add_line(username=message.from_user.username,
                      from_user="Возможно:) тогда расскажи мне о себе?",
                      from_bot="male_01")


@dp.message_handler(text="У тебя очень приятный голос :)")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG7mEKZbapG6xc4haKpn8VuRbXbySiAAINDgACIPMJSBGao-8tbzCFIAQ",
                            reply_markup=answer_women_5_6_7_voice)  # male_02
    await sa.add_line(username=message.from_user.username,
                      from_user="У тебя очень приятный голос :)",
                      from_bot="male_02")


@dp.message_handler(text="Жил в Париже и Лондоне")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG8GEKZd2KdhSYB_alGWHtx0ifHj1aAAIODgACIPMJSE0UXXut74tFIAQ",  # male_03
                            reply_markup=answer_women_6_voice)
    await sa.add_line(username=message.from_user.username,
                      from_user="Жил в Париже и Лондоне",
                      from_bot="male_03")


@dp.message_handler(text="Прыгал с парашютом")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG8mEKZhOXbnGo87dpVTUqo8RhH1ulAAIPDgACIPMJSGLAF22C1YxxIAQ",  # male_04
                            reply_markup=answer_women_7_voice)
    await sa.add_line(username=message.from_user.username,
                      from_user="Прыгал с парашютом",
                      from_bot="male_04")


@dp.message_handler(text="Ни разу не был в кино за последние 5 лет")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG9GEKZiyulkirOhhDLQxP2yu37A1UAAIQDgACIPMJSEjNuA7I6-AMIAQ",  # male_05
                            reply_markup=answer_women_8_voice)
    await sa.add_line(username=message.from_user.username,
                      from_user="Ни разу не был в кино за последние 5 лет",
                      from_bot="male_05")


@dp.message_handler(text="Я подумаю :) Но что там с фактами, Париж?")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG9mEKZpFdVPUqhJU999QjAAEyhs3EswACEg4AAiDzCUh8zpIDLB26ISAE",  # male_06
                            reply_markup=answer_women_9_voice)
    await sa.add_line(username=message.from_user.username,
                      from_user="Я подумаю :) Но что там с фактами, Париж?",
                      from_bot="male_06")


@dp.message_handler(text="Ого, очень круто! Расскажи мне про Париж?")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG-GEKZrCVzzrYkZXBi7nm2atAws2IAAITDgACIPMJSBHo1aSeeG5YIAQ")  # male_07
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG-mEKZtU70mtb2bGo1PRc8KXjXZWdAAIUDgACIPMJSGYMRGOlvGgBIAQ",  # male_08
                            reply_markup=answer_women_10_voice)
    await sa.add_line(username=message.from_user.username,
                      from_user="Ого, очень круто! Расскажи мне про Париж?",
                      from_bot="male_07 male_08")


@dp.message_handler(text="Наоборот! Расскажешь мне про Париж?")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG-GEKZrCVzzrYkZXBi7nm2atAws2IAAITDgACIPMJSBHo1aSeeG5YIAQ")  # male_07
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG-mEKZtU70mtb2bGo1PRc8KXjXZWdAAIUDgACIPMJSGYMRGOlvGgBIAQ",  # male_08
                            reply_markup=answer_women_10_voice)
    await sa.add_line(username=message.from_user.username,
                      from_user="Наоборот! Расскажешь мне про Париж?",
                      from_bot="male_07 male_08")


@dp.message_handler(text="Ого, неожиданно! Расскажешь?")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG-GEKZrCVzzrYkZXBi7nm2atAws2IAAITDgACIPMJSBHo1aSeeG5YIAQ")  # male_07
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG-mEKZtU70mtb2bGo1PRc8KXjXZWdAAIUDgACIPMJSGYMRGOlvGgBIAQ",  # male_08
                            reply_markup=answer_women_10_voice)
    await sa.add_line(username=message.from_user.username,
                      from_user="Ого, неожиданно! Расскажешь?",
                      from_bot="male_07 male_08")


@dp.message_handler(text="Кажется, ты был не очень занят учебой:)")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG_GEKZy6rL9njWGGHiUJ4ZnytU5ChAAIVDgACIPMJSIalVuevKwH5IAQ",
                            reply_markup=answer_women_11_voice)  # male_09
    await sa.add_line(username=message.from_user.username,
                      from_user="Кажется, ты был не очень занят учебой:)",
                      from_bot="male_09")


@dp.message_handler(text="Что именно ты изучал?")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG_mEKZ03BIiuNerNwOqgks6VACj5bAAIWDgACIPMJSMJavc32_5qZIAQ",
                            reply_markup=answer_women_12_voice)  # male_10
    await sa.add_line(username=message.from_user.username,
                      from_user="Что именно ты изучал?",
                      from_bot="male_10")


@dp.message_handler(text="А теперь ты вернулся в Россию? Почему?")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIHAAFhCmikWKTByE7MdSN-16NgGLWv4gACGA4AAiDzCUhhhssAAWKEP2EgBA")
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIHAmEKaLFchjFlslnItO0EzYzlkYB7AAIcDgACIPMJSHHv7n3nw0pDIAQ",
                            reply_markup=answer_women_13_voice)  # male_12
    await sa.add_line(username=message.from_user.username,
                      from_user="А теперь ты вернулся в Россию? Почему?",
                      from_bot="male_11 male_12")


@dp.message_handler(text="Мне бы хотелось больше путешествовать")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIHBGEKaMPcNWRbOBPtE3ibrJ3Kj-_8AAIeDgACIPMJSJxI9LQNcHvoIAQ")
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIHBmEKaM2TPipmUZ3HZOAo5k7aEvpdAAIgDgACIPMJSOQry3xR9kdBIAQ",
                            reply_markup=answer_women_14_15_voice)  # male_14
    await sa.add_line(username=message.from_user.username,
                      from_user="Мне бы хотелось больше путешествовать",
                      from_bot="male_13 male_14")


@dp.message_handler(text="Не удобно сейчас слушать, давай текстом?")
async def answer_men(message: types.Message):
    await message.answer(text="Хорошо, давай текстом. Хотя мне кажется, что голосовые более живые и искренние.")
    await message.answer(text=" Итак, факты обо мне : \n"
                              " – Я жил в Париже и Лондоне. \n"
                              " – Прыгал с парашютом. \n"
                              " – Ни разу не был в кино за последние 5 лет. \n"
                              " Один из них неправда, как думаешь какой?", reply_markup=answer_women_5_6_7)
    await sa.add_line(username=message.from_user.username,
                      from_user="Не удобно сейчас слушать, давай текстом?",
                      from_bot=" Итак, факты обо мне :  – Я жил в Париже и Лондоне.  – Прыгал с парашютом.  – Ни разу не был в кино за последние 5 лет. Один из них неправда, как думаешь какой?")



@dp.message_handler(text="Жил в Париже и Лондоне.")
async def answer_men(message: types.Message):
    await message.answer(text="Нет, Париж - правда, Лондон тоже. Жил там несколько лет во время учебы.",
                         reply_markup=answer_women_6)
    await sa.add_line(username=message.from_user.username,
                      from_user="Жил в Париже и Лондоне.",
                      from_bot="Нет, Париж - правда, Лондон тоже. Жил там несколько лет во время учебы.")


@dp.message_handler(text="Прыгал с парашютом.")
async def answer_men(message: types.Message):
    await message.answer(text="Хаха, а ты молодец! Неужели это так легко угадать?",
                         reply_markup=answer_women_7)
    await sa.add_line(username=message.from_user.username,
                      from_user="Прыгал с парашютом.",
                      from_bot="Хаха, а ты молодец! Неужели это так легко угадать?")


@dp.message_handler(text="Ни разу не был в кино за последние 5 лет.")
async def answer_men(message: types.Message):
    await message.answer(
        text="Нет, это чистая правда! Очень люблю кино, но как-то все время не до этого. Может исправим это как-нибудь?)",
        reply_markup=answer_women_8)
    await sa.add_line(username=message.from_user.username,
                      from_user="Ни разу не был в кино за последние 5 лет.",
                      from_bot="Нет, это чистая правда! Очень люблю кино, но как-то все время не до этого. Может исправим это как-нибудь?)")


@dp.message_handler(text="Я подумаю :) Но что там с фактами, Париж?")
async def answer_men(message: types.Message):
    await message.answer(text="Нет, я не прыгал с парашютом, а в Париже действительно жил.",
                         reply_markup=answer_women_9)
    await sa.add_line(username=message.from_user.username,
                      from_user="Я подумаю :) Но что там с фактами, Париж?",
                      from_bot="Нет, я не прыгал с парашютом, а в Париже действительно жил")


@dp.message_handler(text="Ого, очень круто! Расскажи мне про Париж?")
async def answer_men(message: types.Message):
    await message.answer(text="Ты уверена, что против голосовых? Это довольно долгий рассказ :)",
                         reply_markup=answer_women_10_11)
    await sa.add_line(username=message.from_user.username,
                      from_user="Ого, очень круто! Расскажи мне про Париж?",
                      from_bot="Ты уверена, что против голосовых? Это довольно долгий рассказ :)")


@dp.message_handler(text="Наоборот! Расскажешь мне про Париж?")
async def answer_men(message: types.Message):
    await message.answer(text="Ты уверена, что против голосовых? Это довольно долгий рассказ :)",
                         reply_markup=answer_women_10_11)
    await sa.add_line(username=message.from_user.username,
                      from_user="Наоборот! Расскажешь мне про Париж?",
                      from_bot="Ты уверена, что против голосовых? Это довольно долгий рассказ :)")


@dp.message_handler(text="Ого, неожиданно!  Расскажешь?")
async def answer_men(message: types.Message):
    await message.answer(text="Ты уверена, что против голосовых? Это довольно долгий рассказ :)",
                         reply_markup=answer_women_10_11)
    await sa.add_line(username=message.from_user.username,
                      from_user="Ого, неожиданно!  Расскажешь?",
                      from_bot="Ты уверена, что против голосовых? Это довольно долгий рассказ :)")


@dp.message_handler(text="Ладно, давай голосовыми :)")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG-GEKZrCVzzrYkZXBi7nm2atAws2IAAITDgACIPMJSBHo1aSeeG5YIAQ")  # male_07
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG-mEKZtU70mtb2bGo1PRc8KXjXZWdAAIUDgACIPMJSGYMRGOlvGgBIAQ",  # male_08
                            reply_markup=answer_women_10_voice)
    await sa.add_line(username=message.from_user.username,
                      from_user="Ладно, давай голосовыми :)",
                      from_bot="male_07  male_08")


@dp.message_handler(text="Уверена, лучше текстом.")
async def answer_men(message: types.Message):
    await message.answer(text="Точно? Лучше один раз услышать, чем прочесть :)",
                         reply_markup=answer_women_12_13)
    await sa.add_line(username=message.from_user.username,
                      from_user="Уверена, лучше текстом.",
                      from_bot="Точно? Лучше один раз услышать, чем прочесть :)")


@dp.message_handler(text="Уговорил, рассказывай уже!")
async def answer_men(message: types.Message):
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG-GEKZrCVzzrYkZXBi7nm2atAws2IAAITDgACIPMJSBHo1aSeeG5YIAQ")  # male_07
    await dp.bot.send_voice(message.from_user.id,
                            "AwACAgIAAxkBAAIG-mEKZtU70mtb2bGo1PRc8KXjXZWdAAIUDgACIPMJSGYMRGOlvGgBIAQ",  # male_08
                            reply_markup=answer_women_10_voice)
    await sa.add_line(username=message.from_user.username,
                      from_user="Уговорил, рассказывай уже!",
                      from_bot="male_07  male_08")


@dp.message_handler(text="Точно, я люблю читать:)")
async def answer_men(message: types.Message):
    await message.answer(
        text="Хорошо, договорились. Так вот Париж, я поехал туда по обмену во время учебы, а потом не смог расстаться с этим городом. Париж очень красивый и очень свободный. И знаешь, французы совсем не такие как мы, особенно молодежь. Кажется, что им все дозволено и они не видят смысла отказывать себе в удовольствиях.")
    await message.answer(
        text="А еще я почти не говорил по-французски когда приехал. А английский считается в Париже очень дурным тоном :) Лучше сказать 2 фразы на очень плохом французском, чем свободно общаться на чистом английском.",
        reply_markup=answer_women_14)
    await sa.add_line(username=message.from_user.username,
                      from_user="Точно, я люблю читать:)",
                      from_bot="А еще я почти не говорил по-французски когда приехал. А английский считается в Париже очень дурным тоном :) Лучше сказать 2 фразы на очень плохом французском, чем свободно общаться на чистом английском.")


@dp.message_handler(text="Кажется, ты был не очень занят учебой:)")
async def answer_men(message: types.Message):
    await message.answer(text="Возможно. Хотя учебы тоже было довольно много", reply_markup=answer_women_15)
    await sa.add_line(username=message.from_user.username,
                      from_user="Кажется, ты был не очень занят учебой:)",
                      from_bot="Возможно. Хотя учебы тоже было довольно много")


@dp.message_handler(text="Что именно ты изучал?")
async def answer_men(message: types.Message):
    await message.answer(
        text="Чего я только не изучал, там же не как у нас. Там ты сам составляешь себе программу и выбираешь предметы. Очень интересно, но от выбора глаза разбегаются. Скучаю немножко по студенчеству.",
        reply_markup=answer_women_16)
    await sa.add_line(username=message.from_user.username,
                      from_user="Что именно ты изучал?",
                      from_bot="Чего я только не изучал, там же не как у нас. Там ты сам составляешь себе программу и выбираешь предметы. Очень интересно, но от выбора глаза разбегаются. Скучаю немножко по студенчеству.")


@dp.message_handler(text="А теперь ты вернулся в Россию? Почему?")
async def answer_men(message: types.Message):
    await message.answer(text="Соскучился:) Пока вернулся на несколько месяцев, а дальше посмотрим.")
    await message.answer(text="Что о себе расскажешь? Где бы ты хотела жить?", reply_markup=answer_women_17)
    await sa.add_line(username=message.from_user.username,
                      from_user="А теперь ты вернулся в Россию? Почему?",
                      from_bot="Что о себе расскажешь? Где бы ты хотела жить?")


@dp.message_handler(text="Мне бы хотелось больше путешествовать :)")
async def answer_men(message: types.Message, state: FSMContext):
    await message.answer(text="Хороший ответ :) Я бы тоже хотел увидеть больше", reply_markup=delete)
    await sa.add_line(username=message.from_user.username,
                      from_user="Мне бы хотелось больше путешествовать :)",
                      from_bot="Хороший ответ :) Я бы тоже хотел увидеть больше")
    await message.answer("Продолжение следует...")
    await message.answer(
        "Надеемся тебе понравился этот небольшой чат, хочешь узнать первым когда будет доступна полная версия?",
        reply_markup=final)

