from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import QDir
import sys
import os
from main_window import MainWindow

os.chdir(os.path.dirname(__file__))
app = QApplication(sys.argv)
app.setWindowIcon(QIcon(os.path.join(QDir.currentPath(), "images", "logo.ico")))
window = MainWindow(app)
window.show()
app.exec()