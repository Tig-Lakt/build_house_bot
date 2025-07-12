from aiogram import types, Bot
from aiogram import Router, F
from aiogram.fsm.context import FSMContext

from states import UserData
from database.database import add_app
from resources import *
from functions import is_valid_format_phone
from config import (
    TOKEN,
    ADMIN_ID,
)

bot = Bot(token=TOKEN)
router = Router()


async def go_back(callback: types.CallbackQuery, state: FSMContext, previous_state, previous_text, previous_kb):
    try:
        await callback.message.delete()
    except:
        pass
    await callback.message.answer(
        text=previous_text,
        reply_markup=previous_kb.as_markup(resize_keyboard=True)
    )
    await state.set_state(previous_state)

@router.callback_query(F.data == "begin")
async def f_begin(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.message.delete()
    except:
        pass    
    await callback.message.answer(
        text=choise_housetype_text,
        reply_markup=housetype_inline_kb.as_markup(resize_keyboard=True)
    )
    await state.set_state(UserData.housetype)
    
@router.callback_query(F.data.startswith('housetype_'))
async def f_input_housetype(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.message.delete()
    except:
        pass
    await state.update_data(housetype=callback.data[10:])
    
    if callback.data[10:] == 'brick':
        text = brick_housetype_text
        kb = housetype_step_kb
    elif callback.data[10:] == 'frame':
        text = frame_housetype_text
        kb = housetype_step_kb
    elif callback.data[10:] == 'modular':
        text = modular_housetype_text
        kb = housetype_step_kb
    elif callback.data[10:] == 'havent_decided':
        text = havent_decided_housetype_text
        kb = housetype_step_kb
    elif callback.data[10:] == 'examples':
        text = examples_housetype_text
        kb = examples_step_kb
    
    await callback.message.answer(
        text=text,
        reply_markup=kb.as_markup(resize_keyboard=True)
    )

@router.callback_query(F.data.startswith('stephousetype_'))
async def f_stephousetype(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.message.delete()
    except:
        pass
    if callback.data[14:] == 'back':
        await go_back(callback, state, None, choise_housetype_text, housetype_inline_kb)
    elif callback.data[14:] == 'next':
        await callback.message.answer(
            text=area_text,
            reply_markup=area_step_kb.as_markup(resize_keyboard=True)
        )
        await state.set_state(UserData.area)

@router.callback_query(F.data.startswith('area_'))
async def f_input_area(callback: types.CallbackQuery, state: FSMContext):
    if callback.data[5:] == 'back':
        await go_back(callback, state, UserData.housetype, choise_housetype_text, housetype_inline_kb)
        return
        
    try:
        await callback.message.delete()
    except:
        pass
    await state.update_data(area=callback.data[5:])
    await callback.message.answer(
        text=plot_text,
        reply_markup=plot_step_kb.as_markup(resize_keyboard=True)
    )
    await state.set_state(UserData.plot)
    
@router.callback_query(F.data.startswith('plot_'))
async def f_input_plot(callback: types.CallbackQuery, state: FSMContext):
    if callback.data[5:] == 'back':
        await go_back(callback, state, UserData.area, area_text, area_step_kb)
        return
        
    try:
        await callback.message.delete()
    except:
        pass
    await state.update_data(plot=callback.data[5:])
    await callback.message.answer(
        text=budget_text,
        reply_markup=budget_step_kb.as_markup(resize_keyboard=True)
    )
    await state.set_state(UserData.budget)
    
@router.callback_query(F.data.startswith('budget_'))
async def f_input_budget(callback: types.CallbackQuery, state: FSMContext):
    if callback.data[7:] == 'back':
        await go_back(callback, state, UserData.plot, plot_text, plot_step_kb)
        return
        
    try:
        await callback.message.delete()
    except:
        pass
    await state.update_data(budget=callback.data[7:])
    await callback.message.answer(
        text=start_date_text,
        reply_markup=start_date_step_kb.as_markup(resize_keyboard=True)
    )
    await state.set_state(UserData.start_date)
    
@router.callback_query(F.data.startswith('start_date_'))
async def f_input_start_date(callback: types.CallbackQuery, state: FSMContext):
    if callback.data[11:] == 'back':
        await go_back(callback, state, UserData.budget, budget_text, budget_step_kb)
        return
        
    try:
        await callback.message.delete()
    except:
        pass
    await state.update_data(start_date=callback.data[11:])
    await callback.message.answer(
        text=comment_text,
        reply_markup=comment_step_kb.as_markup(resize_keyboard=True)
    )
    await state.set_state(UserData.comment)
    
@router.callback_query(F.data.startswith('comment_'))
async def f_comment(callback: types.CallbackQuery, state: FSMContext):
    if callback.data[8:] == 'back':
        await go_back(callback, state, UserData.start_date, start_date_text, start_date_step_kb)
        return
        
    try:
        await callback.message.delete()
    except:
        pass
    if callback.data[8:] == 'skip':
        await state.update_data(comment='Не указано')
        await callback.message.answer(contacts_text)
        await state.set_state(UserData.phone)
    elif callback.data[8:] == 'add':
        await callback.message.answer(text=comment_add_text)
        await state.set_state(UserData.comment)

@router.message(UserData.comment)
async def f_input_comment(message: types.Message, state: FSMContext):
    await state.update_data(comment=message.text)
    await message.answer(contacts_text)
    await state.set_state(UserData.phone)
    
@router.message(UserData.phone)
async def f_input_phone(message: types.Message, state: FSMContext):
    if message.text.lower() == 'назад':
        await message.answer(
            text=comment_text,
            reply_markup=comment_step_kb.as_markup(resize_keyboard=True)
        )
        await state.set_state(UserData.comment)
        return
        
    check_phone_format = await is_valid_format_phone(message.text)
    if check_phone_format:
        await state.update_data(phone=message.text)
        await message.answer(name_text)
        await state.set_state(UserData.name)
    else:
        await message.answer(contacts_error_text)
        await state.set_state(UserData.phone)
        
@router.message(UserData.name)
async def f_input_name(message: types.Message, state: FSMContext):
    if message.text.lower() == 'назад':
        await message.answer(contacts_text)
        await state.set_state(UserData.phone)
        return
        
    user_id = message.from_user.id
    await state.update_data(name=message.text)
    user_data = await state.get_data()
    
    housetype = user_data['housetype']
    area = user_data['area']
    plot = user_data['plot']
    budget = user_data['budget']
    start_date = user_data['start_date']
    comment = user_data['comment']
    phone = user_data['phone']
    name = user_data['name']
    
    text = await get_fin_text(name)
    await message.answer(text)
    
    await add_app(user_id, housetype, int(area), int(plot), int(budget), int(start_date), comment, phone, name)
    
    await bot.send_message(
        chat_id=ADMIN_ID,
        text=f"""Поступила новая заявка от:
USER_ID: {user_id}, 
Имя: {name}"""    
    )
    
    await state.clear()
    
    