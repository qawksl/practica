import sys

from PyQt6.QtCore import QSize, QStringListModel
from PyQt6.QtWidgets import QMainWindow,QHBoxLayout,QPushButton, QWidget, QListView, QVBoxLayout
from database import Database

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

        self.add_button = QPushButton("Добавить")
        self.del_button = QPushButton("Удалить")
        self.edit_button = QPushButton("Изменить")
        self.update_button = QPushButton("Обновить")
        self.update_button.clicked.connect(self.update_list_view_patients)
        self.otdel_button = QPushButton("Отделение")


        buttons = QHBoxLayout()
        buttons.addWidget(self.add_button)
        buttons.addWidget(self.del_button)
        buttons.addWidget(self.edit_button)
        buttons.addWidget(self.update_button)
        buttons.addWidget(self.otdel_button)
        buttons_widget = QWidget()
        buttons_widget.setLayout(buttons)

        layout = QVBoxLayout()
        layout.addWidget(buttons_widget)
        layout.addWidget(list_widget)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def get_patients(self):
        db = Database()
        result_raw = db.get_patients()
        result = []
        for r in result_raw:
            result.append(str(r["id"])+ "."+ r["name"]+ " "+ r["firstname"]+ " "+ r["otchestvo"] )
        return result

    def get_list_model_patients(self):
        list_model = QStringListModel()
        list_model.setStringList(self.get_patients())
        return list_model
    
    def update_list_view_patients(self):
        self.list_view.setModel(self.get_list_model_patients())

    

    

