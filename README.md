# Kryptografia_projekt




Notatki

Gui
Aplikacja: qt designer
Generowanie kodu:
python -m PyQt5.uic.pyuic
python -m PyQt5.uic.pyuic from_qt_designer.ui -o gui_from_designer.py



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
