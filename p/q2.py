import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QTextEdit
from PyQt5.QtGui import QIcon

class myWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        exitAction = QAction(QIcon('image.png'),'&Выход', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Выйти')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar()

        fullAction = QAction(QIcon('loh2.png'),'&Туфта', self)        
        fullAction.setShortcut('Ctrl+P')
        fullAction.triggered.connect(self.full)
        fullAction.setStatusTip('Ниче не делать')
        self.statusBar()



        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')
        fileMenu.addAction(fullAction)
        fileMenu.addAction(exitAction)


        self.statusBar().showMessage('Поехали')
        self.setGeometry(300, 300, 450, 250)
        self.setWindowTitle('Менюха')    
        self.show()

    def full(self):
        print('Ничего не происходит')
        self.textEdit.append('Ничего не происходит')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myWindow()
    sys.exit(app.exec_())