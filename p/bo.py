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

        self.holes = []
        grid = QGridLayout()
        grid.setSpacing(10)
        
        for i in range(6):
            k = i
            self.holes.append(QPixmap("bo1.png"))
            grid.addWidget(self.holes[i], i, k)


        self.setLayout(grid) 
        self.setGeometry(300, 300, 650,650)
        self.setWindowTitle('Крутец')    
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myWindow()
    sys.exit(app.exec_())