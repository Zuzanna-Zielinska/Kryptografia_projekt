import random
import miller_rabin

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QTextEdit, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Testy pierwszeństwa")

        self.title_label = QLabel("Testy pierwszeństwa")
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)  # Wyśrodkowanie tekstu

        self.number_label = QLabel("Liczba:")
        self.number_input = QLineEdit()

        self.generate_button = QPushButton("Wygeneruj liczbę")
        self.generate_button.clicked.connect(self.generate_number)

        self.start_button = QPushButton("Rozpocznij test")
        self.start_button.clicked.connect(self.test_number)

        self.solovay_label = QLabel("Test Solovaya-Strassena")
        # self.solovay_label.setAlignment(Qt.AlignCenter) #Nie działa
        self.miller_label = QLabel("Test Millera-Rabina")
        # self.miller_label.setAlignment(Qt.AlignCenter)

        self.solovay_steps = QTextEdit()
        self.solovay_steps.setReadOnly(True)
        self.solovay_steps.setLineWrapMode(QTextEdit.WidgetWidth)

        self.miller_steps = QTextEdit()
        self.miller_steps.setReadOnly(True)
        self.miller_steps.setLineWrapMode(QTextEdit.WidgetWidth)

        self.results_label = QLabel("Wynik testu")
        self.results_label.setAlignment(Qt.AlignCenter)  # Wyśrodkowanie tekstu
        self.results = QLabel()
        self.results.setAlignment(Qt.AlignCenter)  # Wyśrodkowanie tekstu

        row_num = 0
        layout = QGridLayout()
        layout.addWidget(self.title_label, row_num, 0, 1, 3)
        row_num += 1

        layout.addWidget(self.number_label, row_num, 0)
        layout.addWidget(self.number_input, row_num, 1)
        layout.addWidget(self.generate_button, row_num, 2)
        row_num += 1

        layout.addWidget(self.start_button, row_num, 0, 1, 3)
        row_num += 1

        layout.addWidget(self.solovay_label, row_num, 0)
        layout.addWidget(self.miller_label, row_num, 1)
        row_num += 1

        layout.addWidget(self.solovay_steps, row_num, 0)
        layout.addWidget(self.miller_steps, row_num, 1)
        row_num += 1

        layout.addWidget(self.results_label, row_num, 0)
        layout.addWidget(self.results, row_num, 1, 1, 2)
        row_num += 1

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def generate_number(self):
        num = random.randint(1, 1000000)
        self.number_input.setText(str(num))

        # Tutaj możesz umieścić kod do generowania liczby
        # Możesz odczytać wprowadzoną wartość z self.number_input.text()
        return num

    def test_number(self):

        result_miller_rabin = miller_rabin.get_15_numbers()
        result_solovay_strassen = miller_rabin.get_15_numbers()

        self.show_steps(result_miller_rabin[1], result_solovay_strassen[1])
        self.show_result(result_miller_rabin[0], result_solovay_strassen[0])

    def show_steps(self, steps_miller_rabin, steps_solovay_strassen):

        self.miller_steps.setText(str(steps_miller_rabin))
        self.solovay_steps.setText(str(steps_solovay_strassen))

    def show_result(self, result_miller_rabin, result_solovay_strassen):

        if result_miller_rabin == result_solovay_strassen:
            self.results.setText(f"Liczba jest pierwsza  z prawdopodobieństwem 3/4")
        else:
            self.results.setText("Liczba jest złożona")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
