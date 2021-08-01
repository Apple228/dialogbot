from aiogram.types import CallbackQuery

from loader import dp, db


@dp.callback_query_handler(text="man")
async def enter_sex(call: CallbackQuery):
    await db.update_user_sex(sex="Мужской", telegram_id=call.from_user.id)
    await call.message.answer(text="Привет! Меня зовут Аня. Кажется сегодня мне повезло :)")
