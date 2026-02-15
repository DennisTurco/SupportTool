from database.database_initializer import DatabaseInitializer
from database.enums.database_type import DatabaseType

if __name__ == "__main__":
    DatabaseInitializer.init_database(DatabaseType.PRODUCTION)
