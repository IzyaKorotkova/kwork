from interface import *
import tkinter as tk
from tkinter import filedialog
import openpyxl
from PyQt5.QtWidgets import QHeaderView, QMessageBox
from sql import *


class password_window(QtWidgets.QMainWindow,Ui_password):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.pushButtonAdd.clicked.connect(self.button_add)
        self.parent = parent
        self.pushButtonBack.clicked.connect(self.button_back)

    def button_add(self):
        if self.lineEditPassword.text() == '1234':
            self.admin_window = admin_window(self.parent)
            self.admin_window.show()
        else:
            QMessageBox.question(self, 'Message', "Пароль неверный.",
                                     QMessageBox.Ok)

    def button_back(self):
        self.hide()
        self.parent.open()


class admin_window(QtWidgets.QMainWindow,Ui_admin):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.pushButtonExit.clicked.connect(self.back)
        self.pushButtonAdd.clicked.connect(self.button_add)
        self.pushButtonDelete.clicked.connect(self.button_delete)
        self.pushButtonChange.clicked.connect(self.button_change)

    def button_change(self):
        if self.radioButtonCity.isChecked() and self.lineEdit.text() and self.lineEdit_2.text():
            change_city(self.lineEdit.text(), self.lineEdit_2.text())
        elif self.radioButtonFlight.isChecked() and self.lineEdit.text() and self.lineEdit_2.text():
            change_flight(self.lineEdit.text(), self.lineEdit_2.text())
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def button_delete(self):
        if self.radioButtonCity.isChecked() and self.lineEdit.text():
            delete_city(self.lineEdit.text())
        elif self.radioButtonFlight.isChecked() and self.lineEdit.text():
            delete_flight(self.lineEdit.text())
        self.lineEdit.clear()

    def button_add(self):
        if self.radioButtonCity.isChecked() and self.lineEdit.text():
            add_city(self.lineEdit.text())
        elif self.radioButtonFlight.isChecked() and self.lineEdit.text():
            add_flight(self.lineEdit.text())
        self.lineEdit.clear()

    def back(self):
            self.hide()
            self.parent.open()

class filter_window(QtWidgets.QMainWindow,Ui_Filter):

    def __init__(self,parent):
        super().__init__()
        self.setupUi(self)
        self.pushButtonFilter.clicked.connect(self.button_filter)
        self.parent = parent

    def button_filter(self):
        where =""
        if not self.checkBoxDate.isChecked() :
            date = self.dateEdit.text()
            Y, M, D = date.split('.')
            date = f"{D}.{M}.{Y}"
            where += "a.date_fly = '" + date + "' and "
        if not self.checkBoxTime.isChecked():
            where += "a.time_fly = '" + self.timeEdit.text() + "' and "
        if not self.checkBoxId.isChecked():
            where += "a.id = " + self.spinBoxId.text() + " and "
        if not self.checkBoxPlace.isChecked():
            where += "a.free_place = " + self.spinBoxPlace.text() + " and "
        if self.lineEditFromPlace.text():
            id_from = get_city_2(self.lineEditFromPlace.text())
            where += "from_place = " + str(id_from) + " and "
        if self.lineEditToPlace.text():
            id_to = get_city_2(self.lineEditToPlace.text())
            where += "to_place = " + str(id_to) + " and "
        if self.lineEditFlight.text():
            id_flight = get_flight_2(self.lineEditFlight.text())
            where += "flight_id = " + str(id_flight) + " and "
        if where != "":
            where = where[:-4]
        self.parent.open_table(where)


class change_window(QtWidgets.QMainWindow,Ui_add):

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.labelDate.setText(_translate("Widget", "Дата вылета"))
        self.pushButtonAdd.setText(_translate("Widget", "Изменить"))
        self.pushButtonBack.setText(_translate("Widget", "Назад"))
        self.labelTime.setText(_translate("Widget", "Время"))
        self.labelToPlace.setText(_translate("Widget", "Пункт прибытия"))
        self.labelFromPlace.setText(_translate("Widget", "Пункт отправления"))
        self.labelFlight.setText(_translate("Widget", "Номер рейса"))
        self.labelPlace.setText(_translate("Widget", "Места"))

    def __init__(self,parent,id):
        super().__init__()
        self.setupUi(self)
        self.pushButtonAdd.clicked.connect(self.button_add)
        self.parent = parent
        self.pushButtonBack.clicked.connect(self.back)
        self.id = id

    def back(self):
            self.hide()
            self.parent.open()

    def button_add(self):
        a = True
        self.labelFromPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: fff")
        self.labelToPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: fff")
        self.labelFlight.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: fff")
        if not self.lineEditFromPlace.text():
            a=False
            QMessageBox.question(self, 'Message', "Не заполнен пункт отправления.",
                                     QMessageBox.Ok)
            self.labelFromPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
        elif get_city_2(self.lineEditFromPlace.text()) == '':
            a=False
            QMessageBox.question(self, 'Message', "Нет такого города.",
                                     QMessageBox.Ok)
            self.labelFromPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
        if not self.lineEditToPlace.text():
            a=False
            QMessageBox.question(self, 'Message', "Не заполнен пункт прибытия.",
                                     QMessageBox.Ok)
            self.labelToPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
        elif get_city_2(self.lineEditToPlace.text()) == '':
            a=False
            QMessageBox.question(self, 'Message', "Нет такого города.",
                                     QMessageBox.Ok)
            self.labelToPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
        if not self.lineEditFlight.text():
            a=False
            QMessageBox.question(self, 'Message', "Не заполнен номер рейса.",
                                     QMessageBox.Ok)
            self.labelFlight.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
        elif get_flight_2(self.lineEditFlight.text()) == '':
            a=False
            QMessageBox.question(self, 'Message', "Нет такого рейса.",
                                     QMessageBox.Ok)
            self.labelFlight.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
        if self.lineEditToPlace.text() == self.lineEditFromPlace.text():
            a=False
            QMessageBox.question(self, 'Message', "Пункты назначения и отправления не могут совпадать.",
                                     QMessageBox.Ok)
            self.labelFromPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
            self.labelToPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
        if a:
            change_flight_schedule(self.id, self.dateEdit.text(), self.timeEdit.text(), get_city_2(self.lineEditToPlace.text()), get_city_2(self.lineEditFromPlace.text()), get_flight_2(self.lineEditFlight.text()), self.spinBox.text())
            self.back()

class report_window(QtWidgets.QMainWindow,Ui_report):
    def __init__(self,parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.pushButtonBack.clicked.connect(self.back)
        self.pushButtonAdd.clicked.connect(self.button_add)

    def back(self):
        self.hide()
        self.parent.open()

    def button_add(self):
        checked_options = []
        if self.checkBoxDate.isChecked():
            checked_options.append("Дата")
        if self.checkBoxTime.isChecked():
            checked_options.append("Время")
        if self.checkBoxFromPlace.isChecked():
            checked_options.append("Пункт отправления")
        if self.checkBoxToPlace.isChecked():
            checked_options.append("Пункт прибытия")
        if self.checkBoxFlight.isChecked():
            checked_options.append("Рейс")
        if self.checkBoxFreePlace.isChecked():
            checked_options.append("Места")
        if checked_options:
            self.hide()
            self.report2window = report2_window(self, checked_options)
            self.report2window.open()
        else:
            QMessageBox.question(self, 'Message', "Не выбраны пункты для отчета.",
                                     QMessageBox.Ok)


class report2_window(QtWidgets.QMainWindow,Ui_report2):
    def __init__(self, parent, checked_options):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.pushButtonBack.clicked.connect(self.back)
        self.checked_options = checked_options
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.on_header_clicked)
        self.first_clicked_index = None
        self.pushButtonAdd.clicked.connect(self.add)

    def add(self):
        root = tk.Tk()
        root.withdraw()  # Скрыть основное окно
        file_name = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if file_name:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            for row in range(self.tableWidget.rowCount()):
                for column in range(self.tableWidget.columnCount()):
                    cell = sheet.cell(row=row+1, column=column+1)
                    item = self.tableWidget.item(row, column)
                    if item is not None:
                        cell.value = item.text()
                    else:
                        cell.value = ''
            workbook.save(file_name)

    def on_header_clicked(self, logicalIndex):
        if self.first_clicked_index is None:
            self.first_clicked_index = logicalIndex  # сохраняем индекс первого нажатия
        else:
            second_index = logicalIndex
            rows_count = self.tableWidget.rowCount()
            for row in range(rows_count):
                item1 = self.tableWidget.item(row, self.first_clicked_index)
                item2 = self.tableWidget.item(row, second_index)  #индекс другого столбца

                # обмен содержимым ячеек
                temp_text = item1.text()
                item1.setText(item2.text())
                item2.setText(temp_text)
            temp = self.checked_options[self.first_clicked_index]
            self.checked_options[self.first_clicked_index] = self.checked_options[second_index]
            self.checked_options[second_index] = temp
            self.tableWidget.setHorizontalHeaderLabels(self.checked_options)
            self.first_clicked_index = None

    def open_table(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(self.checked_options))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        if len(self.checked_options)>1:
            self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(self.checked_options)
        # Добавляем строки из базы данных
        rows = get_airplane_2(self.checked_options)
        for row in rows:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            for column, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_position, column, item)

    def back(self):
        self.hide()
        self.parent.show()

    def open(self):
        self.show()
        self.open_table()


class add_window(QtWidgets.QMainWindow,Ui_add):
    def __init__(self,parent):
        super().__init__()
        self.setupUi(self)
        self.pushButtonAdd.clicked.connect(self.button_add)
        self.parent = parent
        self.pushButtonBack.clicked.connect(self.back)

    def back(self):
            self.hide()
            self.parent.open()

    def button_add(self):
        a = True
        self.labelFromPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: fff")
        self.labelToPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: fff")
        self.labelFlight.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: fff")
        if not self.lineEditFromPlace.text():
            a=False
            QMessageBox.question(self, 'Message', "Не заполнен пункт отправления.",
                                     QMessageBox.Ok)
            self.labelFromPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
        elif get_city_2(self.lineEditFromPlace.text()) == '':
            a=False
            QMessageBox.question(self, 'Message', "Нет такого города.",
                                     QMessageBox.Ok)
            self.labelFromPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
        if not self.lineEditToPlace.text():
            a=False
            QMessageBox.question(self, 'Message', "Не заполнен пункт прибытия.",
                                     QMessageBox.Ok)
            self.labelToPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
        elif get_city_2(self.lineEditToPlace.text()) == '':
            a=False
            QMessageBox.question(self, 'Message', "Нет такого города.",
                                     QMessageBox.Ok)
            self.labelToPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
        if not self.lineEditFlight.text():
            a=False
            QMessageBox.question(self, 'Message', "Не заполнен номер рейса.",
                                     QMessageBox.Ok)
            self.labelFlight.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
        elif get_flight_2(self.lineEditFlight.text()) == '':
            a=False
            QMessageBox.question(self, 'Message', "Нет такого рейса.",
                                     QMessageBox.Ok)
            self.labelFlight.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
        if self.lineEditToPlace.text() == self.lineEditFromPlace.text():
            a=False
            QMessageBox.question(self, 'Message', "Пункты назначения и отправления не могут совпадать.",
                                     QMessageBox.Ok)
            self.labelFromPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
            self.labelToPlace.setStyleSheet("font: 10pt \"Segoe UI\";\n" "color: red")
        if a:
            add_flight_schedule(self.dateEdit.text(), self.timeEdit.text(), get_city_2(self.lineEditToPlace.text()), get_city_2(self.lineEditFromPlace.text()), get_flight_2(self.lineEditFlight.text()), self.spinBox.text())
            self.back()
