from database.database import DataBase


async def create_models():
    db = DataBase()
    if await db.connect():
        try:
            await db.execute('''
                CREATE TABLE IF NOT EXISTS applications (
                    id BIGSERIAL,
                    user_id BIGINT NOT NULL,
                    housetype TEXT NOT NULL,
                    area INT NOT NULL,
                    plot INT NOT NULL,
                    budget INT NOT NULL,
                    start_date INT NOT NULL,
                    comment TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    name TEXT NOT NULL
                );''')
            
            await db.execute('''
                CREATE TABLE IF NOT EXISTS areas (
                    area_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    area_name VARCHAR(50) NOT NULL UNIQUE
                );''')
            
            await db.execute('''
                CREATE TABLE IF NOT EXISTS plots (
                    plot_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    plot_name VARCHAR(50) NOT NULL UNIQUE
                );''')
            
            await db.execute('''
                CREATE TABLE IF NOT EXISTS budgets (
                    budget_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    budget_name VARCHAR(50) NOT NULL UNIQUE
                );''')
            
            await db.execute('''
                CREATE TABLE IF NOT EXISTS start_dates (
                    start_date_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    start_date_name VARCHAR(50) NOT NULL UNIQUE
                );''')
            
            await db.execute('''
                INSERT INTO areas(area_name) VALUES
                    ('до 100 м²'),
                    ('100–150 м²'),
                    ('150–200 м²'),
                    ('более 200 м²'),
                    ('Пока не знаю')
                    
                ON CONFLICT (area_name) DO NOTHING;
            ''')
            
            await db.execute('''
                INSERT INTO plots(plot_name) VALUES
                    ('Да'),
                    ('В процессе покупки'),
                    ('Пока нет'),
                    ('Нужна помощь с подбором')
                    
                ON CONFLICT (plot_name) DO NOTHING;
            ''')
            
            await db.execute('''
                INSERT INTO budgets(budget_name) VALUES
                    ('до 3 млн ₽'),
                    ('3–5 млн ₽'),
                    ('5–8 млн ₽'),
                    ('более 8 млн ₽'),
                    ('Пока не решил(а)')
                    
                ON CONFLICT (budget_name) DO NOTHING;
            ''')
            
            await db.execute('''
                INSERT INTO start_dates(start_date_name) VALUES
                    ('В ближайшие 1–2 месяца'),
                    ('Через 3–6 месяцев'),
                    ('Через год'),
                    ('Просто интересуюсь')
                    
                ON CONFLICT (start_date_name) DO NOTHING;
            ''')

        except Exception as e:
            print(f"Ошибка при работе с базой данных: {e}")

        finally:
            await db.close()