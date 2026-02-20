import logging
import os

from config.configuration import Configuration


class LogService:
    _is_configured = False

    @classmethod
    def get_logger(cls, name: str | None = None):
        if not cls._is_configured:
            cls._configure()
        return logging.getLogger(name)

    @classmethod
    def _configure(cls):
        config = Configuration()
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.getLevelName(config.log_level.upper()))

        formatter = logging.Formatter(config.log_format)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # File handler
        if not os.path.exists(config.log_folder):
            os.makedirs(config.log_folder)
        file_handler = logging.FileHandler(config.log_folder + config.log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)

        # prevent from duplicated handlers
        if not root_logger.handlers:
            root_logger.addHandler(console_handler)
            root_logger.addHandler(file_handler)

        cls._is_configured = True
