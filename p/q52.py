import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):      
        self.btn = QPushButton('Беги', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.runAway)
        
        self.i = 22
        self.le = QLineEdit(self)
        self.le.move(130, self.i)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Диалог ввода')
        self.show()
        
        
    def runAway(self):
        self.i += 5
        self.le.move(130, self.i)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())