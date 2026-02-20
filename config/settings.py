import os

"""
Contains structural and internal application constants.

Do NOT put runtime or user-editable configuration here.
For configurable values, use configuration.py and config.ini
"""

MIGRATIONS_DIR = os.path.join("database", "migrations")

PRODUCTION_DATABASE_DIR = os.path.join(os.path.expanduser("~"), "Documents", "Shard", "data")
PRODUCTION_DATABASE_PATH = os.path.join(PRODUCTION_DATABASE_DIR, "SupportTool.db")
