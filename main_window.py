import sys

from PyQt6.QtCore import QSize, QStringListModel
from PyQt6.QtWidgets import QMainWindow,QHBoxLayout,QPushButton, QWidget, QListView, QVBoxLayout
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Главная")
        self.resize(800,600)