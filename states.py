from aiogram.dispatcher.filters.state import State, StatesGroup


class States(StatesGroup):
    image = State()
    work = State()

