import os

MIGRATIONS_DIR = os.path.join("database", "migrations")

PRODUCTION_DATABASE_DIR = os.path.join(os.environ["USERPROFILE"], "Documents", "Shard", "data")
PRODUCTION_DATABASE_PATH = os.path.join(PRODUCTION_DATABASE_DIR, "SupportTool.db")
