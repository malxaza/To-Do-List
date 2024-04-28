import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi


#შევქმენით კლასი, რომელშიც ვქმინთ მთავარ ფანჯარას
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("design.ui", self)#შემოვიტანეთ დიზაინის ფაილი
        self.btnadd.clicked.connect(self.add_task)
        self.btnremove.clicked.connect(self.remove_task)

    def add_task(self):
        task = self.lineEdit.text()
        if task:
            self.listWidget.addItem(task)
            self.lineEdit.clear()

    def remove_task(self):
        selected_task = self.listWidget.selectedItems()
        if selected_task:
            for task in selected_task:
                self.listWidget.takeItem(self.listWidget.row(task))


app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle("To Do list")
window.show()
sys.exit(app.exec_())





