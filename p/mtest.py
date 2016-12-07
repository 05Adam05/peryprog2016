import sys
from PyQt5.QtWidgets import QMainWindow,QWidget, QAction, qApp, QApplication, QTextEdit, QFileDialog, QLabel, QCheckBox, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):


        exitAction = QAction('&Выход', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Выйти')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar()

        fullAction = QAction('&Открыть тест', self)        
        fullAction.setShortcut('Ctrl+O')
        fullAction.triggered.connect(self.openTest)
        fullAction.setStatusTip('Открыть тест')
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')
        fileMenu.addAction(fullAction)
        fileMenu.addAction(exitAction)


        grid = QGridLayout()
        grid.setSpacing(10)

        self.question = QLabel()
        grid.addWidget(self.question,0,0)
        self.answers = []
        self.answers.append(QCheckBox())
        grid.addWidget(self.answers[0],1,0)
        self.answers.append(QCheckBox())
        grid.addWidget(self.answers[1],1,1)
        self.answers.append(QCheckBox())
        grid.addWidget(self.answers[2],2,0)
        self.answers.append(QCheckBox())
        grid.addWidget(self.answers[3],2,1)
        self.nextButtton = QPushButton()
        self.nextButtton.clicked.connect(self.goNext)
        grid.addWidget(self.nextButtton,3,1)

        self.myWidg = QWidget()
        self.myWidg.hide()
        self.myWidg.setLayout(grid)
        self.setCentralWidget(self.myWidg)

        self.endWidg = QLabel()

        self.setGeometry(300, 300, 450, 250)
        self.setWindowTitle('Мегатест')    
        self.show()

    def openTest(self):
        fname = QFileDialog.getOpenFileName(self, 'Открыть файл', '.')
        self.test = []
        with open(fname[0], 'r', encoding='utf-8') as f:        
            for line in f:
                self.test.append(line)

        self.counts = int(self.test[0])
        self.currentQuestion = 1
        self.line = 1
        self.rightCounts = 0
        print(self.counts)

        self.goNext()
        self.myWidg.show()




    def goNext(self):
        if self.currentQuestion > 1:
            right = 0
            for canswer in self.answers:
                if canswer.isChecked():
                    if canswer.text() in self.rightAnswers:
                        right += 1
                    else:
                        right = 0
                        break
            print('right',right)
            if right == len(self.rightAnswers):
                self.rightCounts += 1
            print(self.rightCounts)

        if self.currentQuestion > self.counts:
            self.myWidg.hide()
            self.endWidg.setText('Твой результат: '+str(self.rightCounts)+'/'+str(self.counts))
            self.setCentralWidget(self.endWidg)
            return

        l = self.line
        self.question.setText(self.test[l])
        answers = self.test[l+1][:-1].split(', ')
        for canswer, answer in zip(self.answers, answers):
            canswer.setText(answer)
        self.rightAnswers = self.test[l+2][:-1].split(', ')
        # print(rightAnswers)
        self.line += 3
        self.currentQuestion += 1


 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myWindow()
    sys.exit(app.exec_())