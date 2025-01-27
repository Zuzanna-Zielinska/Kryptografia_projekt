import random
import miller_rabin
import solovay_strassen
import time

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, \
    QPushButton, QGridLayout, QTextEdit, QWidget, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setGeometry(300, 300, 800, 550)

        self.setMinimumSize(800, 550)
        self.show_details = False
        self.a = -1
        self.force_a = False

        self.int_validator = QIntValidator()


        self.setWindowTitle("Testy pierwszeństwa")

        self.title_label = QLabel("Testy pierwszeństwa")
        self.title_label.setAlignment(Qt.AlignCenter)  # Wyśrodkowanie tekstu

        self.number_label = QLabel("Liczba:")
        self.number_input = QLineEdit()
        self.number_input.setValidator(self.int_validator)

        self.generate_button = QPushButton("Wygeneruj liczbę")
        self.generate_button.clicked.connect(self.generate_number)

        self.iteration_number_label = QLabel("Liczba iteracji:")
        self.iteration_number_input = QLineEdit()
        self.iteration_number_input.setText("4")
        self.iteration_number_input.setValidator(self.int_validator)

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
        self.solovay_steps.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.miller_steps = QTextEdit()
        self.miller_steps.setReadOnly(True)
        self.miller_steps.setLineWrapMode(QTextEdit.WidgetWidth)
        self.miller_steps.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.results_solovay = QLabel()
        self.results_solovay.setAlignment(Qt.AlignCenter)  # Wyśrodkowanie tekstu
        self.results_miller = QLabel()
        self.results_miller.setAlignment(Qt.AlignCenter)  # Wyśrodkowanie tekstu

        self.advanced_options = QPushButton("Zaawansowane opcje")
        self.advanced_options.setCheckable(True)
        self.advanced_options.clicked.connect(self.set_advanced_options)

        self.generate_from_label = QLabel("Wygeneruj liczbę  od:")
        self.generate_from_label.setVisible(False)
        self.generate_from_input = QLineEdit()
        self.generate_from_input.setVisible(False)
        self.generate_from_input.setText("1")
        self.generate_from_input.setValidator(self.int_validator)
        self.generate_from_input.setMaximumWidth(200)

        self.generate_to_label = QLabel("Wygeneruj liczbę do:")
        self.generate_to_label.setVisible(False)
        self.generate_to_input = QLineEdit()
        self.generate_to_input.setVisible(False)
        self.generate_to_input.setText("1000000")
        self.generate_to_input.setValidator(self.int_validator)
        self.generate_to_input.setMaximumWidth(200)

        self.insert_a_button = QPushButton("Wymuś pierwsze a:")
        self.insert_a_button.setVisible(False)
        self.insert_a_button.setCheckable(True)
        # self.insert_a_button.setAlignment(Qt.AlignCenter)
        self.insert_a_button.clicked.connect(self.set_a)

        self.insert_a_input = QLineEdit()
        self.insert_a_input.setVisible(False)
        self.insert_a_input.setValidator(self.int_validator)
        self.insert_a_input.setMaximumWidth(200)

        self.set_app_style()


        row_num = 0
        layout = QGridLayout()
        layout.addWidget(self.title_label, row_num, 0, 1, 4)
        row_num += 1

        layout.addWidget(self.number_label, row_num, 0)
        layout.addWidget(self.number_input, row_num, 1, 1, 2)
        layout.addWidget(self.generate_button, row_num, 3)
        row_num += 1

        layout.addWidget(self.iteration_number_label, row_num, 0)
        layout.addWidget(self.iteration_number_input, row_num, 1, 1, 2)
        layout.addWidget(self.details_button, row_num, 3)
        row_num += 1

        layout.addWidget(self.start_button, row_num, 0, 1, 4)
        row_num += 1

        layout.addWidget(self.solovay_label, row_num, 0, 1, 2)
        layout.addWidget(self.miller_label, row_num, 2, 1, 2)
        row_num += 1

        layout.addWidget(self.solovay_steps, row_num, 0, 1, 2)
        layout.addWidget(self.miller_steps, row_num, 2, 1, 2)
        row_num += 1

        layout.addWidget(self.results_solovay, row_num, 0, 1, 2)
        layout.addWidget(self.results_miller, row_num, 2, 1, 2)
        row_num += 1

        layout.addWidget(self.advanced_options, row_num, 3)
        row_num += 1

        layout.addWidget(self.generate_from_label, 1, 4)
        layout.addWidget(self.generate_from_input, 2, 4)
        layout.addWidget(self.generate_to_label, 3, 4)
        layout.addWidget(self.generate_to_input, 4, 4)
        layout.addWidget(self.insert_a_button, 5, 4, alignment=Qt.AlignBottom)
        layout.addWidget(self.insert_a_input, 6, 4)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def set_app_style(self):
        self.backgroung_color = "#343132"
        self.text_color = "#D8E2DC"
        self.border_color = "#B3D6C6"
        # self.border_color = "#D8E2DC"
        self.button_color = "#B3D6C6"
        self.button_text_color = "#343132"

        # self.backgroung_color = "#343132"
        # self.text_color = "#D8E2DC"
        # self.border_color = "#60C799"
        # # self.border_color = "#D8E2DC"
        # self.button_color = "#60C799"
        # self.button_text_color = "#343132"


        # title_font = QFont("Times New Roman", 16)
        # normal_font = QFont("Times New Roman", 10)
        title_font = QFont("Aptos", 16)
        normal_font = QFont("Aptos")
        # title_font = QFont("Calibri", 16)
        # normal_font = QFont("Calibri", 10)


        #background-color
        self.setStyleSheet(f"background-color: {self.backgroung_color};")


        #text and buttons color
        self.title_label.setStyleSheet(f"color: {self.text_color};")
        self.number_label.setStyleSheet(f"color: {self.text_color};")
        self.iteration_number_label.setStyleSheet(f"color: {self.text_color};")
        self.solovay_label.setStyleSheet(f"color: {self.text_color};")
        self.miller_label.setStyleSheet(f"color: {self.text_color};")
        self.results_solovay.setStyleSheet(f"color: {self.text_color};")
        self.results_miller.setStyleSheet(f"color: {self.text_color};")

        self.generate_button.setStyleSheet(f"color: {self.button_text_color};background-color: {self.button_color};")
        self.details_button.setStyleSheet(f"color: {self.button_text_color};background-color: {self.button_color};")
        self.start_button.setStyleSheet(f"color: {self.button_text_color};background-color: {self.button_color};")
        self.advanced_options.setStyleSheet(f"color: {self.button_text_color};background-color: {self.button_color};")
        self.insert_a_button.setStyleSheet(f"color: {self.button_text_color};background-color: {self.button_color};")
        # self.generate_button.setStyleSheet(f"color: {self.text_color};")
        # self.details_button.setStyleSheet(f"color: {self.text_color};")
        # self.start_button.setStyleSheet(f"color: {self.text_color};")
        # self.advanced_options.setStyleSheet(f"color: {self.text_color};")
        # self.insert_a_button.setStyleSheet(f"color: {self.text_color};")

        self.solovay_steps.setStyleSheet(f"color: {self.text_color}; border: 1px solid {self.border_color};")
        self.miller_steps.setStyleSheet(f"color: {self.text_color}; border: 1px solid {self.border_color};")

        self.number_input.setStyleSheet(f"color: {self.text_color}; border: 1px solid {self.border_color};")
        self.iteration_number_input.setStyleSheet(f"color: {self.text_color}; border: 1px solid {self.border_color};")

        self.generate_from_label.setStyleSheet(f"color: {self.text_color};")
        self.generate_from_input.setStyleSheet(f"color: {self.text_color}; border: 1px solid {self.border_color};")
        self.generate_to_label.setStyleSheet(f"color: {self.text_color};")
        self.generate_to_input.setStyleSheet(f"color: {self.text_color}; border: 1px solid {self.border_color};")
        self.insert_a_input.setStyleSheet(f"color: {self.text_color}; border: 1px solid {self.border_color};")

        #font
        self.title_label.setFont(title_font)
        self.number_label.setFont(normal_font)
        self.iteration_number_label.setFont(normal_font)
        self.solovay_label.setFont(normal_font)
        self.miller_label.setFont(normal_font)
        self.results_solovay.setFont(normal_font)
        self.results_miller.setFont(normal_font)

        self.number_input.setFont(normal_font)
        self.iteration_number_input.setFont(normal_font)
        self.solovay_steps.setFont(normal_font)
        self.miller_steps.setFont(normal_font)
        self.generate_from_label.setFont(normal_font)
        self.generate_from_input.setFont(normal_font)
        self.generate_to_label.setFont(normal_font)
        self.generate_to_input.setFont(normal_font)
        self.insert_a_input.setFont(normal_font)

        self.generate_button.setFont(normal_font)
        self.details_button.setFont(normal_font)
        self.start_button.setFont(normal_font)
        self.advanced_options.setFont(normal_font)
        self.insert_a_button.setFont(normal_font)




    def set_details(self):

        self.show_details = not self.show_details

    def set_a(self):

        self.force_a = not self.force_a
        self.a = -1


    def set_advanced_options(self):
        # self.generate_from_label.show()
        if self.generate_from_label.isVisible():
            self.generate_from_label.setVisible(False)
            self.generate_from_input.setVisible(False)
            self.generate_to_label.setVisible(False)
            self.generate_to_input.setVisible(False)
            self.insert_a_button.setVisible(False)
            self.insert_a_input.setVisible(False)
        else:
            self.generate_from_label.setVisible(True)
            self.generate_from_input.setVisible(True)
            self.generate_to_label.setVisible(True)
            self.generate_to_input.setVisible(True)
            self.insert_a_button.setVisible(True)
            self.insert_a_input.setVisible(True)
        pass

    def generate_number(self):

        f = self.generate_from_input.text()
        t = self.generate_to_input.text()

        if f == "":
            self.generate_from_input.setText("1")
            f = "1"

        if t == "":
            self.generate_to_input.setText("1000000")
            t = "1000000"

        f = int(f)
        t = int(t)

        if f >= t:
            self.generate_from_input.setText("1")
            self.generate_to_input.setText("1000000")
            f = 1
            t = 1000000


        num = random.randint(f, t)

        if num % 2 == 0:
            num += 1
            if num > t:
                num -= 2

        self.number_input.setText(str(num))
        return num

    def test_number(self):

        # start = time.time()

        n_number_txt = self.number_input.text()

        if n_number_txt == "":
            self.number_input.setText(str(self.generate_number()))
        n_int = int(self.number_input.text())

        if n_int < 0:
            n_int = abs(n_int)
            self.number_input.setText(str(n_int))

        i_number_txt = self.iteration_number_input.text()
        if i_number_txt == "":
            self.iteration_number_input.setText("4")
            i_number_txt = 4
        if int(i_number_txt) < 1:
            self.iteration_number_input.setText("1")

        # print(f"------------\n{self.a}\n")

        a_message = ""
        if self.insert_a_input.text() != "" and self.force_a:
            self.a = int(self.insert_a_input.text())
            a_message = "1 < a < n-1\n\n"


        result_miller_rabin = miller_rabin.miller(n_int,
                                                  int(self.iteration_number_input.text()),
                                                  self.show_details,
                                                  self.a)
        result_solovay_strassen = solovay_strassen.solovay_strassen(n_int,
                                                                    int(self.iteration_number_input.text()),
                                                                    self.show_details,
                                                                    self.a)

        if n_int == 0 or n_int == 1:
            self.miller_steps.setText("")
            self.solovay_steps.setText("")
            self.results_miller.setText("Liczba nie jest ani pierwsza, ani złożona")
            self.results_solovay.setText("Liczba nie jest ani pierwsza, ani złożona")
        else:
            self.show_steps(result_miller_rabin[1], result_solovay_strassen[1], a_message)
            self.show_result(result_miller_rabin[0], result_solovay_strassen[0])

        # end = time.time()
        # print(f"Time: {end - start}")

    def show_steps(self, steps_miller_rabin, steps_solovay_strassen, a_message = ""):

        self.miller_steps.setText(a_message + steps_miller_rabin)
        self.solovay_steps.setText(a_message + steps_solovay_strassen)

    def show_result(self, result_miller_rabin, result_solovay_strassen):

        if result_miller_rabin:
            self.results_miller.setText(f"Liczba jest pierwsza z minimalnym \nprawdopodobieństwem "
                                        f"{1 - 4**(-int(self.iteration_number_input.text()))}")
        else:
            self.results_miller.setText("Liczba jest złożona")

        if result_solovay_strassen:
            self.results_solovay.setText(f"Liczba jest pierwsza z minimalnym \nprawdopodobieństwem "
                                         f"{1 - 2**(-int(self.iteration_number_input.text()))}")
        else:
            self.results_solovay.setText("Liczba jest złożona")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
