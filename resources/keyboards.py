from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


# - отдельные кнопки
inline_btn_head_menu = InlineKeyboardButton(text='Меню ♻️', callback_data='head_menu')
###################################################################################################
# главное меню - вариант "без подписки"
btn_begin = InlineKeyboardButton(text='Начать', callback_data='begin')

begin_inline_btns = [
    btn_begin,
]

begin_inline_kb = InlineKeyboardBuilder()
begin_inline_kb.add(*begin_inline_btns)
begin_inline_kb.adjust(2)

###################################################################################################
# главное меню - вариант "без подписки"
btn_brick = InlineKeyboardButton(text='Кирпичные', callback_data='housetype_brick')
btn_frame = InlineKeyboardButton(text='Каркасные', callback_data='housetype_frame')
btn_modular = InlineKeyboardButton(text='Модульные', callback_data='housetype_modular')
btn_havent_decided = InlineKeyboardButton(text='Еще не определился', callback_data='housetype_havent_decided')
btn_examples = InlineKeyboardButton(text='Примеры работ', callback_data='housetype_examples')

housetype_inline_btns = [
    btn_brick,
    btn_frame,
    btn_modular,
    btn_havent_decided,
    btn_examples,
]

housetype_inline_kb = InlineKeyboardBuilder()
housetype_inline_kb.add(*housetype_inline_btns)
housetype_inline_kb.adjust(2)

###################################################################################################
# главное меню - вариант "без подписки"
btn_housetype_next = InlineKeyboardButton(text='🔘 Да, подходит', callback_data='stephousetype_next')
btn_housetype_back = InlineKeyboardButton(text='🔘 Назад', callback_data='stephousetype_back')

housetype_btns = [
    btn_housetype_next,
    btn_housetype_back,
]

housetype_step_kb = InlineKeyboardBuilder()
housetype_step_kb.add(*housetype_btns)
housetype_step_kb.adjust(2)

###################################################################################################
# главное меню - вариант "без подписки"
btn_examples_next = InlineKeyboardButton(text='🔘 Да', callback_data='examples_next')
btn_examples_back = InlineKeyboardButton(text='🔘 Выйти', callback_data='examples_back')

examples_btns = [
    btn_examples_next,
    btn_examples_back,
]

examples_step_kb = InlineKeyboardBuilder()
examples_step_kb.add(*examples_btns)
examples_step_kb.adjust(2)

###################################################################################################
# главное меню - вариант "без подписки"
btn_area_1 = InlineKeyboardButton(text='🔘 до 100 м²', callback_data='area_1')
btn_area_2 = InlineKeyboardButton(text='🔘 100–150 м²', callback_data='area_2')
btn_area_3 = InlineKeyboardButton(text='🔘 150–200 м²', callback_data='area_3')
btn_area_4 = InlineKeyboardButton(text='🔘 более 200 м²', callback_data='area_4')
btn_area_5 = InlineKeyboardButton(text='🔘 Пока не знаю', callback_data='area_5')

area_btns = [
    btn_area_1,
    btn_area_2,
    btn_area_3,
    btn_area_4,
    btn_area_5
]

area_step_kb = InlineKeyboardBuilder()
area_step_kb.add(*area_btns)
area_step_kb.adjust(2)

###################################################################################################
# главное меню - вариант "без подписки"
btn_plot_1 = InlineKeyboardButton(text='🔘 Да', callback_data='plot_1')
btn_plot_2 = InlineKeyboardButton(text='🔘 В процессе покупки', callback_data='plot_2')
btn_plot_3 = InlineKeyboardButton(text='🔘 Пока нет', callback_data='plot_3')
btn_plot_4 = InlineKeyboardButton(text='🔘 Нужна помощь с подбором', callback_data='plot_4')

plot_btns = [
    btn_plot_1,
    btn_plot_2,
    btn_plot_3,
    btn_plot_4,
]

plot_step_kb = InlineKeyboardBuilder()
plot_step_kb.add(*plot_btns)
plot_step_kb.adjust(1)

###################################################################################################
# главное меню - вариант "без подписки"
btn_budget_1 = InlineKeyboardButton(text='🔘 до 3 млн ₽', callback_data='budget_1')
btn_budget_2 = InlineKeyboardButton(text='🔘 3–5 млн ₽', callback_data='budget_2')
btn_budget_3 = InlineKeyboardButton(text='🔘 5–8 млн ₽', callback_data='budget_3')
btn_budget_4 = InlineKeyboardButton(text='🔘 более 8 млн ₽', callback_data='budget_4')
btn_budget_5 = InlineKeyboardButton(text='🔘 Пока не решил(а)', callback_data='budget_5')

budget_btns = [
    btn_budget_1,
    btn_budget_2,
    btn_budget_3,
    btn_budget_4,
    btn_budget_5,
]

budget_step_kb = InlineKeyboardBuilder()
budget_step_kb.add(*budget_btns)
budget_step_kb.adjust(2)

###################################################################################################
# 
btn_start_date_1 = InlineKeyboardButton(text='🔘 В ближайшие 1–2 месяца', callback_data='start_date_1')
btn_start_date_2 = InlineKeyboardButton(text='🔘 Через 3–6 месяцев', callback_data='start_date_2')
btn_start_date_3 = InlineKeyboardButton(text='🔘 Через год', callback_data='start_date_3')
btn_start_date_4 = InlineKeyboardButton(text='🔘 Просто интересуюсь', callback_data='start_date_4')

start_date_btns = [
    btn_start_date_1,
    btn_start_date_2,
    btn_start_date_3,
    btn_start_date_4,
]

start_date_step_kb = InlineKeyboardBuilder()
start_date_step_kb.add(*start_date_btns)
start_date_step_kb.adjust(2)


###################################################################################################
# главное меню - вариант "без подписки"
btn_comment_add = InlineKeyboardButton(text='🔘 Добавить', callback_data='comment_add')
btn_comment_skip = InlineKeyboardButton(text='🔘 Пропустить', callback_data='comment_skip')

comment_btns = [
    btn_comment_add,
    btn_comment_skip,
]

comment_step_kb = InlineKeyboardBuilder()
comment_step_kb.add(*comment_btns)
comment_step_kb.adjust(2)