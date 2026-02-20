from config.configuration import Configuration
from exceptions.exceptions import ConfigurationFileNotFound

configs = """
    [GUI]
    icon = test.png
    width = 500
    height = 500
    theme = light

    [APP]
    version = 1.0.0

    [LOGGING]
    log_level = DEBUG
    log_file = test.log
    log_format = format
"""


def test_configuaration_file_path_error():
    try:
        Configuration(path="./not_valid_path/file/.ini")
        assert False
    except ConfigurationFileNotFound:
        assert True


def test_configuration_icon_read(tmp_path):
    config = __get_config_file(tmp_path)
    assert config.icon == "test.png"


def test_configuration_width_read(tmp_path):
    config = __get_config_file(tmp_path)
    assert config.width == 500


def test_configuration_height_read(tmp_path):
    config = __get_config_file(tmp_path)
    assert config.height == 500


def test_configuration_theme_read(tmp_path):
    config = __get_config_file(tmp_path)
    assert config.theme == "light"


def test_configuration_version_read(tmp_path):
    config = __get_config_file(tmp_path)
    assert config.version == "1.0.0"


def test_configuration_log_level_read(tmp_path):
    config = __get_config_file(tmp_path)
    assert config.log_level == "DEBUG"


def test_configuration_log_file_read(tmp_path):
    config = __get_config_file(tmp_path)
    assert config.log_file == "test.log"


def test_configuration_log_format_read(tmp_path):
    config = __get_config_file(tmp_path)
    assert config.log_format == "format"


def __get_config_file(tmp_path):
    config_file = tmp_path / "config.ini"
    config_file.write_text(configs)
    return Configuration(path=config_file)
