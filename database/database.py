import sqlite3

from config.settings import PRODUCTION_DATABASE_PATH


class Database:
    @staticmethod
    def get_connection() -> sqlite3.Connection:
        connection = sqlite3.connect(PRODUCTION_DATABASE_PATH)
        connection.row_factory = sqlite3.Row
        return connection
