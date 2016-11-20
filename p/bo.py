import sys
import random

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QBasicTimer


class myWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        self.holes = []
        self.holesL = []

        k = 0
        for i in range(6):
            
            self.holes.append(QPixmap("piq.png"))
            self.holesL.append(QLabel('1',self))
            grid.addWidget(self.holesL[i], k, i)
            k = k + 1 if k < 3 else 0


        self.setLayout(grid) 
        self.setGeometry(300, 300, 650,650)
        self.setWindowTitle('Крутец')    
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myWindow()
    sys.exit(app.exec_())