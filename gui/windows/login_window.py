from PySide6 import QtGui
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QLineEdit, QMessageBox

from config.configuration import Configuration
from gui.main import MainWindow
from repositories.operator_repository import OperatorRepository
from services.log_service import LogService


class LoginWindow:
    def __init__(self):
        self.logger = LogService.get_logger(__name__)

        loader = QUiLoader()
        file = QFile("./gui/ui/LoginWindow.ui")
        file.open(QFile.ReadOnly)
        self.window = loader.load(file)
        file.close()

        password_line_edit = self.window.passwordText
        password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_visible = False

        # only for debug the application
        self.window.emailText.setText("admin@gmail.com")
        self.window.passwordText.setText("asdasd123")

        self.window.loginBtn.clicked.connect(lambda: self.__login())
        self.window.show_hideBtn.clicked.connect(lambda: self.__show_hide_password())

    def show(self):
        self.logger.debug("Showing Login Window")
        self.window.show()

    def __login(self):
        email = self.window.emailText.text()
        password = self.window.passwordText.text()
        operator = OperatorRepository.get_operator_by_email_and_password(email, password)
        if operator is None:
            self.__credential_error()
        else:
            self.logger.info(f"User {email} logged successfully")
            self.window.close()
            MainWindow()

    def __credential_error(self):
        self.logger.info("Login credentials error")
        dialog = QMessageBox()
        icon = Configuration().icon
        dialog.setWindowIcon(QtGui.QIcon(icon))
        dialog.setWindowTitle("Login Error")
        dialog.setText("Email or Password are not correct")
        dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        dialog.setIcon(QMessageBox.Icon.Critical)
        dialog.exec()

    def __show_hide_password(self):
        password_line_edit = self.window.passwordText
        if self.password_visible:
            password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        else:
            password_line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.password_visible = not self.password_visible
