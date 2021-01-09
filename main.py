from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3


# Класс который перекидывает в главный класс, регистрационный
class UiLoginWindow(object):
    # Дизайн UX и UI
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(333, 307)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usernameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameEdit.setGeometry(QtCore.QRect(10, 10, 311, 41))
        self.usernameEdit.setObjectName("usernameEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordEdit.setGeometry(QtCore.QRect(10, 80, 311, 41))
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.RegisterBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterBtn.setGeometry(QtCore.QRect(4, 150, 323, 131))
        self.RegisterBtn.setObjectName("RegisterBtn")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        self.RegisterBtn.clicked.connect(self.Login)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("RegisterWindow", "Register"))
        self.usernameEdit.setPlaceholderText(_translate("LoginWindow",
                                                        "Username"))
        self.passwordEdit.setPlaceholderText(_translate("LoginWindow",
                                                        "Password"))
        self.RegisterBtn.setText(_translate("LoginWindow", "Login"))

    # Функция перекидывающая пользователя в главный класс
    def Main_Open(self):
        self.Main_Window = QtWidgets.QMainWindow()
        self.Main_Window_Ui = UiMainWindow()
        self.Main_Window_Ui.setupUi(self.Main_Window)
        self.username = self.usernameEdit.text()
        self.Main_Window.show()

    # Функция перекидывающая пользователя в класс информирующий об ошибке
    def Error_Open(self):
        self.Error_Window = QtWidgets.QMainWindow()
        self.Error_Window_Ui = UiErrorWindow()
        self.Error_Window_Ui.setupUi(self.Error_Window)
        self.Error_Window.show()

    # Функция проверки нахождения пользователя в базе данных
    def Login(self):
        self.username = self.usernameEdit.text()
        self.password = self.passwordEdit.text()
        self.connect = sqlite3.connect('db.db')
        self.current = self.connect.cursor()
        print("Connected to SQLite")
        # Проверка на наличие пользователя в БД
        self.request = ('SELECT * FROM user WHERE name="%s" '
                        'and password="%s"' % (self.username, self.password))

        self.current.execute(self.request)
        if self.current.fetchone() is not None:
            self.Main_Open()
        else:
            self.Error_Open()


# Главный класс с показом списка задач и кнопками добавления, удаления задач
class UiMainWindow(object):
    # Список задач
    def Show_Data(self):
        self.connect = sqlite3.connect("db.db")
        self.request = 'SELECT * FROM user'
        self.result = self.connect.execute(self.request)
        self.listWidget.setRowCount(0)
        for self.row_num, self.row_data in enumerate(self.result):
            self.listWidget.insertRow(self.row_num)
            for self.col_num, self.data in enumerate(self.row_data):
                self.listWidget.setItem(self.row_num,
                                        self.col_num,
                                        QtWidgets.QTableWidgetItem(str
                                                                   (self.data)
                                                                   ))

    # Дизайн UX и UI
    def setupUi(self, Main_Window):
        Main_Window.setObjectName("Main_Window")
        Main_Window.resize(564, 707)
        self.centralwidget = QtWidgets.QWidget(Main_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(4, 70, 283, 61))
        self.addBtn.setObjectName("addBtn")
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QtCore.QRect(285, 70, 273, 61))
        self.deleteBtn.setObjectName("deleteBtn")
        self.updateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.updateBtn.setGeometry(QtCore.QRect(4, 10, 553, 61))
        self.updateBtn.setObjectName("updateBtn")
        self.listWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(11, 134, 542, 561))
        self.listWidget.setRowCount(20)
        self.listWidget.setColumnCount(5)
        self.listWidget.setObjectName("listWidget")
        Main_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)
        self.updateBtn.clicked.connect(self.Show_Data)

        self.addBtn.clicked.connect(self.Add)
        self.deleteBtn.clicked.connect(self.Delete)

    def retranslateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("Main_Window", "TO DO"))
        self.addBtn.setText(_translate("Main_Window", "Add"))
        self.deleteBtn.setText(_translate("Main_Window", "Delete"))
        self.updateBtn.setText(_translate("Main_Window", "Update"))

    # Функция перекидывающая пользователя в класс
    # добавляющий задачу в базу данных
    def Add(self):
        self.Add_Window = QtWidgets.QMainWindow()
        self.Add_Window_Ui = UiAddWindow()
        self.Add_Window_Ui.setupUi(self.Add_Window)
        self.Add_Window.show()

    # Функция перекидывающая пользователя в класс
    # удаляющий задачу из базы данных
    def Delete(self):
        self.Delete_Window = QtWidgets.QMainWindow()
        self.Delete_Window_Ui = UiDeleteWindow()
        self.Delete_Window_Ui.setupUi(self.Delete_Window)
        self.Delete_Window.show()


# Класс информирующий пользователя об ошибке


class UiErrorWindow(object):
    # Дизайн UX и UI
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.okBtn = QtWidgets.QPushButton(self.centralwidget)
        self.okBtn.setGeometry(QtCore.QRect(10, 140, 301, 51))
        self.okBtn.setObjectName("okBtn")
        self.okBtn.clicked.connect(QtWidgets.qApp.quit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.okBtn.setText(_translate("MainWindow", "OKAY"))
        self.label.setText(_translate("MainWindow", "Error"))


# Класс добавляющий задачу в базу данных


class UiAddWindow(object):
    # Дизайн UX и UI
    def setupUi(self, Add_Window):
        Add_Window.setObjectName("Add_Window")
        Add_Window.resize(351, 244)
        self.centralwidget = QtWidgets.QWidget(Add_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.addText = QtWidgets.QLineEdit(self.centralwidget)
        self.addText.setGeometry(QtCore.QRect(15, 20, 321, 41))
        self.addText.setObjectName("addText")
        self.addText2 = QtWidgets.QLineEdit(self.centralwidget)
        self.addText2.setGeometry(QtCore.QRect(15, 75, 321, 41))
        self.addText2.setObjectName("addText2")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(35, 150, 281, 71))
        self.addBtn.setObjectName("addBtn")
        Add_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_Window)
        QtCore.QMetaObject.connectSlotsByName(Add_Window)

        self.addBtn.clicked.connect(self.Add)

    def retranslateUi(self, Add_Window):
        _translate = QtCore.QCoreApplication.translate
        Add_Window.setWindowTitle(_translate("Add_Window", "Add"))
        self.addText.setPlaceholderText(_translate("Add_Window", "New To Do"))
        self.addText2.setPlaceholderText(_translate("Add_Window",
                                                    "New Deadline"))
        self.addBtn.setText(_translate("Add_Window", "Add"))

    # Функция добавляющая задачу в базу данных
    def Add(self):
        self.add_text = self.addText.text()
        self.add_text2 = self.addText2.text()
        self.connect = sqlite3.connect('db.db')
        self.current = self.connect.cursor()
        self.request = ("INSERT INTO user(todo, date) VALUES('%s', '%s')"
                        % (''.join(self.add_text), (''.join(self.add_text2))))
        self.current.execute(self.request)
        self.connect.commit()
        if self.current.rowcount:
            print("Inserted")
        else:
            print("Error")


# Класс удаляющий задачу из базы данных


class UiDeleteWindow(object):
    # Список задач
    def Show_Data(self):
        self.connect = sqlite3.connect("db.db")
        self.request = 'SELECT * FROM user'
        self.result = self.connect.execute(self.request)
        self.tableWidget.setRowCount(0)
        for self.row_num, self.row_data in enumerate(self.result):
            self.tableWidget.insertRow(self.row_num)
            for self.col_num, self.data in enumerate(self.row_data):
                self.tableWidget.setItem(self.row_num,
                                         self.col_num,
                                         QtWidgets.QTableWidgetItem(str
                                                                    (self.data)
                                                                    ))

    # Дизайн UX и UI
    def setupUi(self, Delete_Window):
        Delete_Window.setObjectName("Delete_Window")
        Delete_Window.resize(565, 461)
        self.centralwidget = QtWidgets.QWidget(Delete_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(11, 10, 542, 271))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.numberEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numberEdit.setGeometry(QtCore.QRect(31, 295, 499, 51))
        self.numberEdit.setObjectName("numberEdit")
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QtCore.QRect(25, 375, 511, 71))
        self.deleteBtn.setObjectName("deleteBtn")
        Delete_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Delete_Window)
        QtCore.QMetaObject.connectSlotsByName(Delete_Window)

        self.Show_Data()

        self.deleteBtn.clicked.connect(self.Delete)

    def retranslateUi(self, Delete_Window):
        _translate = QtCore.QCoreApplication.translate
        Delete_Window.setWindowTitle(_translate("Delete_Window", "Delete"))
        self.numberEdit.setPlaceholderText(_translate("Delete_Window",
                                                      "Enter to Number"))
        self.deleteBtn.setText(_translate("Delete_Window", "Delete"))

    # Функция удаляющая задачу из базы данных
    def Delete(self):
        self.number = self.numberEdit.text()
        self.connect = sqlite3.connect("db.db")
        self.current = self.connect.cursor()
        self.request = ('DELETE FROM user WHERE id = "%s"' % self.number)
        self.current.execute(self.request)
        self.connect.commit()
        if self.current.rowcount:
            print("Deleted")


# Функция запускающая приложение
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Login_Window = QtWidgets.QMainWindow()
    ui = UiLoginWindow()
    ui.setupUi(Login_Window)
    # Запуск
    Login_Window.show()
    sys.exit(app.exec_())
