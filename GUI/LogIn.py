from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setSizeIncrement(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(13)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAccessibleName("")
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setAccessibleName("")
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(282, 0, 413, 592))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth()
        )
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setAccessibleName("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(-1, 30, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setProperty("type", "")
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.usernameLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.verticalLayout_4.addWidget(self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.frame)
        self.usernameLineEdit.setMinimumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setStyleSheet("")
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.verticalLayout_4.addWidget(self.usernameLineEdit)
        self.passwordLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.verticalLayout_4.addWidget(self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.frame)
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setStyleSheet("")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.verticalLayout_4.addWidget(self.passwordLineEdit)
        self.logInButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logInButton.sizePolicy().hasHeightForWidth())
        self.logInButton.setSizePolicy(sizePolicy)
        self.logInButton.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.logInButton.setFont(font)
        self.logInButton.setStyleSheet("")
        self.logInButton.setObjectName("logInButton")
        self.verticalLayout_4.addWidget(self.logInButton, 0, QtCore.Qt.AlignHCenter)
        self.separator = QtWidgets.QFrame(self.frame)
        self.separator.setWindowModality(QtCore.Qt.NonModal)
        self.separator.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.separator.sizePolicy().hasHeightForWidth())
        self.separator.setSizePolicy(sizePolicy)
        self.separator.setMinimumSize(QtCore.QSize(0, 2))
        self.separator.setSizeIncrement(QtCore.QSize(0, 2))
        self.separator.setBaseSize(QtCore.QSize(10, 2))
        self.separator.setFrameShape(QtWidgets.QFrame.HLine)
        self.separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separator.setObjectName("separator")
        self.verticalLayout_4.addWidget(self.separator)
        self.signUpLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.signUpLabel.setFont(font)
        self.signUpLabel.setObjectName("signUpLabel")
        self.verticalLayout_4.addWidget(self.signUpLabel)
        self.registerButton = QtWidgets.QPushButton(self.frame)
        self.registerButton.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("")
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout_4.addWidget(self.registerButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Log In"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.logInButton.setText(_translate("MainWindow", "Log in"))
        self.signUpLabel.setText(
            _translate("MainWindow", "Not an existing user? Join for free!")
        )
        self.registerButton.setText(_translate("MainWindow", "Sign up"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
