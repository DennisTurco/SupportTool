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
from qt_core import QLabel, QPainter, QPixmap, Qt, QVBoxLayout, QWidget


class PyIcon(QWidget):
    def __init__(self, icon_path, icon_color):
        super().__init__()

        self._icon_path = icon_path
        self._icon_color = icon_color

        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.icon = QLabel()
        self.icon.setAlignment(Qt.AlignCenter)

        self.set_icon(self._icon_path, self._icon_color)

        self.layout.addWidget(self.icon)

    def set_icon(self, icon_path, icon_color=None):
        color = ""
        if icon_color is not None:
            color = icon_color
        else:
            color = self._icon_color

        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        painter.end()

        self.icon.setPixmap(icon)
