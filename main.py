from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout
from random import randint
def show_winner():
    number = randint(0,99)
    winner.setText(str(number))
    text.setText('Бабиджон:')

app = QApplication([])
main_win = QWidget()
main_win.resize(400,400)

but  = QPushButton('Сгенерировать')
text = QLabel('Кто бабиджон?')
winner = QLabel('?')
line = QVBoxLayout()

line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(but, alignment = Qt.AlignCenter)
main_win.setLayout(line)


but.clicked.connect(show_winner)
main_win.show()
app.exec_()
