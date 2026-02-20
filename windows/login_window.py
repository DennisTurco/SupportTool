from PySide6 import QtGui
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QLineEdit, QMessageBox

from repositories.operator_repository import OperatorRepository


class LoginWindow:
    def __init__(self):
        loader = QUiLoader()

        file = QFile("./ui/LoginWindow.ui")
        file.open(QFile.ReadOnly)

        self.window = loader.load(file)
        file.close()

        password_line_edit = self.window.passwordText
        password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

        self.password_visible = False

        self.window.loginBtn.clicked.connect(lambda: self.login())

        self.window.show_hideBtn.clicked.connect(lambda: self.show_hide_password())

    def show(self):
        self.window.show()

    def login(self):
        email = self.window.emailText.text()
        password = self.window.passwordText.text()
        operator = OperatorRepository.get_operator_by_email_and_password(email, password)
        if operator is None:
            self.credential_error()
        else:
            QApplication.instance().quit()

    def credential_error(self):
        dialog = QMessageBox()
        dialog.setWindowIcon(QtGui.QIcon("./imgs/icon.png"))
        dialog.setWindowTitle("Login Error")
        dialog.setText("Email or Password are not correct")
        dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        dialog.setIcon(QMessageBox.Icon.Critical)

        dialog.exec()

    def show_hide_password(self):
        password_line_edit = self.window.passwordText
        if not self.password_visible:
            password_line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
            self.password_visible = True
        else:
            password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
            self.password_visible = False
