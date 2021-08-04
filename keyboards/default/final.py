from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

final = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Да, конечно!")
        ],
        [
            KeyboardButton(text="Нет, спасибо")
        ],

    ],
    resize_keyboard=True
)

delete = ReplyKeyboardRemove()