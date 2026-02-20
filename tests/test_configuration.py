from config.configuration import Configuration
from exceptions.exceptions import ConfigurationFileNotFound

configs = """
    [GUI]
    icon = test.png
    width = 100
    height = 100
    theme = dark
"""


def test_configuration_read(tmp_path):
    config_file = tmp_path / "config.ini"
    config_file.write_text(configs)

    config = Configuration(path=config_file)
    assert config.icon == "test.png"


def test_configuaration_file_path_error():
    try:
        Configuration(path="./not_valid_path/file/.ini")
        assert False
    except ConfigurationFileNotFound:
        assert True
