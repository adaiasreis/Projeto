from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate, QDateTime
from PyQt5 import uic

class Inicio(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_inicio.ui", self)