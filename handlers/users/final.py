from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.final import final, delete
from loader import dp, sa


@dp.message_handler(text="Мне нравится тебя слушать, продолжай :)")
async def answer_final(message: types.Message):
    await message.answer("Продолжение следует...")
    await message.answer(
        "Надеемся тебе понравился этот небольшой чат, хочешь узнать первым когда будет доступна полная версия?",
        reply_markup=final)


@dp.message_handler(text="Давай, текстом удобнее :)")
async def answer_final(message: types.Message):
    await message.answer("Продолжение следует...")
    await message.answer(
        "Надеемся тебе понравился этот небольшой чат, хочешь узнать первым когда будет доступна полная версия?",
        reply_markup=final)



@dp.message_handler(state="Final")
async def answer_final(message: types.Message, state: FSMContext):
    await message.answer("Продолжение следует...")
    await message.answer(
        "Надеемся тебе понравился этот небольшой чат, хочешь узнать первым когда будет доступна полная версия?",
        reply_markup=final)
    await state.reset_state()


@dp.message_handler(text="Да, конечно!")
async def answer_final(message: types.Message, state: FSMContext):
    await sa.add_line(username=message.from_user.username,
                from_bot="Надеемся тебе понравился этот небольшой чат, хочешь узнать первым когда будет доступна полная версия?",
                from_user="Да, конечно!")
    await message.answer("Отлично, договорились! Поделишься своими впечатлениями?", reply_markup=delete)
    await state.set_state("Отзыв")


@dp.message_handler(text="Нет, спасибо")
async def answer_final(message: types.Message, state: FSMContext):
    await sa.add_line(username=message.from_user.username, from_bot="Надеемся тебе понравился этот небольшой чат, хочешь узнать первым когда будет доступна полная версия?",
                from_user="Нет, спасибо!")
    await message.answer("Нам жаль это слышать! Поделишься своими впечатлениями?", reply_markup=delete)
    await state.set_state("Отзыв")


@dp.message_handler(state="Отзыв")
async def answer_final(message: types.Message, state: FSMContext):
    await sa.add_line(username=message.from_user.username, from_bot="Отлично, договорились! Поделишься своими впечатлениями?",
                from_user=message.text)
    await message.answer("Спасибо за обратную связь", reply_markup=delete)
    await state.reset_state()
