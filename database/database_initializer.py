import os
import sqlite3

from config.settings import (
    MIGRATIONS_DIR,
    PRODUCTION_DATABASE_DIR,
    PRODUCTION_DATABASE_PATH,
)


class DatabaseInitializer:
    @staticmethod
    def init_database():
        DatabaseInitializer.__create_database_if_missing()
        DatabaseInitializer.__run_migrations()

    @staticmethod
    def __create_database_if_missing():
        os.makedirs(PRODUCTION_DATABASE_DIR, exist_ok=True)

    @staticmethod
    def __run_migrations():
        with sqlite3.connect(PRODUCTION_DATABASE_PATH) as conn:
            cursor = conn.cursor()

            DatabaseInitializer.__read_and_execute_sql_script(cursor, os.path.join(MIGRATIONS_DIR, "001_schema.sql"))
            DatabaseInitializer.__read_and_execute_sql_script(cursor, os.path.join(MIGRATIONS_DIR, "002_seed.sql"))

            print("Migrations executed correctly!")

    @staticmethod
    def __read_and_execute_sql_script(cursor: sqlite3.Cursor, migration: str):
        with open(migration, encoding="utf-8") as file:
            script = file.read()
        cursor.executescript(script)
