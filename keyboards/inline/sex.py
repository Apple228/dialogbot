from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

sex = InlineKeyboardMarkup(row_width=2,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(
                                        text="Девушка",
                                        callback_data="woman"
                                    ),
                                    InlineKeyboardButton(
                                        text="Парень",
                                        callback_data="man"
                                    )
                                ]
                            ])
