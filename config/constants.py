import os
import sys
from utils import (
    get_bot_token, 
    get_db_connection_params, 
    update_config_file,
    get_admin,
)


update_config_file()

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, PROJECT_PATH)

TOKEN = get_bot_token()

DB_CONN = get_db_connection_params()

ADMIN_ID = get_admin()