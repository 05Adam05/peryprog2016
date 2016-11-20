import sys
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QGridLayout, QLineEdit, QTextEdit

class myWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # lbl1 = QLabel('Привет', self)
        # lbl1.move(15, 10)
        # lbl2 = QLabel('Привееет', self)
        # lbl2.move(35, 40)
        
        # lbl3 = QLabel('Привеееет', self)
        # lbl3.move(55, 70)

        # okButton = QPushButton("Да")
        # cancelButton = QPushButton("Отмена")
        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(okButton)
        # hbox.addWidget(cancelButton)
        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)
        
        # self.setLayout(vbox)    

        # grid = QGridLayout()
        # self.setLayout(grid)
 
        # names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']
        # positions = [(i,j) for i in range(5) for j in range(4)]
        # print(positions)
        
        # for position, name in zip(positions, names):
        #     if name == '':
        #         continue
        #     button = QPushButton(name)
        #     grid.addWidget(button, *position)

        # for i in range(5):
        #     for j in range(3):
        #         if i == 2 and j == 1:
        #             continue
        #         button = QPushButton("*")
        #         grid.addWidget(button, *(i, j))

        title = QLabel('Заголовок')
        author = QLabel('Автор')
        review = QLabel('Описание')
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        grid.addWidget(QLabel('Жизь боль'), 7, 0)
        
        
        self.setLayout(grid) 

        
        self.setGeometry(300, 300, 350,300)
        self.setWindowTitle('Крутец')    
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myWindow()
    sys.exit(app.exec_())