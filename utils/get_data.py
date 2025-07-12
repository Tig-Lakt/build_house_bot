import os
import sys

import yaml
import logging
from dotenv import load_dotenv

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_PATH)

dotenv_path = os.path.join(PROJECT_PATH, ".env")
load_dotenv(dotenv_path, override=True)

CONFIG_FILE_PATH = os.path.join(PROJECT_PATH, "src", "config.yaml")

logging.basicConfig(level=logging.INFO)


def get_bot_token() -> str:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        logging.error("Ошибка: Переменная окружения TELEGRAM_BOT_TOKEN не задана.")
        return None 

    return token


def get_admin() -> str:
    admin_id = os.environ.get("ADMIN_ID")
    if not admin_id:
        logging.error("Ошибка: Переменная окружения ADMIN_ID не задана.")
        return None 

    return admin_id


def update_config_file(token: str=None, host: str=None, port: int=None, database: str=None, user: str=None, password: str=None):
    config_data = {"bot_token": token}

    if host is not None:
        config_data["host"] = host
        config_data["port"] = port
        config_data["database"] = database
        config_data["user"] = user
        config_data["password"] = password

    try:
        with open(CONFIG_FILE_PATH, "w") as file:
            yaml.dump(config_data, file)
    except Exception as e:
        logging.error(f"Ошибка при записи в config.yaml: {e}")


def get_db_connection_params() -> list[str]:
    try:
        with open(CONFIG_FILE_PATH, "r") as file:
            config = yaml.safe_load(file)
            host = os.environ.get("DB_HOST") or config.get("host")
            port = os.environ.get("DB_PORT") or config.get("port")
            database = os.environ.get("DB_NAME") or config.get("database")
            user = os.environ.get("DB_USER") or config.get("user")
            password = os.environ.get("DB_PASSWORD") or config.get("password")

            return [host, port, database, user, password]
    except FileNotFoundError:
        print(f"Ошибка: Файл конфигурации не найден: {CONFIG_FILE_PATH}")
        return []
    except KeyError as e:
        print(f"Ошибка: Ключ '{e}' отсутствует в файле конфигурации.")
        return []
    except yaml.YAMLError as e:
        print(f"Ошибка: Ошибка при чтении YAML файла: {e}")
        return []
