import sqlite3

from config.settings import PRODUCTION_DATABASE_PATH, TEST_DATABASE_PATH
from database.enums.database_type import DatabaseType


class Database:
    @staticmethod
    def get_connection(type: DatabaseType) -> sqlite3.Connection:
        if type == DatabaseType.PRODUCTION:
            return Database.__get_connection_from_production_database()
        elif type == DatabaseType.TEST:
            return Database.__get_connection_from_test_database()

    @staticmethod
    def __get_connection_from_production_database() -> sqlite3.Connection:
        connection = sqlite3.connect(PRODUCTION_DATABASE_PATH)
        connection.row_factory = sqlite3.Row
        return connection

    @staticmethod
    def __get_connection_from_test_database() -> sqlite3.Connection:
        connection = sqlite3.connect(TEST_DATABASE_PATH)
        connection.row_factory = sqlite3.Row
        return connection
