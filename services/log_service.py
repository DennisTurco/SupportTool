import logging
from pathlib import Path

from config.configuration import Configuration


class LogService:
    _is_configured = False

    @classmethod
    def get_logger(cls, name: str | None = None, folder: Path | None = None, file: str | None = None):
        if not cls._is_configured:
            cls._configure(folder=folder, file=file)
        return logging.getLogger(name)

    @classmethod
    def _configure(cls, folder: Path | None = None, file: str | None = None):
        config = Configuration()
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.getLevelName(config.log_level.upper()))

        root_logger.handlers.clear()

        formatter = logging.Formatter(config.log_format)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # File handler
        log_folder = Path(folder or config.log_folder)
        log_folder.mkdir(parents=True, exist_ok=True)
        log_file = file or config.log_file
        log_path = log_folder / log_file
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)

        root_logger.addHandler(console_handler)
        root_logger.addHandler(file_handler)

        cls._is_configured = True
