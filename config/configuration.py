import configparser
import os

from exceptions.exceptions import ConfigurationFileNotFound

"""
Handles runtime configuration loaded from config.ini.

Do NOT put structural or hard-coded application constants here.
Those belong in settings.py.
"""


class Configuration:
    def __init__(self, path="./config/config.ini"):
        if not os.path.exists(path):
            raise ConfigurationFileNotFound(f"Configuration file .ini not found in {path}")

        self._config = configparser.ConfigParser(interpolation=None)
        self._config.read(path)

    @property
    def icon(self):
        return self._config.get("GUI", "icon")

    @property
    def width(self):
        return self._config.getint("GUI", "width")

    @property
    def height(self):
        return self._config.getint("GUI", "height")

    @property
    def theme(self):
        return self._config.get("GUI", "theme")

    @property
    def version(self):
        return self._config.get("APP", "version")

    @property
    def log_level(self):
        return self._config.get("LOGGING", "log_level")

    @property
    def log_folder(self):
        return self._config.get("LOGGING", "log_folder")

    @property
    def log_file(self):
        return self._config.get("LOGGING", "log_file")

    @property
    def log_format(self):
        return self._config.get("LOGGING", "log_format")
