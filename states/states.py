from aiogram.fsm.state import StatesGroup, State


class UserData(StatesGroup):
    housetype = State()
    area = State()
    plot = State()
    budget = State()
    start_date = State()
    comment = State()
    phone = State()
    name = State()