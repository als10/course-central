from PyQt5 import QtCore, QtGui, QtWidgets

difficulties = ["Beginner", "Intermediate", "Advanced"]


class CourseWidget(QtWidgets.QWidget):
    def __init__(self, row, parent=None):
        super(CourseWidget, self).__init__(parent)
        self.course = QtWidgets.QGridLayout(self)
        self.course.setContentsMargins(10, 10, 10, 10)
        self.course.setSpacing(15)
        self.course.setObjectName("course")

        self.line = QtWidgets.QFrame(self)
        self.line.setMinimumSize(QtCore.QSize(0, 2))
        self.line.setBaseSize(QtCore.QSize(0, 2))
        self.line.setAcceptDrops(False)
        self.line.setAutoFillBackground(False)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.course.addWidget(self.line, 6, 0, 1, 2)

        self.durationLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.durationLabel.setFont(font)
        self.durationLabel.setObjectName("durationLabel")
        self.course.addWidget(self.durationLabel, 3, 0, 1, 1)

        self.difficultyLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.difficultyLabel.setFont(font)
        self.difficultyLabel.setObjectName("difficultyLabel")
        self.course.addWidget(self.difficultyLabel, 3, 1, 1, 1)

        self.courseNameLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.courseNameLabel.setFont(font)
        self.courseNameLabel.setWordWrap(True)
        self.courseNameLabel.setObjectName("courseNameLabel")
        self.course.addWidget(self.courseNameLabel, 1, 0, 2, 2)

        self.setLayout(self.course)

        self.row = row

        self.setText(row["CourseName"], row["Difficulty"], '$' + str(row["Fees"]))

    def setText(self, courseName, difficulty, duration):
        self.courseNameLabel.setText(courseName)
        self.difficultyLabel.setText(difficulties[difficulty])
        self.durationLabel.setText(duration)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, table):
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 400))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_4.addWidget(self.titleLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.searchLineEdit.setFont(font)
        self.searchLineEdit.setText("")
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout.addWidget(self.searchLineEdit)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setSizePolicy(
            QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
            )
        )
        self.searchButton.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.horizontalLayout_2.setStretch(0, 70)
        self.horizontalLayout_2.setStretch(1, 10)
        self.horizontalLayout_2.setStretch(2, 20)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 809, 231))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.coursesList = QtWidgets.QListWidget(self.widget)
        self.coursesList.setObjectName("coursesList")
        self.verticalLayout_3.addWidget(self.coursesList)
        self.verticalLayout_2.addWidget(self.widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorLabel.sizePolicy().hasHeightForWidth())
        self.errorLabel.setSizePolicy(sizePolicy)
        self.errorLabel.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.errorLabel.setFont(font)
        self.errorLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.errorLabel.setObjectName("errorLabel")
        self.errorLabel.setContentsMargins(40, 40, 40, 40)
        self.verticalLayout_4.addWidget(self.errorLabel)

        if table == -1 or len(table) == 0:
            self.errorLabel.setVisible(True)
            self.scrollArea.setVisible(False)
        else:
            self.errorLabel.setVisible(False)
            for row in table:
                self.addItem(row)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Courses"))
        self.titleLabel.setText(_translate("MainWindow", "All Courses"))
        self.titleLabel.setAccessibleName("red")
        self.searchLineEdit.setPlaceholderText(
            _translate("MainWindow", "Search for courses...")
        )
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "SORT BY"))
        self.label_2.setAccessibleName("red")
        self.comboBox.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Name"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Difficulty"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Fees"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "ASC"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "DESC"))
        self.errorLabel.setText(_translate("MainWindow", "No Courses Found!"))

    def addItem(self, item):
        courseWidget = CourseWidget(item)
        listWidgetItem = QtWidgets.QListWidgetItem(self.coursesList)
        listWidgetItem.setSizeHint(courseWidget.sizeHint())
        self.coursesList.addItem(listWidgetItem)
        self.coursesList.setItemWidget(listWidgetItem, courseWidget)
