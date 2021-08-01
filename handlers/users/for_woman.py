from aiogram.types import CallbackQuery

from loader import dp, db



@dp.callback_query_handler(text="woman")
async def enter_sex(call: CallbackQuery):
    await db.update_user_sex(sex="Женский", telegram_id=call.from_user.id)
    await call.message.answer(text="Привет! Меня зовут Андрей. Кажется сегодня мне повезло :)")
