from class_window import *

class main_window(QtWidgets.QMainWindow,Ui_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButtonExit.clicked.connect(self.button_Exit)
        self.pushButtonAdd.clicked.connect(self.button_add)
        self.pushButtonDelete.clicked.connect(self.button_delete)
        self.pushButtonCreate.clicked.connect(self.button_report)
        self.pushButtonChange.clicked.connect(self.button_change)
        self.pushButtonFilter.clicked.connect(self.button_filter)
        self.pushButtonAdmin.clicked.connect(self.button_admin)

    def button_admin(self):
        self.hide()
        self.password_window = password_window(self)
        self.password_window.show()

    def button_filter(self):
        self.filter_window = filter_window(self)
        self.filter_window.show()

    def button_change(self):
        selected_cell = self.tableWidget.currentItem()
        if selected_cell is not None:
            row = selected_cell.row()
            item = self.tableWidget.item(row, 0)
            self.hide()
            self.change_window = change_window(self, item.text())
            self.change_window.show()
        else:
            QMessageBox.question(self, 'Message', "Не выбрана записи для изменения.",
                                     QMessageBox.Ok)

    def button_report(self):
        self.hide()
        self.report_window = report_window(self)
        self.report_window.show()

    def button_Exit(self):
        self.close()
        app.exit()

    def button_add(self):
        self.hide()
        self.add_window = add_window(self)
        self.add_window.show()

    def open_table(self, where):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        # Выравнивание для столбцов таблицы
        self.tableWidget.horizontalHeader().setSectionResizeMode( QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5,QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderLabels(["Id", "Дата", "Время", "Откуда", "Куда", "Рейс","Свободные места"])
        # Добавляем строки из базы данных
        if where != "":
            rows = get_flight_where(where)
        else:
            rows = get_airplane()
        for row in rows:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            for column, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_position, column, item)

    def button_delete(self):
        reply = QMessageBox.question(self, 'Message', "Вы уверены, что хотите удалить эти данные из таблицы? Их нельзя будет восстановить",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if self.tableWidget.selectedItems():
                selected_items = self.tableWidget.selectedItems()
                selected_rows = set()

                for item in selected_items:
                    selected_rows.add(item.row())
                # Теперь selected_rows содержит индексы всех выделенных строк

                for row in selected_rows:
                    item = self.tableWidget.item(row, 0)
                    delete_airplane(item.text())
                self.open_table('')
            else:
                QMessageBox.question(self, 'Message', "Не выбраны записи для удаления.",
                                     QMessageBox.Ok)

    def open(self):
        where = ""
        window.show()
        self.open_table(where)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = main_window()
    window.open()
    sys.exit(app.exec_())

# Закрываем соединение с базой данных
connection.close()
