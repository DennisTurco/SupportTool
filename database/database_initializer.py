import os
import sqlite3

from config.settings import (
    MIGRATIONS_DIR,
    PRODUCTION_DATABASE_DIR,
    PRODUCTION_DATABASE_PATH,
    TEST_DATABASE_DIR,
    TEST_DATABASE_PATH,
)
from database.enums.database_type import DatabaseType


class DatabaseInitializer:
    @staticmethod
    def init_database(database: DatabaseType):
        database_path = DatabaseInitializer.__get_path_by_type(database)
        database_dir = DatabaseInitializer.__get_dir_by_type(database)
        DatabaseInitializer.__create_database_if_missing(database_dir)
        DatabaseInitializer.__run_migrations(database_path)

    @staticmethod
    def __create_database_if_missing(database_dir: str):
        os.makedirs(database_dir, exist_ok=True)

    @staticmethod
    def __run_migrations(database_path: str):
        with sqlite3.connect(database_path) as conn:
            cursor = conn.cursor()

            DatabaseInitializer.__read_and_execute_sql_script(cursor, os.path.join(MIGRATIONS_DIR, "001_schema.sql"))
            DatabaseInitializer.__read_and_execute_sql_script(cursor, os.path.join(MIGRATIONS_DIR, "002_seed.sql"))

            print("Migrations executed correctly!")

    @staticmethod
    def __read_and_execute_sql_script(cursor: sqlite3.Cursor, migration: str):
        with open(migration, encoding="utf-8") as file:
            script = file.read()
        cursor.executescript(script)

    @staticmethod
    def __get_path_by_type(database: DatabaseType):
        if database == DatabaseType.PRODUCTION:
            return PRODUCTION_DATABASE_PATH
        elif database == DatabaseType.TEST:
            return TEST_DATABASE_PATH

    @staticmethod
    def __get_dir_by_type(database: DatabaseType):
        if database == DatabaseType.PRODUCTION:
            return PRODUCTION_DATABASE_DIR
        elif database == DatabaseType.TEST:
            return TEST_DATABASE_DIR
