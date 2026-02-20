import logging
from pathlib import Path

import pytest

from config.configuration import Configuration
from services.log_service import LogService


@pytest.fixture(autouse=True)
def reset_log_service():
    LogService._is_configured = False
    logging.getLogger().handlers.clear()


def test_get_logger_returns_logger():
    logger = LogService.get_logger("my_test_logger")
    assert isinstance(logger, logging.Logger)
    # should have 2 handlers
    assert len(logging.getLogger().handlers) >= 2


def test_logger_level_matches_config(monkeypatch):
    monkeypatch.setattr(Configuration, "log_level", "DEBUG")
    LogService._is_configured = False
    LogService.get_logger()
    root_logger = logging.getLogger()
    assert root_logger.level == logging.DEBUG


def test_file_handler_created(tmp_path):
    LogService.get_logger("file_test_logger", folder=tmp_path, file="test.log")

    # check if FileHandler file exists
    file_handlers = [h for h in logging.getLogger().handlers if isinstance(h, logging.FileHandler)]
    assert file_handlers, "error during FileHandler creation"

    for fh in file_handlers:
        assert tmp_path.as_posix() in Path(fh.baseFilename).as_posix()
