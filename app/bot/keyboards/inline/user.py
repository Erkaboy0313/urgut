from aiogram import types

confirm = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Ha", callback_data="yes"),
            types.InlineKeyboardButton(text="Yo'q", callback_data="no"),
        ],
    ]
)

commands = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Yangilik qo'shish", callback_data='news')
        ]
    ]
)