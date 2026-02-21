#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#

import json
import os


class Settings:
    json_file = "settings.json"
    app_path = os.path.abspath(os.getcwd())
    settings_path = os.path.normpath(os.path.join(app_path, json_file))
    if not os.path.isfile(settings_path):
        print(f'WARNING: "settings.json" not found! check in the folder {settings_path}')

    def __init__(self):
        super().__init__()

        self.items = {}
        self.deserialize()

    def serialize(self):
        with open(self.settings_path, "w", encoding="utf-8") as write:
            json.dump(self.items, write, indent=4)

    def deserialize(self):
        with open(self.settings_path, encoding="utf-8") as reader:
            settings = json.loads(reader.read())
            self.items = settings
