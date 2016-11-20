import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QTextEdit, QAction, QFileDialog, QApplication, QGridLayout, QHBoxLayout)
from PyQt5.QtGui import QIcon
 
class Example(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        grid = QGridLayout()  
        self.textEdit = QTextEdit()
        # self.setCentralWidget(self.textEdit)
        self.textEdit2 = QTextEdit()
        grid.addWidget(self.textEdit,1,0)
        grid.addWidget(self.textEdit2,1,1)

        
        self.statusBar()

        w = QWidget()
        w.setLayout(grid)
        self.setCentralWidget(w)
 
        openFile = QAction(QIcon('loh2.jpg'), 'Открыть', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Открыть новый файл')
        openFile.triggered.connect(self.showDialog)

        runFile = QAction(QIcon('loh2.jpg'), 'Выполнить', self)
        runFile.setShortcut('Ctrl+R')
        runFile.setStatusTip('Выполнить')
        runFile.triggered.connect(self.runF)
 
 
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')
        fileMenu.addAction(openFile)
        fileMenu = menubar.addMenu('&Выполнить')
        fileMenu.addAction(runFile)      
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('ФФайл')
        self.show()
        
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Открыть файл', '..')
        print(fname)
        
        with open(fname[0], 'r', encoding='utf-8') as f:        
            data = f.read()
            # print(data)
            self.textEdit.setText(data)

    def runF(self):
        e = exec(self.textEdit.toPlainText())
        self.textEdit2.setText(eval(self.textEdit.toPlainText()))
                                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())