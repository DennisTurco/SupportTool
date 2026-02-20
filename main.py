from PySide6.QtWidgets import QApplication

from database.database_initializer import DatabaseInitializer
from gui.main import MainWindow

if __name__ == "__main__":
    DatabaseInitializer.init_database()

    app = QApplication()

    # login = LoginWindow()
    # login.show()

    MainWindow()

    app.exec()
