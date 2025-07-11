import asyncpg
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

from config import DB_CONN


class DataBase:
    
    def __init__(self):
        self.host = DB_CONN[0]
        self.port = DB_CONN[1]
        self.database = DB_CONN[2]
        self.user = DB_CONN[3]
        self.password = DB_CONN[4]

        if not all([self.host, self.port, self.database, self.user, self.password]):
            raise ValueError(
                "Необходимо установить переменные окружения: DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD"
            )

        self.connection = None
        self.dsn = (
            f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        )

    async def connect(self) -> bool:
        try:
            self.connection = await asyncpg.connect(self.dsn)
            logger.info("Успешно подключено к PostgreSQL!")
            return True
        except asyncpg.PostgresConnectionError as e:
            logger.error(f"Ошибка подключения к PostgreSQL: {e}")
            return False

    async def execute(self, query: str, *args) -> bool:
        if self.connection is None:
            logger.error("Ошибка: Нет активного подключения к базе данных.")
            return False

        try:
            await self.connection.execute(query, *args)
            return True
        except Exception as e:
            logger.exception(f"Ошибка выполнения запроса: {e}") 
            return False

    async def fetch(self, query: str, *args) -> list[asyncpg.Record] | None:
        if self.connection is None:
            logger.error("Ошибка: Нет активного подключения к базе данных.")
            return None

        try:
            rows = await self.connection.fetch(query, *args)
            return rows
        except Exception as e:
            logger.exception(f"Ошибка выполнения запроса: {e}")  
            return None

    async def fetchrow(self, query: str, *args) -> asyncpg.Record | None:
        if self.connection is None:
            logger.error("Ошибка: Нет активного подключения к базе данных.")
            return None

        try:
            row = await self.connection.fetchrow(query, *args)
            return row
        except Exception as e:
            logger.exception(f"Ошибка выполнения запроса: {e}")  
            return None

    async def close(self):
        if self.connection:
            await self.connection.close()
            logger.info("Соединение с PostgreSQL закрыто.")
        else:
            logger.warning("Нет активного соединения для закрытия.")


async def add_app(user_id: int,
                housetype, 
                area: int, 
                plot: int,
                budget: int,
                start_date: int,
                comment: str,
                phone: str,
                name: str):
    
    db = DataBase()
    
    try:
        if not await db.connect():
            logger.error("Не удалось подключиться к базе данных.")
            return

        await db.execute(
            """INSERT INTO applications(
                user_id, 
                housetype, 
                area, 
                plot,
                budget,
                start_date,
                comment,
                phone,
                name           
                ) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9)""",
                user_id, 
                housetype, 
                area, 
                plot,
                budget,
                start_date,
                comment,
                phone,
                name
        )

    except Exception as e:
        logger.exception(f"Ошибка при работе с базой данных: {e}")
    finally:
        if db.connection:
            await db.close()