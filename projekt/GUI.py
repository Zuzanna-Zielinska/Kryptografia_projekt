#pip install pyqt5
#pip install pyqt5-tools

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

window_x_position = 200
window_y_position = 200
window_width = 300
window_height = 500


def button_clicked():
    print("clicked")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(window_x_position, window_y_position, window_width, window_height)
    win.setWindowTitle("Testy pierwszości")

    label = QtWidgets.QLabel(win)
    label.setText("Jej!")
    label.move(50, 50)

    button = QtWidgets.QPushButton(win)
    button.setText("click me")
    button.clicked.connect(button_clicked)


    win.show()
    sys.exit(app.exec_())

window()