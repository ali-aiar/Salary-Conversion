from PyQt6.QtWidgets import QMainWindow,  QTableWidgetItem
from PyQt6 import uic, QtCore
import os


class SalaryView(QMainWindow):
    def __init__(self, salary_data):
        super().__init__()
        file_path = ((os.path.dirname(__file__))) + \
            '/salary_view.ui'
        uic.loadUi(file_path, self)
        self.setWindowTitle('Salary Information')
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 400)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 150)
        self.tableWidget.setColumnWidth(7, 150)
        # self.lineEdit.textChanged.connect(self.on_search_changes)
        self.create_table(salary_data)

    def create_table(self, salary_data):
        for i, salary in enumerate(salary_data):
            item1 = self.cell_style(salary.user_data.id)
            item2 = self.cell_style(salary.user_data.name)
            item3 = self.cell_style(salary.user_data.username)
            item4 = self.cell_style(salary.user_data.email)
            address = salary.user_data.address['street'] + ",  " + \
                salary.user_data.address['suite'] + ",  " + \
                salary.user_data.address['city'] + ",  " + \
                salary.user_data.address['zipcode']
            item5 = self.cell_style(address)
            item6 = self.cell_style(salary.user_data.phone)
            item7 = self.cell_style(
                ("%.3f" % salary.user_salary.user_salary_in_IDR))
            item8 = self.cell_style(
                ("%.3f" % salary.user_salary.converted_user_salary))

            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, item1)
            self.tableWidget.setItem(i, 1, item2)
            self.tableWidget.setItem(i, 2, item3)
            self.tableWidget.setItem(i, 3, item4)
            self.tableWidget.setItem(i, 4, item5)
            self.tableWidget.setItem(i, 5, item6)
            self.tableWidget.setItem(i, 6, item7)
            self.tableWidget.setItem(i, 7, item8)

    def cell_style(self, data):
        item = QTableWidgetItem()
        item.setText(str(data))
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        return item

    # def on_search_changes(self):
    #     search_text = self.lineEdit.text()
    #     if not search_text:
    #         for i in range(self.tableWidget.rowCount()):
    #             self.tableWidget.setRowHidden(i, False)
    #         return
    #     for i in range(self.tableWidget.rowCount()):
    #         hide_row = True
    #         for j in range(self.tableWidget.columnCount()-5):
    #             item = self.tableWidget.item(i, j)
    #             if item and search_text in item.text():
    #                 hide_row = False
    #                 break
    #         self.tableWidget.setRowHidden(i, hide_row)
