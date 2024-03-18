from aiogram.filters.state import State, StatesGroup


class NewsState(StatesGroup):
    titleuz = State()
    titleru = State()
    descriptionuz = State()
    descriptionru = State()
    image = State()
    confirm = State()