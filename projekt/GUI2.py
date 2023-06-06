import random
import miller_rabin
import solovay_strassen

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QTextEdit, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.show_details = False

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

        self.iteration_number_label = QLabel("Liczba iteracji:")
        self.iteration_number_input = QLineEdit()
        self.iteration_number_input.setText("4")

        self.details_button = QPushButton("Pokaż szczegółowe rozwiązanie")
        self.details_button.setCheckable(True)
        self.details_button.clicked.connect(self.set_details)

        self.start_button = QPushButton("Rozpocznij test")
        self.start_button.clicked.connect(self.test_number)

        self.solovay_label = QLabel("Test Solovaya-Strassena")
        self.solovay_label.setAlignment(Qt.AlignCenter)
        self.miller_label = QLabel("Test Millera-Rabina")
        self.miller_label.setAlignment(Qt.AlignCenter)

        self.solovay_steps = QTextEdit()
        self.solovay_steps.setReadOnly(True)
        self.solovay_steps.setLineWrapMode(QTextEdit.WidgetWidth)

        self.miller_steps = QTextEdit()
        self.miller_steps.setReadOnly(True)
        self.miller_steps.setLineWrapMode(QTextEdit.WidgetWidth)

        self.results_solovay = QLabel()
        self.results_solovay.setAlignment(Qt.AlignCenter)  # Wyśrodkowanie tekstu
        self.results_miller = QLabel()
        self.results_miller.setAlignment(Qt.AlignCenter)  # Wyśrodkowanie tekstu

        self.advanced_options = QPushButton("Zaawansowane opcje")
        self.advanced_options.clicked.connect(self.set_advanced_options)

        # self.generate_from_label = QLabel("Od:").hide()

        row_num = 0
        layout = QGridLayout()
        layout.addWidget(self.title_label, row_num, 0, 1, 3)
        row_num += 1

        layout.addWidget(self.number_label, row_num, 0)
        layout.addWidget(self.number_input, row_num, 1)
        layout.addWidget(self.generate_button, row_num, 2)

        # layout.addWidget(self.generate_from_label, row_num, 3)
        row_num += 1

        layout.addWidget(self.iteration_number_label, row_num, 0)
        layout.addWidget(self.iteration_number_input, row_num, 1)
        layout.addWidget(self.details_button, row_num, 2)
        row_num += 1

        layout.addWidget(self.start_button, row_num, 0, 1, 3)
        row_num += 1

        layout.addWidget(self.solovay_label, row_num, 0)
        layout.addWidget(self.miller_label, row_num, 2)
        row_num += 1

        layout.addWidget(self.solovay_steps, row_num, 0)
        layout.addWidget(self.miller_steps, row_num, 2)
        row_num += 1

        layout.addWidget(self.results_solovay, row_num, 0)
        layout.addWidget(self.results_miller, row_num, 2, 1, 2)
        row_num += 1

        # layout.addWidget(self.advanced_options, row_num, 2)
        row_num += 1

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def set_details(self):

        self.show_details = not self.show_details

    def set_advanced_options(self):
        # self.generate_from_label.show()
        pass

    def generate_number(self):
        num = random.randint(1, 1000000)
        if num % 2 == 0:
            num += 1

        self.number_input.setText(str(num))
        return num

    def test_number(self):

        if self.number_input.text() == "":
            self.number_input.setText(str(self.generate_number()))
        if self.iteration_number_input.text() == "":
            self.iteration_number_input.setText("4")

        result_miller_rabin = miller_rabin.miller(int(self.number_input.text()), int(self.iteration_number_input.text()), self.show_details)
        result_solovay_strassen = solovay_strassen.solovay_strassen(int(self.number_input.text()), int(self.iteration_number_input.text()), self.show_details)


        self.show_steps(result_miller_rabin[1], result_solovay_strassen[1])
        self.show_result(result_miller_rabin[0], result_solovay_strassen[0])

    def show_steps(self, steps_miller_rabin, steps_solovay_strassen):

        self.miller_steps.setText(steps_miller_rabin)
        self.solovay_steps.setText(steps_solovay_strassen)

    def show_result(self, result_miller_rabin, result_solovay_strassen):

        if result_miller_rabin:
            self.results_miller.setText(f"Liczba jest pierwsza  z minimalnym \nprawdopodobieństwem {1 - 4**(-int(self.iteration_number_input.text()))}")
        else:
            self.results_miller.setText("Liczba jest złożona")

        if result_solovay_strassen:
            self.results_solovay.setText(f"Liczba jest pierwsza  z minimalnym \nprawdopodobieństwem {1 - 2**(-int(self.iteration_number_input.text()))}")
        else:
            self.results_solovay.setText("Liczba jest złożona")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
