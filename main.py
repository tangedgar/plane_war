from PyQt5.QtWidgets import QToolTip

class FirsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("登录")
        self.textfield()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDsktowidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def textfield(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        user = QLabel("用户名(mingri):")
        self.userEdit = QLineEdit()
        self.userEdit.setToolTip("请输入您的账号")

        passWord = QLabel("密码(666666):")
        self.passWordEdit = QLineEdit()
        self.passWordEdit.setToolTip("请输入您的密码")

        grid = QGridLayout()
        grid.setSpacing(0)

        grid.addWidget(user, 0, 0)
        grid.addWidget(self.userEdit, 1, 0)
        grid.addWidget(passWord, 2, 0)
        grid.addWidget(self.passWordEdit, 3, 0)
        empty = QLabel()
        grid.addWidget(empty, 4, 0)
        btn_logon = QPushButton("登录")
        btn_quit = QPushButton("退出")
        grid.addWidget(btn_logon, 5, 0, 1, 2)
        grid.addWidget(btn_quit, 6, 0, 1, 2)

        btn_logon.clicked.connect(self.onclick)
        btn_quit.clicked.connect(quit)
        self.setLayout(grid)

    def onclick(self):
        if self.userEdit.text() == "mingri":
            if self.passWordEdit.text() == '666666':
                ex.close()
                MainWindow.show()
            else:
                self.passWordEdit.setText('密码错误请重新输入')
        else:
            self.userEdit.setText('账号错误请重新输入')
