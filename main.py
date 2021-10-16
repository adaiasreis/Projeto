from PyQt5.QtWidgets import QApplication
import sys
from layouts.ui_telaLogin import FazerLogin


app = QApplication(sys.argv)
window = FazerLogin()
window.show()
app.exec_()