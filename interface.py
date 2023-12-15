from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap

import sys, pickle

class Ui_main(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(900, 424)

        self.pushButtonFilter = QtWidgets.QPushButton(Widget)
        self.pushButtonFilter.setGeometry(QtCore.QRect(690, 10, 31, 31))
        self.pushButtonFilter.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonFilter.setObjectName("pushButtonAdd")


        self.labelMain = QtWidgets.QLabel(Widget)
        self.labelMain.setGeometry(QtCore.QRect(20, 10, 350, 31))
        self.labelMain.setStyleSheet("font: 700 18pt \"Segoe UI\";\n"
"color: #000")
        self.labelMain.setObjectName("labelMain")
        self.pushButtonAdd = QtWidgets.QPushButton(Widget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(730, 50, 151, 41))
        self.pushButtonAdd.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonAdd.setObjectName("pushButtonAdd")

        self.pushButtonAdmin = QtWidgets.QPushButton(Widget)
        self.pushButtonAdmin.setGeometry(QtCore.QRect(730, 250, 151, 41))
        self.pushButtonAdmin.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonAdmin.setObjectName("pushButtonAdd")

        self.tableWidget = QtWidgets.QTableWidget(Widget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 711, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButtonChange = QtWidgets.QPushButton(Widget)
        self.pushButtonChange.setGeometry(QtCore.QRect(730, 100, 151, 41))
        self.pushButtonChange.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonChange.setObjectName("pushButtonChange")
        self.pushButtonDelete = QtWidgets.QPushButton(Widget)
        self.pushButtonDelete.setGeometry(QtCore.QRect(730, 150, 151, 41))
        self.pushButtonDelete.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.pushButtonCreate = QtWidgets.QPushButton(Widget)
        self.pushButtonCreate.setGeometry(QtCore.QRect(730, 200, 151, 41))
        self.pushButtonCreate.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.pushButtonExit = QtWidgets.QPushButton(Widget)
        self.pushButtonExit.setGeometry(QtCore.QRect(730, 360, 151, 41))
        self.pushButtonExit.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonExit.setObjectName("pushButtonExit")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.labelMain.setText(_translate("Widget", "Расписание самолетов"))
        self.pushButtonAdd.setText(_translate("Widget", "Добавить "))
        self.pushButtonAdmin.setText(_translate("Widget", "Город/Рейс"))
        self.pushButtonChange.setText(_translate("Widget", "Изменить "))
        self.pushButtonDelete.setText(_translate("Widget", "Удалить "))
        self.pushButtonCreate.setText(_translate("Widget", "Создать отчет"))
        self.pushButtonExit.setText(_translate("Widget", "Выйти "))


class Ui_add(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(990, 120)
        self.labelDate = QtWidgets.QLabel(Widget)
        self.labelDate.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.labelDate.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelDate.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDate.setObjectName("labelDate")

        self.labelPlace = QtWidgets.QLabel(Widget)
        self.labelPlace.setGeometry(QtCore.QRect(720, 20, 91, 31))
        self.labelPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelPlace.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPlace.setObjectName("labelPlace")

        self.spinBox = QtWidgets.QSpinBox(Widget)
        self.spinBox.setGeometry(QtCore.QRect(720, 60, 91, 41))
        self.spinBox.setObjectName("spinBox")

        self.pushButtonAdd = QtWidgets.QPushButton(Widget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(820, 60, 151, 41))
        self.pushButtonAdd.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonAdd.setObjectName("pushButtonAdd")

        self.pushButtonBack = QtWidgets.QPushButton(Widget)
        self.pushButtonBack.setGeometry(QtCore.QRect(820, 20, 151, 31))
        self.pushButtonBack.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonBack.setObjectName("pushButtonAdd")

        self.lineEditFromPlace = QtWidgets.QLineEdit(Widget)
        self.lineEditFromPlace.setGeometry(QtCore.QRect(210, 60, 171, 41))
        self.lineEditFromPlace.setObjectName("lineEditFromPlace")
        self.lineEditToPlace = QtWidgets.QLineEdit(Widget)
        self.lineEditToPlace.setGeometry(QtCore.QRect(380, 60, 171, 41))
        self.lineEditToPlace.setObjectName("lineEditToPlace")
        self.timeEdit = QtWidgets.QTimeEdit(Widget)
        self.timeEdit.setGeometry(QtCore.QRect(130, 60, 81, 41))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(Widget)
        self.dateEdit.setGeometry(QtCore.QRect(20, 60, 110, 41))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEditFlight = QtWidgets.QLineEdit(Widget)
        self.lineEditFlight.setGeometry(QtCore.QRect(550, 60, 171, 41))
        self.lineEditFlight.setObjectName("lineEditFlight")
        self.labelTime = QtWidgets.QLabel(Widget)
        self.labelTime.setGeometry(QtCore.QRect(130, 20, 81, 31))
        self.labelTime.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelTime.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTime.setObjectName("labelTime")
        self.labelToPlace = QtWidgets.QLabel(Widget)
        self.labelToPlace.setGeometry(QtCore.QRect(380, 20, 171, 31))
        self.labelToPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelToPlace.setAlignment(QtCore.Qt.AlignCenter)
        self.labelToPlace.setObjectName("labelToPlace")
        self.labelFromPlace = QtWidgets.QLabel(Widget)
        self.labelFromPlace.setGeometry(QtCore.QRect(210, 20, 171, 31))
        self.labelFromPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelFromPlace.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFromPlace.setObjectName("labelFromPlace")
        self.labelFlight = QtWidgets.QLabel(Widget)
        self.labelFlight.setGeometry(QtCore.QRect(550, 20, 171, 31))
        self.labelFlight.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelFlight.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFlight.setObjectName("labelFlight")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.labelDate.setText(_translate("Widget", "Дата вылета"))
        self.pushButtonAdd.setText(_translate("Widget", "Добавить"))
        self.pushButtonBack.setText(_translate("Widget", "Назад"))
        self.labelTime.setText(_translate("Widget", "Время"))
        self.labelToPlace.setText(_translate("Widget", "Пункт прибытия"))
        self.labelFromPlace.setText(_translate("Widget", "Пункт отправления"))
        self.labelFlight.setText(_translate("Widget", "Номер рейса"))
        self.labelPlace.setText(_translate("Widget", "Места"))



class Ui_report(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(420, 190)
        self.labelMain = QtWidgets.QLabel(Widget)
        self.labelMain.setGeometry(QtCore.QRect(10, 10, 401, 31))
        self.labelMain.setStyleSheet("font: 700 14pt \"Segoe UI\";\n"
"color: #000")
        self.labelMain.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMain.setObjectName("labelMain")
        self.pushButtonAdd = QtWidgets.QPushButton(Widget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(260, 130, 151, 41))
        self.pushButtonAdd.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonBack = QtWidgets.QPushButton(Widget)
        self.pushButtonBack.setGeometry(QtCore.QRect(260, 90, 151, 31))
        self.pushButtonBack.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonBack.setObjectName("pushButtonAdd_2")
        self.checkBoxDate = QtWidgets.QCheckBox(Widget)
        self.checkBoxDate.setGeometry(QtCore.QRect(20, 50, 141, 22))
        self.checkBoxDate.setObjectName("checkBoxDate")
        self.checkBoxTime = QtWidgets.QCheckBox(Widget)
        self.checkBoxTime.setGeometry(QtCore.QRect(20, 70, 141, 22))
        self.checkBoxTime.setObjectName("checkBoxTime")
        self.checkBoxFromPlace = QtWidgets.QCheckBox(Widget)
        self.checkBoxFromPlace.setGeometry(QtCore.QRect(20, 90, 141, 22))
        self.checkBoxFromPlace.setObjectName("checkBoxFromPlace")
        self.checkBoxToPlace = QtWidgets.QCheckBox(Widget)
        self.checkBoxToPlace.setGeometry(QtCore.QRect(20, 110, 141, 22))
        self.checkBoxToPlace.setObjectName("checkBoxToPlace")
        self.checkBoxFlight = QtWidgets.QCheckBox(Widget)
        self.checkBoxFlight.setGeometry(QtCore.QRect(20, 130, 141, 22))
        self.checkBoxFlight.setObjectName("checkBoxFlight")
        self.checkBoxFreePlace = QtWidgets.QCheckBox(Widget)
        self.checkBoxFreePlace.setGeometry(QtCore.QRect(20, 150, 141, 22))
        self.checkBoxFreePlace.setObjectName("checkBoxFreePlace")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.labelMain.setText(_translate("Widget", "Данные для отчета"))
        self.pushButtonAdd.setText(_translate("Widget", "Создать "))
        self.pushButtonBack.setText(_translate("Widget", "Назад "))
        self.checkBoxDate.setText(_translate("Widget", "Дата вылета"))
        self.checkBoxTime.setText(_translate("Widget", "Время вылета"))
        self.checkBoxFromPlace.setText(_translate("Widget", "Пункт отправления"))
        self.checkBoxToPlace.setText(_translate("Widget", "Пункт назначения"))
        self.checkBoxFlight.setText(_translate("Widget", "Рейс"))
        self.checkBoxFreePlace.setText(_translate("Widget", "Свободные места"))

class Ui_report2(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(885, 423)
        self.labelMain = QtWidgets.QLabel(Widget)
        self.labelMain.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.labelMain.setStyleSheet("font: 700 14pt \"Segoe UI\";\n"
"color: #000")
        self.labelMain.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMain.setObjectName("labelMain")
        self.pushButtonAdd = QtWidgets.QPushButton(Widget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(720, 370, 151, 41))
        self.pushButtonAdd.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonBack = QtWidgets.QPushButton(Widget)
        self.pushButtonBack.setGeometry(QtCore.QRect(720, 330, 151, 31))
        self.pushButtonBack.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonBack.setObjectName("pushButtonAdd_2")
        self.tableWidget = QtWidgets.QTableWidget(Widget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 691, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.labelMain.setText(_translate("Widget", "Данные для отчета"))
        self.pushButtonAdd.setText(_translate("Widget", "Сохранить "))
        self.pushButtonBack.setText(_translate("Widget", "Назад "))


class Ui_Filter(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(429, 291)
        self.labelDate = QtWidgets.QLabel(Widget)
        self.labelDate.setGeometry(QtCore.QRect(20, 80, 111, 31))
        self.labelDate.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelDate.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDate.setObjectName("labelDate")
        self.pushButtonFilter = QtWidgets.QPushButton(Widget)
        self.pushButtonFilter.setGeometry(QtCore.QRect(140, 230, 151, 41))
        self.pushButtonFilter.setStyleSheet("font:700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonFilter.setObjectName("pushButtonFilter")
        self.lineEditFromPlace = QtWidgets.QLineEdit(Widget)
        self.lineEditFromPlace.setGeometry(QtCore.QRect(20, 40, 131, 41))
        self.lineEditFromPlace.setObjectName("lineEditFromPlace")
        self.lineEditToPlace = QtWidgets.QLineEdit(Widget)
        self.lineEditToPlace.setGeometry(QtCore.QRect(150, 40, 131, 41))
        self.lineEditToPlace.setObjectName("lineEditToPlace")
        self.timeEdit = QtWidgets.QTimeEdit(Widget)
        self.timeEdit.setGeometry(QtCore.QRect(20, 180, 111, 41))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(Widget)
        self.dateEdit.setGeometry(QtCore.QRect(20, 110, 110, 41))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEditFlight = QtWidgets.QLineEdit(Widget)
        self.lineEditFlight.setGeometry(QtCore.QRect(280, 40, 131, 41))
        self.lineEditFlight.setObjectName("lineEditFlight")
        self.labelTime = QtWidgets.QLabel(Widget)
        self.labelTime.setGeometry(QtCore.QRect(30, 150, 81, 31))
        self.labelTime.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelTime.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTime.setObjectName("labelTime")
        self.labelToPlace = QtWidgets.QLabel(Widget)
        self.labelToPlace.setGeometry(QtCore.QRect(150, 10, 131, 31))
        self.labelToPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelToPlace.setAlignment(QtCore.Qt.AlignCenter)
        self.labelToPlace.setObjectName("labelToPlace")
        self.labelFromPlace = QtWidgets.QLabel(Widget)
        self.labelFromPlace.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.labelFromPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelFromPlace.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFromPlace.setObjectName("labelFromPlace")
        self.labelFlight = QtWidgets.QLabel(Widget)
        self.labelFlight.setGeometry(QtCore.QRect(280, 10, 131, 31))
        self.labelFlight.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelFlight.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFlight.setObjectName("labelFlight")
        self.checkBoxDate = QtWidgets.QCheckBox(Widget)
        self.checkBoxDate.setGeometry(QtCore.QRect(150, 120, 77, 22))
        self.checkBoxDate.setObjectName("checkBoxDate")
        self.checkBoxTime = QtWidgets.QCheckBox(Widget)
        self.checkBoxTime.setGeometry(QtCore.QRect(150, 190, 77, 22))
        self.checkBoxTime.setObjectName("checkBoxTime")
        self.spinBoxPlace = QtWidgets.QSpinBox(Widget)
        self.spinBoxPlace.setGeometry(QtCore.QRect(260, 110, 71, 41))
        self.spinBoxPlace.setObjectName("spinBoxPlace")
        self.checkBoxPlace = QtWidgets.QCheckBox(Widget)
        self.checkBoxPlace.setGeometry(QtCore.QRect(340, 120, 71, 22))
        self.checkBoxPlace.setObjectName("checkBoxPlace")
        self.labelPlace = QtWidgets.QLabel(Widget)
        self.labelPlace.setGeometry(QtCore.QRect(260, 80, 71, 31))
        self.labelPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelPlace.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPlace.setObjectName("labelPlace")
        self.labelId = QtWidgets.QLabel(Widget)
        self.labelId.setGeometry(QtCore.QRect(260, 150, 71, 31))
        self.labelId.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelId.setAlignment(QtCore.Qt.AlignCenter)
        self.labelId.setObjectName("labelId")
        self.checkBoxId = QtWidgets.QCheckBox(Widget)
        self.checkBoxId.setGeometry(QtCore.QRect(340, 190, 71, 22))
        self.checkBoxId.setObjectName("checkBoxId")
        self.spinBoxId = QtWidgets.QSpinBox(Widget)
        self.spinBoxId.setGeometry(QtCore.QRect(260, 180, 71, 41))
        self.spinBoxId.setObjectName("spinBoxId")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.labelDate.setText(_translate("Widget", "Дата вылета"))
        self.pushButtonFilter.setText(_translate("Widget", "Фильтровать"))
        self.labelTime.setText(_translate("Widget", "Время"))
        self.labelToPlace.setText(_translate("Widget", "Куда"))
        self.labelFromPlace.setText(_translate("Widget", "Откуда"))
        self.labelFlight.setText(_translate("Widget", "Номер рейса"))
        self.checkBoxDate.setText(_translate("Widget", "Любое"))
        self.checkBoxTime.setText(_translate("Widget", "Любое"))
        self.checkBoxPlace.setText(_translate("Widget", "Любые"))
        self.labelPlace.setText(_translate("Widget", "Места"))
        self.labelId.setText(_translate("Widget", "ID"))
        self.checkBoxId.setText(_translate("Widget", "Любое"))

class Ui_admin(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(578, 210)
        self.pushButtonAdd = QtWidgets.QPushButton(Widget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(250, 50, 151, 41))
        self.pushButtonAdd.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonDelete = QtWidgets.QPushButton(Widget)
        self.pushButtonDelete.setGeometry(QtCore.QRect(410, 50, 151, 41))
        self.pushButtonDelete.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.pushButtonExit = QtWidgets.QPushButton(Widget)
        self.pushButtonExit.setGeometry(QtCore.QRect(410, 10, 151, 31))
        self.pushButtonExit.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.lineEdit = QtWidgets.QLineEdit(Widget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 151, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButtonChange = QtWidgets.QPushButton(Widget)
        self.pushButtonChange.setGeometry(QtCore.QRect(410, 150, 151, 41))
        self.pushButtonChange.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonChange.setObjectName("pushButtonChange_2")
        self.radioButtonCity = QtWidgets.QRadioButton(Widget)
        self.radioButtonCity.setGeometry(QtCore.QRect(180, 50, 71, 22))
        self.radioButtonCity.setObjectName("radioButton")
        self.radioButtonFlight = QtWidgets.QRadioButton(Widget)
        self.radioButtonFlight.setGeometry(QtCore.QRect(180, 70, 71, 22))
        self.radioButtonFlight.setObjectName("radioButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 150, 231, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.labelMain_2 = QtWidgets.QLabel(Widget)
        self.labelMain_2.setGeometry(QtCore.QRect(10, 20, 151, 31))
        self.labelMain_2.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelMain_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMain_2.setObjectName("labelMain_2")
        self.labelMain_3 = QtWidgets.QLabel(Widget)
        self.labelMain_3.setGeometry(QtCore.QRect(10, 160, 151, 31))
        self.labelMain_3.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelMain_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMain_3.setObjectName("labelMain_3")
        self.labelMain_4 = QtWidgets.QLabel(Widget)
        self.labelMain_4.setGeometry(QtCore.QRect(20, 110, 551, 31))
        self.labelMain_4.setStyleSheet("font:  10pt \"Segoe UI\";\n"
"color: #000")
        self.labelMain_4.setObjectName("labelMain_4")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.pushButtonAdd.setText(_translate("Widget", "Добавить "))
        self.pushButtonDelete.setText(_translate("Widget", "Удалить "))
        self.pushButtonExit.setText(_translate("Widget", "Назад"))
        self.pushButtonChange.setText(_translate("Widget", "Изменить "))
        self.radioButtonCity.setText(_translate("Widget", "Город"))
        self.radioButtonFlight.setText(_translate("Widget", "Рейс"))
        self.labelMain_2.setText(_translate("Widget", "Название"))
        self.labelMain_3.setText(_translate("Widget", "Новое название:"))
        self.labelMain_4.setText(_translate("Widget", "Город/рейс будет изменен во всех самолетах автоматически"))

class Ui_password(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(282, 94)
        self.pushButtonAdd = QtWidgets.QPushButton(Widget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.pushButtonAdd.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.lineEditPassword = QtWidgets.QLineEdit(Widget)
        self.lineEditPassword.setGeometry(QtCore.QRect(80, 10, 181, 31))
        self.lineEditPassword.setObjectName("lineEditFlight")
        self.labelFlight = QtWidgets.QLabel(Widget)
        self.labelFlight.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.labelFlight.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"color: #000")
        self.labelFlight.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFlight.setObjectName("labelFlight")
        self.pushButtonBack = QtWidgets.QPushButton(Widget)
        self.pushButtonBack.setGeometry(QtCore.QRect(150, 50, 111, 31))
        self.pushButtonBack.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
"background-color: #97ba1e;\n"
"border: 1px solid #97ba1e;\n"
"color: #fff\n"
"")
        self.pushButtonBack.setObjectName("pushButtonAdd_2")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.pushButtonAdd.setText(_translate("Widget", "Подтвердить"))
        self.labelFlight.setText(_translate("Widget", "Пароль"))
        self.pushButtonBack.setText(_translate("Widget", "Отмена"))

