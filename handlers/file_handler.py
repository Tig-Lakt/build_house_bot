from aiogram import types
from aiogram.types import FSInputFile
from aiogram import Router, F

from config import FILE_PATH

from functions import get_all_apps_file


router = Router()


@router.callback_query(F.data == "get_file")
async def f_get_file(callback: types.CallbackQuery): 
    
    result = await get_all_apps_file()
    
    if result:
        await callback.message.answer_document(
            document=FSInputFile(FILE_PATH)
    )