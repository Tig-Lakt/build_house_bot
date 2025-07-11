from aiogram import types
from aiogram import Router
from aiogram.filters.command import Command

from resources import (
    begin_inline_kb,
    welcome_text,
)

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    
    await message.answer(
            text=welcome_text,
            reply_markup=begin_inline_kb.as_markup(resize_keyboard=True)
        )