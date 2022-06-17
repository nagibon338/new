from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from variabels import *
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_w,win_h)
    def initUI(self):
        self.family = QLabel(txt_family)
        self.family_input = QLineEdit(txt_family_input)
        self.age = QLabel(txt_age)
        self.age_input = QLabel(txt_age_input)
        
    def connects(self):
    def next_click(self):
        self.hide()
    