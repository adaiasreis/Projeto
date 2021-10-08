from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5 import uic
import sys
from layouts.mainWindow import MainWindow



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()