import sys
import random

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QLabel, QTextBrowser
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QBasicTimer, QEvent

UNACTIVE = "bo1.png"
GOOD = "bo2.png"
BAD = "bo3.png"



# class ClickableQLabel(QLabel):
 
#     def __init(self, parent):
#         QLabel.__init__(self, parent)
 
#     def mousePressEvent(self, ev):
#         self.emit(SIGNAL('clicked()'))


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
        # self.holes = []
        self.holesL = []

        k, n = 0, 0
        for i in range(6):
            # self.holes.append(QPixmap(UNACTIVE))
            self.holesL.append(QLabel('UNACTIVE',self))
            # self.holesL[i].setPixmap(self.holes[i])
            self.holesL[i].setPixmap(QPixmap(UNACTIVE))
            # self.holesL[i].mousePressEvent = self.boom
            self.holesL[i].installEventFilter(self)

            # self.holesL[i].clicked.connect(self.doAction)
            #self.connect(self.holesL[i], SIGNAL('clicked()'), self.boom)

            grid.addWidget(self.holesL[i], n, k)
            if k < 2:
                k = k + 1
            else:
                k = 0
                n += 1

        self.count = QLabel('0')
        self.time = QLabel('60')
        self.runBtn = QPushButton('Начать')
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

        if self.step >= 60:
            self.timer.stop()
            self.runBtn.setEnabled(True)
            return
        
        self.step = self.step + 1
        l = int(self.time.text()) - 1
        self.time.setText(str(l))
        

    def startGame(self):
        if self.timer.isActive():
            self.timer.stop()
            self.runBtn.setEnabled(True)
        else:
            self.timer.start(500, self)
            self.runBtn.setEnabled(False)

    def clearHim(self):
        self.holesL[self.now].setText('UNACTIVE')
        self.holesL[self.now].setPixmap(QPixmap(UNACTIVE))

    def showHim(self):
        number = random.randint(0,5)
        typ = random.randint(0,1)
        if typ:
            self.holesL[number].setText('BAD')
            self.holesL[number].setPixmap(QPixmap(BAD))
        else:
            self.holesL[number].setText('GOOD')
            self.holesL[number].setPixmap(QPixmap(GOOD)) 

        self.now = number

    def eventFilter(self, source, event):
        # print(event.type())
        if event.type() == QEvent.MouseButtonPress:
            print("The sender is:", source.text())
        return super().eventFilter(source, event)





 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myWindow()
    sys.exit(app.exec_())