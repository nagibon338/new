from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint

app = QApplication([])
main_win = QWidget()
main_win.resize(300,200)

question = QLabel('Сколько числом фильмов "Мстители"? ')
 
btn1 = QRadioButton('1')
btn2 = QRadioButton('2')
btn3 = QRadioButton('3')
btn4 = QRadioButton('4')

def show_win():
    box = QMessageBox()
    box.setText('Верно!')
    box.exec_()
def show_lose():
    boxl = QMessageBox()
    boxl.setText('Не верно!')
    boxl.exec_()

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn4, alignment = Qt.AlignCenter)

layout_main = QVBoxLayout()

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)

btn1.clicked.connect(show_lose)
btn2.clicked.connect(show_lose)
btn3.clicked.connect(show_lose)
btn4.clicked.connect(show_win)

main_win.setLayout(layout_main)
main_win.show()
app.exec_()
