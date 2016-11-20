import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar, QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):      
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
 
        self.btn = QPushButton('Поехали', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)
 
        self.timer = QBasicTimer()
        self.step = 0
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Твоя жизнь')
        self.show()
        
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Мертв')
            return
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Поехали')
        else:
            self.timer.start(50, self)
            self.btn.setText('Пауза')
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())