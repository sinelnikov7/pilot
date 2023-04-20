import datetime
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5 import QtWidgets

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.username = QtWidgets.QLineEdit(self)
        self.password = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.username.setPlaceholderText('Логин')
        self.password.setPlaceholderText('Пароль')
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):

        response = requests.post('http://127.0.0.1:8080/api-token-auth/',
                                 data={"username": self.username.text(), "password": self.password.text()})
        if response.status_code == 200:
            self.token = response.json().get('token')
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Ошибка', 'Неправильный логин или пароль')


class Window(QMainWindow):

    def __init__(self, login):
        super().__init__()
        self.setWindowTitle("Python ")
        self.w_width = 500
        self.w_height = 500
        self.setGeometry(100, 100, self.w_width, self.w_height)
        self.UiComponents()
        self.show()
        self.speed = 15
        self.token = login.token

    def UiComponents(self):
        self.label = QLabel(self)
        self.l_width = 40
        self.l_height = 40
        self.label.setGeometry(200, 200, self.l_width, self.l_height)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid darkgreen;"
                                 "background : lightgreen;"
                                 "}")


    def keyPressEvent(self, event):

        x = self.label.x()
        y = self.label.y()
        if event.key() == Qt.Key_Up:
            if y > 0:
                self.label.move(x, y - self.speed)
        elif event.key() == Qt.Key_Down:
            if y < self.w_height - self.l_height:
                self.label.move(x, y + self.speed)
        elif event.key() == Qt.Key_Left:
            if x > 0:
                self.label.move(x - self.speed, y)
        elif event.key() == Qt.Key_Right:
            if x < self.w_width - self.l_width:
                self.label.move(x + self.speed, y)
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(x, y)
        print(self.token)
        print(self.time)
        requests.post('http://127.0.0.1:8080/create_step/',
                      data={"x": x, "y": y, "token": self.token, "time": self.time})



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = Window(login)
        window.show()
        print('!!!!!')
        sys.exit(app.exec_())