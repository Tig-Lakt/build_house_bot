welcome_text = """📌 Продолжая отвечать на вопросы бота, вы соглашаетесь на
обработку персональных данных согласно <a href="https://google.com">политике
конфиденциальности</a>.
"""

choise_housetype_text = """Приветствуем! Мы строим дома под ключ:
🧱 Кирпичные | 🪵 Каркасные | 🏠 Модульные
Давайте подберём для вас лучший вариант. Ответьте на
несколько коротких вопросов — это займёт 1–2 минуты 🙌
"""

brick_housetype_text = """
🧱 Кирпичные дома — это долговечность, прочность и
классический внешний вид.
Отлично подходят для постоянного проживания.
✅ Срок службы: 50+ лет
✅ Тепло- и шумоизоляция
✅ Возможность нестандартной архитектуры
Продолжим?
"""

frame_housetype_text = """
🪵 Каркасные дома — тёплые, энергоэффективные, быстро
строятся.
✅ Строим от 3 месяцев
✅ Экономия на отоплении
✅ Гарантия 10 лет
Продолжим?
"""

modular_housetype_text = """
🏠 Модульные дома — современное решение для дачи или
постоянного проживания.
Собираются на участке за считанные дни.
✅ Минимум подготовки
✅ Быстрый монтаж
✅ Можно перевезти
"""

havent_decided_housetype_text = """
Ничего страшного! Мы поможем подобрать оптимальный тип по
бюджету и задачам.
Перейдём к следующему вопросу?
"""

examples_housetype_text = """
📸 Вот примеры наших реализованных проектов:
👉 Посмотреть (тут ссылка на страницу сайта)
Продолжим подбор?
"""

area_text = """
Примерная площадь дома?
"""

plot_text = """
У вас уже есть участок под строительство?

"""

budget_text = """
Какой ориентировочный бюджет?
"""

start_date_text = """
Когда планируете начать строительство?
"""

comment_text = """
Хотите оставить комментарий, пожелания или задать вопрос?
"""

comment_add_text = """
Введите текст комментария
"""

contacts_text = """
Почти готово! Оставьте, пожалуйста, ваши контактные данные
— мы свяжемся и проконсультируем вас:
📱 Введите номер телефона: (телефон должен соответствовать формату +7********** - после +7 цифры без пробелов)
"""

contacts_error_text = """
Ошибка!

Номер телефон должен соответствовать формату +7********** - после +7 цифры без пробелов, повторите ввод.
"""

name_text = """
🧑 Как вас зовут?

"""

async def get_fin_text(user_name):
    fin_text = f"""
Спасибо, {user_name}! Мы получили вашу заявку.
Наш специалист свяжется с вами в ближайшее время 📞
📸 Пока можно посмотреть ещё примеры работ:
👉 Перейти на сайт
"""
    return fin_text
