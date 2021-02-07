from GUI import (
    LogIn,
    SignUp,
    CourseList,
    CourseDetails,
    InstructorDetails,
    AddCourse,
    PurchaseCourse,
)
from Database import Users, Instructors, Courses, Transactions, DbHelper
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

dbHelper = DbHelper.DbHelper()
users = Users.Users(dbHelper)
instructors = Instructors.Instructors(dbHelper)
courses = Courses.Courses(dbHelper)
transactions = Transactions.Transactions(dbHelper)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.logInUI = LogIn.Ui_MainWindow()
        self.signUpUI = SignUp.Ui_MainWindow()
        self.coursesUI = CourseList.Ui_MainWindow()
        self.courseDetailsUI = CourseDetails.Ui_MainWindow()
        self.instructorDetailsUI = InstructorDetails.Ui_MainWindow()
        self.purchaseCourseUI = PurchaseCourse.Ui_MainWindow()
        self.addCourseUI = AddCourse.Ui_MainWindow()
        self.setMenuBar()
        self.logOut()

    def setupLogInUI(self):
        self.logInUI.setupUi(self)

        self.backAct.setDisabled(True)
        self.userMenu.setDisabled(True)
        self.coursesMenu.setDisabled(True)

        self.logInUI.logInButton.clicked.connect(self.logIn)
        self.logInUI.registerButton.clicked.connect(self.setupSignUpUI)

    def setupSignUpUI(self):
        self.signUpUI.setupUi(self)

        self.backAct.triggered.connect(self.setupLogInUI)
        self.backAct.setDisabled(False)
        self.userMenu.setDisabled(True)
        self.coursesMenu.setDisabled(True)

        self.signUpUI.signUpPushButton.clicked.connect(self.signUp)
        self.signUpUI.instructorForm.setVisible(False)
        self.signUpUI.instructorCheckBox.stateChanged.connect(
            lambda: self.signUpUI.instructorForm.setVisible(
                self.signUpUI.instructorCheckBox.isChecked()
            )
        )

    def setupProfileUI(self):
        self.signUpUI.setupUi(self)

        self.backAct.triggered.connect(self.setupCourseUI)
        self.backAct.setDisabled(False)
        self.userMenu.setDisabled(False)

        self.signUpUI.signUpPushButton.setText("Update Details")
        self.signUpUI.signUpPushButton.clicked.connect(self.updateUser)

        self.signUpUI.deletePushButton = QtWidgets.QPushButton(self.signUpUI.button)
        self.signUpUI.deletePushButton.setMinimumSize(QtCore.QSize(150, 60))
        self.signUpUI.deletePushButton.setText("Delete Account")
        self.signUpUI.deletePushButton.clicked.connect(lambda: self.deleteUser())
        self.signUpUI.buttonLayout.addWidget(
            self.signUpUI.deletePushButton, 0, QtCore.Qt.AlignHCenter
        )

        self.signUpUI.fullNameLineEdit.setText(self.user["FullName"])
        self.signUpUI.usernameLineEdit.setText(self.user["UserName"])
        self.signUpUI.emailLineEdit.setText(self.user["Email"])
        self.signUpUI.label_3.setVisible(False)
        self.signUpUI.passwordLineEdit.setVisible(False)
        self.signUpUI.label_4.setVisible(False)
        self.signUpUI.confirmLineEdit.setVisible(False)
        self.signUpUI.instructorCheckBox.setVisible(False)
        self.signUpUI.instructorForm.setVisible(self.instructor)

        if self.instructor:
            self.signUpUI.jobLineEdit.setText(self.user["JobDesc"])
            self.signUpUI.universityLineEdit.setText(self.user["University"])
            self.signUpUI.bioTextEdit.setPlainText(self.user["Bio"])

    def setupSortCoursesUI(self, table):
        sortFields = ["None", "CourseName", "Difficulty", "Fees"]
        sortTypes = ["ASC", "DESC"]

        sortField = self.coursesUI.comboBox.currentIndex()
        sortType = self.coursesUI.comboBox_2.currentIndex()

        sortQuery = sortFields[sortField] + " " + sortTypes[sortType]
        sortedCourses = courses.search_courses(sort_by=sortQuery)[0]
        sortedCourses = [i for i in sortedCourses if i in table]

        self.setupSearchCoursesUI(sortedCourses, sortField, sortType)

    def setupSearchCoursesUI(self, table, sortField=0, sortType=0):
        self.coursesUI.setupUi(self, table)

        self.backAct.setDisabled(False)
        self.backAct.triggered.connect(self.setupCourseUI)
        self.userMenu.setDisabled(False)

        self.coursesUI.comboBox.setCurrentIndex(sortField)
        self.coursesUI.comboBox_2.setCurrentIndex(sortType)

        self.coursesUI.titleLabel.setText('Search Results')

        self.coursesUI.searchButton.clicked.connect(
            lambda: self.setupSearchCoursesUI(
                courses.search_courses(
                    course_name=self.coursesUI.searchLineEdit.text().strip().lower()
                )[0]
            )
        )

        self.coursesUI.coursesList.itemClicked.connect(self.setupCourseDetailsUI)

        self.coursesUI.comboBox.currentIndexChanged.connect(
            lambda: self.setupSortCoursesUI(table)
        )
        self.coursesUI.comboBox_2.currentIndexChanged.connect(
            lambda: self.setupSortCoursesUI(table)
        )

    def setupCourseUI(self):
        courses_, message = courses.search_courses()
        if courses_ == False:
            self.showAlert(message)
            return
        self.coursesUI.setupUi(self, courses_)

        self.backAct.setDisabled(True)
        self.userMenu.setDisabled(False)
        self.coursesMenu.setDisabled(not self.instructor)

        self.coursesUI.titleLabel.setText("All Courses")

        self.coursesUI.searchButton.clicked.connect(
            lambda: self.setupSearchCoursesUI(
                courses.search_courses(
                    course_name=self.coursesUI.searchLineEdit.text().strip().lower()
                )[0]
            )
        )

        self.coursesUI.coursesList.itemClicked.connect(self.setupCourseDetailsUI)

        self.coursesUI.comboBox.currentIndexChanged.connect(
            lambda: self.setupSortCoursesUI(courses_)
        )
        self.coursesUI.comboBox_2.currentIndexChanged.connect(
            lambda: self.setupSortCoursesUI(courses_)
        )

    def setupPurchasedCourseUI(self):
        purchasedCourses, message = transactions.get_transactions(self.user["UserID"])
        if purchasedCourses == False:
            self.showAlert(message)
            return
        courseIDs = [i["CourseID"] for i in purchasedCourses]
        if len(courseIDs) == 1:
            courseIDs = courseIDs[0]
        if not courseIDs:
            courseIDs = -1
        purchasedCourses = courses.search_courses(course_id=courseIDs)[0]
        self.coursesUI.setupUi(self, purchasedCourses)

        self.backAct.setDisabled(False)
        self.backAct.triggered.connect(self.setupCourseUI)
        self.userMenu.setDisabled(False)

        self.coursesUI.titleLabel.setText("My Courses")

        self.coursesUI.searchButton.clicked.connect(
            lambda: self.setupSearchCoursesUI(
                courses.search_courses(
                    course_id=courseIDs,
                    course_name=self.coursesUI.searchLineEdit.text().strip().lower(),
                )[0]
            )
        )

        self.coursesUI.coursesList.itemClicked.connect(
            self.setupPurchasedCourseDetailsUI
        )

        self.coursesUI.comboBox.currentIndexChanged.connect(
            lambda: self.setupSortCoursesUI(purchasedCourses)
        )
        self.coursesUI.comboBox_2.currentIndexChanged.connect(
            lambda: self.setupSortCoursesUI(purchasedCourses)
        )

    def setupPurchasedCourseDetailsUI(self, item):
        self.setCourse(item)
        self.courseDetailsUI.setupUi(self)
        self.courseDetailsUI.retranslateUi(self, self.course)
        self.backAct.setDisabled(False)
        self.backAct.triggered.connect(self.setupCourseUI)
        self.courseDetailsUI.purchaseButton.setText("Go to Course")
        self.courseDetailsUI.purchaseButton.clicked.connect(self.setupBrowser)
        self.courseDetailsUI.instructorLabel.mousePressEvent = (
            self.setupInstructorDetailsUI
        )

    def setupCourseDetailsUI(self, item):
        self.setCourse(item)
        self.courseDetailsUI.setupUi(self)
        self.courseDetailsUI.retranslateUi(self, self.course)
        self.backAct.setDisabled(False)
        self.backAct.triggered.connect(self.setupCourseUI)
        self.courseDetailsUI.purchaseButton.clicked.connect(self.setupPurchaseCourseUI)
        if self.instructor:
            self.courseDetailsUI.purchaseButton.setVisible(False)
        self.courseDetailsUI.instructorLabel.mousePressEvent = (
            self.setupInstructorDetailsUI
        )

    def setupPurchaseCourseUI(self):
        self.purchaseCourseUI.setupUi(self, self.course)
        self.backAct.setDisabled(False)
        self.backAct.triggered.connect(self.setupCourseUI)
        self.purchaseCourseUI.purchaseButton.clicked.connect(self.purchaseCourse)
        if self.instructor:
            self.courseDetailsUI.purchaseButton.setVisible(False)

    def setupInstructorDetailsUI(self, *args):
        i = instructors.get_instructor(self.course["UserID"])
        i["FullName"] = self.course["FullName"]
        self.instructorDetailsUI.setupUi(self)
        self.instructorDetailsUI.retranslateUi(self, i)
        self.backAct.setDisabled(False)
        self.backAct.triggered.connect(self.setupCourseUI)

    def setupAddCourseUI(self, course=None):
        self.addCourseUI.setupUi(self)

        self.backAct.setDisabled(False)
        self.backAct.triggered.connect(self.setupCourseUI)

        if course:
            self.setCourse(course)
            self.addCourseUI.addCoursePushButton.setText("Update Course Details")
            self.addCourseUI.addCoursePushButton.clicked.connect(
                lambda: self.addCourse(True)
            )

            self.addCourseUI.deletePushButton = QtWidgets.QPushButton(
                self.addCourseUI.scrollAreaWidgetContents
            )
            self.addCourseUI.deletePushButton.setText("Delete Course")
            self.addCourseUI.deletePushButton.clicked.connect(self.deleteCourse)
            self.addCourseUI.verticalLayout_2.addWidget(
                self.addCourseUI.deletePushButton
            )

            self.addCourseUI.courseNameLineEdit.setText(self.course["CourseName"])
            self.addCourseUI.descTextEdit.setPlainText(self.course["Description"])
            self.addCourseUI.durationLineEdit.setText(
                self.course["Duration"].split()[0]
            )
            self.addCourseUI.feesLineEdit.setText(str(self.course["Fees"]))
            self.addCourseUI.durationComboBox.setCurrentText(
                self.course["Duration"].split()[1]
            )
            self.addCourseUI.difficultyComboBox.setCurrentIndex(
                self.course["Difficulty"]
            )
            self.addCourseUI.linkLineEdit.setText(self.course["CourseLink"])
        else:
            self.addCourseUI.addCoursePushButton.clicked.connect(self.addCourse)

    def setupEditCourseUI(self):
        courses_, message = courses.search_courses(user_id=self.user["UserID"])
        if courses_ == False:
            self.showAlert(message)
            return
        self.coursesUI.setupUi(self, courses_)

        self.backAct.setDisabled(False)
        self.backAct.triggered.connect(self.setupCourseUI)

        self.coursesUI.titleLabel.setText(self.user["FullName"] + "'s Courses")

        self.coursesUI.searchButton.clicked.connect(
            lambda: self.setupSearchCoursesUI(
                courses.search_courses(
                    user_id=self.user["UserID"],
                    course_name=self.coursesUI.searchLineEdit.text().strip().lower(),
                )[0]
            )
        )
        self.coursesUI.coursesList.itemClicked.connect(self.setupAddCourseUI)

        self.coursesUI.comboBox.currentIndexChanged.connect(
            lambda: self.setupSortCoursesUI(courses_)
        )
        self.coursesUI.comboBox_2.currentIndexChanged.connect(
            lambda: self.setupSortCoursesUI(courses_)
        )

    def setupBrowser(self):
        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.browser.setUrl(QtCore.QUrl(self.course["CourseLink"]))
        self.setCentralWidget(self.browser)

        self.backAct.setDisabled(False)
        self.backAct.triggered.connect(self.setupCourseUI)

    def setMenuBar(self):
        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        self.backAct = self.action(menubar, "&Back", self.setupLogInUI)

        self.userMenu = menubar.addMenu("User")
        self.action(
            self.userMenu, "Profile", self.setupProfileUI, "Ctrl+P", "View your profile"
        )
        self.action(
            self.userMenu,
            "My Courses",
            self.setupPurchasedCourseUI,
            tip="View all your purchased courses",
        )
        self.action(
            self.userMenu, "Log Out", self.logOut, "Ctrl+L", "Log out from your account"
        )

        self.coursesMenu = menubar.addMenu("Courses")
        self.action(
            self.coursesMenu, "Add Course", self.setupAddCourseUI, tip="Add a course"
        )
        self.action(
            self.coursesMenu,
            "Edit Course",
            self.setupEditCourseUI,
            tip="Edit and delete your courses",
        )

    def showAlert(self, text, condition=False):
        alert = QtWidgets.QMessageBox(self)
        alert.setObjectName("alert")
        alert.setStyleSheet("QMessageBox QPushButton{min-width:60px;min-height:30px}")
        alert.setIcon(QtWidgets.QMessageBox.Warning)
        if condition:
            alert.setWindowTitle("Delete")
            response = alert.question(self, "", text, alert.Yes | alert.No)
            return alert, response
        alert.setWindowTitle("Error")
        alert.setText(text)
        if "success" in text.lower():
            alert.setWindowTitle("Success")
            alert.setIcon(QtWidgets.QMessageBox.Information)
        alert.exec_()
        return alert

    def action(self, menu, text, command, shortcut="", tip=""):
        action = QtWidgets.QAction(text, self)
        if shortcut:
            action.setShortcut(shortcut)
        if tip:
            action.setStatusTip(tip)
        action.triggered.connect(command)
        menu.addAction(action)
        return action

    def logIn(self):
        username = self.logInUI.usernameLineEdit.text().strip().lower()
        password = self.logInUI.passwordLineEdit.text().strip()
        e, message = users.login(username, password)
        self.showAlert(message)
        if not e:
            return
        self.user = e
        self.instructor = True if self.user["IsInstructor"] else False
        if self.instructor:
            self.user.update(instructors.get_instructor(self.user["UserID"]))
        self.setupCourseUI()

    def signUp(self):
        name = self.signUpUI.fullNameLineEdit.text().strip().title()
        username = self.signUpUI.usernameLineEdit.text().strip().lower()
        email = self.signUpUI.emailLineEdit.text().strip().lower()
        isInstructor = 1 if self.signUpUI.instructorCheckBox.isChecked() else 0
        password = self.signUpUI.passwordLineEdit.text()
        confirm = self.signUpUI.confirmLineEdit.text()
        e, message = users.register(
            name, username, email, password, confirm, isInstructor
        )
        if not e:
            self.showAlert(message)
            return
        userId = e

        if self.signUpUI.instructorCheckBox.isChecked() or self.instructor:
            job = self.signUpUI.jobLineEdit.text().strip().title()
            uni = self.signUpUI.universityLineEdit.text().strip().title()
            bio = self.signUpUI.bioTextEdit.toPlainText().strip()
            bio[0].upper()
            e, message = instructors.register(userId, job, uni, bio)
            if not e:
                self.showAlert(message)
                users.delete_user(userId)
                return
        self.showAlert(message)
        self.setupLogInUI()

    def updateUser(self):
        name = self.signUpUI.fullNameLineEdit.text().strip().title()
        username = self.signUpUI.usernameLineEdit.text().strip().lower()
        email = self.signUpUI.emailLineEdit.text().strip().lower()
        e, message = users.update_user(self.user["UserID"], name, username, email)
        if not e:
            self.showAlert(message)
            return
        userId = e

        if self.signUpUI.instructorCheckBox.isChecked() or self.instructor:
            job = self.signUpUI.jobLineEdit.text().strip().title()
            uni = self.signUpUI.universityLineEdit.text().strip().title()
            bio = self.signUpUI.bioTextEdit.toPlainText().strip()
            bio[0].upper()
            e, message = instructors.update_instructor(userId, job, uni, bio)
            if not e:
                self.showAlert(message)
                return
        self.user = users.get_user(userId)[0]
        self.instructor = True if self.user["IsInstructor"] else False
        if self.instructor:
            self.user.update(instructors.get_instructor(self.user["UserID"]))
        self.showAlert(message)
        self.setupCourseUI()

    def deleteUser(self):
        alert, response = self.showAlert(
            "Are you sure you want to delete your account?", True
        )
        if response == alert.No:
            return
        if self.instructor:
            for course in courses.search_courses(user_id=self.user["UserID"])[0]:
                courses.delete_course(course["CourseID"])
            e, message = instructors.delete_instructor(self.user["UserID"])
            if not e:
                self.showAlert(message)
                return
        for transaction in transactions.get_transactions(self.user["UserID"])[0]:
            transactions.remove_transaction(transaction["TransID"])
        e, message = users.delete_user(self.user["UserID"])
        self.showAlert(message)
        if e:
            self.logOut()

    def logOut(self):
        self.user = None
        self.instructor = False
        self.setupLogInUI()

    def setCourse(self, item):
        self.course = self.coursesUI.coursesList.itemWidget(item).row
        self.course["Instructor"] = users.get_user(self.course["UserID"])[0]["FullName"]

    def addCourse(self, edit=False):
        courseName = self.addCourseUI.courseNameLineEdit.text().strip().title()
        description = self.addCourseUI.descTextEdit.toPlainText().strip()
        description[0].upper()
        duration = (
            str(self.addCourseUI.durationLineEdit.text())
            + " "
            + str(self.addCourseUI.durationComboBox.currentText())
        )
        fees = self.addCourseUI.feesLineEdit.text()
        difficulty = str(self.addCourseUI.difficultyComboBox.currentIndex())
        link = self.addCourseUI.linkLineEdit.text().lower().strip()
        if edit:
            e, message = courses.update_course(
                self.course["CourseID"],
                courseName,
                description,
                difficulty,
                fees,
                duration,
                link,
            )
        else:
            e, message = courses.add_course(
                self.user["UserID"],
                courseName,
                description,
                difficulty,
                fees,
                duration,
                link,
            )
        self.showAlert(message)
        if e:
            self.setupCourseUI()

    def deleteCourse(self):
        alert, response = self.showAlert(
            "Are you sure you want to delete this course?", True
        )
        if response == alert.No:
            return
        for transaction in transactions.get_transactions(
            course_id=self.course["CourseID"]
        )[0]:
            transactions.remove_transaction(transaction["TransID"])
        e, message = courses.delete_course(self.course["CourseID"])
        self.showAlert(message)
        if e:
            self.setupCourseUI()

    def purchaseCourse(self):
        if (
            len(
                transactions.get_transactions(
                    self.user["UserID"], self.course["CourseID"]
                )[0]
            )
            > 0
        ):
            self.showAlert("Course already purchased.")
            return
        e, message = transactions.add_transaction(
            self.user["UserID"], self.course["CourseID"]
        )
        table, message = transactions.get_transactions(
            self.user["UserID"], self.course["CourseID"]
        )
        if not table:
            self.showAlert(message)
            return
        self.generateReceipt(table[0])
        if "Success" in message:
            message = "Successfully purchased!"
        self.showAlert(message)
        self.setupCourseUI()

    def generateReceipt(self, table):
        fees = "$" + str(self.course["Fees"]) + ".00"
        line = "\n" + "-" * 100

        receipt = line[1:]
        receipt += "\n{:^100s}".format("COURSE CENTRAL")
        receipt += line
        receipt += "\n{:<100s}".format("PURCHASED BY")
        receipt += "\n{:<20s}{:<80s}".format("Username:", self.user["UserName"])
        receipt += "\n{:<20s}{:<80s}".format("Name:", self.user["FullName"])
        receipt += "\n{:<20s}{:<80s}".format("Email:", self.user["Email"])
        receipt += line
        receipt += "\n{:<50s}{:>50s}".format(
            "Order No.: " + str(table["TransID"]),
            "Date of Purchase: " + str(table["DOPurchase"]),
        )
        receipt += line
        receipt += "\n{:<85s}{:<10s}{:<5s}".format("PRODUCT DETAILS", "PRICE", "QTY")
        receipt += line
        receipt += "\n{:<85s}{:<10s}{:<5s}".format(self.course["CourseName"], fees, "1")
        receipt += "\n{:<85s}".format("ID: " + str(self.course["CourseID"]))
        receipt += "\n{:<85s}".format("Instructor: " + self.course["Instructor"])
        receipt += line
        receipt += "\n{:<85s}{:<15s}".format("TOTAL", fees)
        receipt += line
        receipt += "\n{:^100s}".format("Thank you for your purchase!")
        receipt += "\n{:^100s}".format("Questions about this payment? Contact us.")
        receipt += "\n{:^100s}".format("www.coursecentral.com")
        receipt += line

        fname = "receipt" + str(table["TransID"]) + ".txt"
        with open(fname, "w") as f:
            f.write(receipt)


if hasattr(QtCore.Qt, "AA_EnableHighDpiScaling"):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, "AA_UseHighDpiPixmaps"):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

try:
    from PyQt5.QtWinExtras import QtWin

    myappid = "alstondmello.coursecentral.1"
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(open("stylesheet.txt").read())
app.setWindowIcon(QtGui.QIcon("icon.ico"))
mainWindow = MainWindow()
mainWindow.showMaximized()
sys.exit(app.exec_())