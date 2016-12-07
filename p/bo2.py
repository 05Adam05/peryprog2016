import sys
import random

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QLabel, QTextBrowser, QToolButton
from PyQt5.QtGui import  QIcon, QFont
from PyQt5.QtCore import QBasicTimer, QSize

UNACTIVE = "bo1.png"
GOOD = "bo3.png"
BAD = "bo2.png"
TIME = 30


class myWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):

        self.now = 0

        self.timer = QBasicTimer()
        self.step = 0



        grid = QGridLayout()
        grid.setSpacing(10)
       
        self.holesL = []

        k, n = 0, 0
        for i in range(6):
            self.holesL.append(QPushButton('U',self))
            self.holesL[i].setFlat(True)
            self.holesL[i].setAutoFillBackground(True)
            self.holesL[i].setIcon(QIcon(UNACTIVE))
            self.holesL[i].setIconSize(QSize(200,200))
            
            # self.holesL[i].installEventFilter(self)

            self.holesL[i].clicked.connect(self.doAction)

            grid.addWidget(self.holesL[i], n, k)
            if k < 2:
                k = k + 1
            else:
                k = 0
                n += 1

        font = QFont('Serif', 15, QFont.Light)
        self.count = QLabel('0')
        self.count.setFont(font)
        self.time = QLabel(str(TIME))
        self.time.setFont(font)
        self.runBtn = QPushButton('Начать')
        self.runBtn.setFont(font)
        grid.addWidget(self.count,6,0)
        grid.addWidget(self.time,6,1)
        grid.addWidget(self.runBtn,6,2)

        self.runBtn.clicked.connect(self.startGame)
        
        self.setLayout(grid) 
        self.setGeometry(300, 300, 650,650)
        self.setWindowTitle('Крутец')    
        self.show()

    def timerEvent(self, e):
        self.clearHim()
        self.showHim()

        if self.step >= TIME * 2:
            self.timer.stop()
            self.runBtn.setEnabled(True)
            self.time.setText(str(TIME))
            self.step = 0
            self.clearHim()
            return
        
        self.step += 1
        if self.step % 2:
            l = int(self.time.text()) - 1
            self.time.setText(str(l))
        

    def startGame(self):
        if self.timer.isActive():
            self.timer.stop()
            self.runBtn.setEnabled(True)
        else:
            self.timer.start(500, self)
            self.count.setText("0")
            self.runBtn.setEnabled(False)

    def clearHim(self):
        self.holesL[self.now].setText('U')
        self.holesL[self.now].setIcon(QIcon(UNACTIVE))

    def showHim(self):
        number = random.randint(0,5)
        typ = random.randint(0,1)
        if typ:
            self.holesL[number].setText('B')
            self.holesL[number].setIcon(QIcon(BAD))
        else:
            self.holesL[number].setText('G')
            self.holesL[number].setIcon(QIcon(GOOD)) 

        self.now = number

    def doAction(self):
        sender = self.sender()
        if sender.text() == 'B':
            count = int(self.count.text()) + 1
            self.count.setText(str(count))
        if sender.text() == 'G':
            count = int(self.count.text()) - 1
            self.count.setText(str(count))



 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myWindow()
    sys.exit(app.exec_())