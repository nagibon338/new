from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from instr import *
from final_win import *
from PyQt5.QtGui import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(title_text)
        self.resize(win_w,win_h)
        self.move(win_x,win_y)
    def initUI(self):
        self.tfio = QLabel(txt_tfio)
        self.fio = QLineEdit(txt_fio)
        self.tyo = QLabel(txt_tyo)
        self.yo = QLineEdit(txt_yo)
        self.instr1 = QLabel(txt_instr1)
        self.but1 = QPushButton(txt_but1)
        self.hearth1 = QLineEdit(txt_hearth1)
        self.instr2 = QLabel(txt_instr2)
        self.but2 = QPushButton(txt_but2)
        self.instr3 = QLabel(txt_instr3)
        self.but3 = QPushButton(txt_but3)
        self.hearth11 = QLineEdit(txt_hearth11)
        self.hearth12 = QLineEdit(txt_hearth12)
        self.final_but = QPushButton(txt_final_but)
        self.timer_lab = QLabel(txt_timer)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tfio,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.fio,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.tyo,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yo,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instr1,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.but1,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.hearth1,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instr2,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.but2,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.timer_lab,alignment = Qt.AlignRight)
        self.layout.addWidget(self.instr3,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.but3,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.hearth11,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.hearth12,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.final_but,alignment = Qt.AlignCenter)
        self.setLayout(self.layout)
    def connects(self):
        self.final_but.clicked.connect(self.next_click)
        self.but1.clicked.connect(self.timer1_save)
        self.but2.clicked.connect(self.timer2_save)
        self.but3.clicked.connect(self.timer3_save)

    def next_click(self):
        self.ew = EndWin()
        self.hide()
    def timer1_save(self):
        global time
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_lab.setText(time.toString('hh:mm:ss'))
        self.timer_lab.setFont(QFont('Times',36,QFont.Bold))
        self.timer_lab.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') <= '00:00:00':
            self.timer.stop()
    
    def timer2_save(self):
        global time
        time = QTime(0,0,45)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1000)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_lab.setText(time.toString('hh:mm:ss'))
        self.timer_lab.setFont(QFont('Times',36,QFont.Bold))
        self.timer_lab.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') <= '00:00:00':
            self.timer.stop()
    def timer3_save(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_lab.setText(time.toString('hh:mm:ss'))
        self.timer_lab.setFont(QFont('Times',36,QFont.Bold))
        self.timer_lab.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') <= '00:00:00':
            self.timer.stop()

