import sys

from PyQt6.QtCore import QSize, QStringListModel
from PyQt6.QtWidgets import QMainWindow,QHBoxLayout,QPushButton, QWidget, QListView, QVBoxLayout
from database import Database
from datetime import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Главная")
        self.resize(800,600)

        list_model = QStringListModel()
        list_model.setStringList(self.get_patients())

        list_widget = QWidget()
        self.list_view = QListView(list_widget)
        self.list_view.setModel(list_model)
        self.list_view.resize(800,600)

        layout = QVBoxLayout()
        layout.addWidget(list_widget)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def get_patients(self):
        db = Database()
        result_raw = db.get_patients()
        result = []
        for r in result_raw:
            day_births = datetime.strptime(str(r["day_births"]), "%Y-%m-%d").strftime("%d.%m.%Y")
            result.append(str(r["id"])+ "."+ r["firstname"]+ " "+ r["name"]+ " "+ r["otchestvo"]+ " " + day_births)
        return result

    def get_list_model_patients(self):
        list_model = QStringListModel()
        list_model.setStringList(self.get_patients())
        return list_model
    
    def update_list_view_patients(self):
        self.list_view.setModel(self.get_list_model_patients())

    

    

