import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel
 
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        lbl = QLabel('Выбери судьбу', self)
        lbl.move(50, 20)  
        btn1 = QPushButton("ЛОХ", self)
        btn1.move(30, 50)
        btn2 = QPushButton("Дурак", self)
        btn2.move(150, 50)
      
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
        
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage('Ты '+sender.text())
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())