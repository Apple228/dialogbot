import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from keyboards.inline.sex import sex
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer('Привет, Как тебя зовут?')
    await state.set_state("set_name")


@dp.message_handler(state="set_name")
async def enter_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Сколько тебе лет?")
    await state.set_state("set_age")


@dp.message_handler(state="set_age")
async def enter_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    try:
        await db.add_user(full_name=data.get("name"), username=message.from_user.username,
                          telegram_id=message.from_user.id, age=message.text)
    except asyncpg.exceptions.UniqueViolationError:
        await db.update_user_fullname(full_name=data.get("name"), age=message.text, telegram_id=message.from_user.id)
    await state.reset_state()
    await message.answer("Ты парень или девушка?", reply_markup=sex)
    # await state.set_state("set_sex")





