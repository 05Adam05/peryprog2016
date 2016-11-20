import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QToolTip, QMessageBox, QDesktopWidget,QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setToolTip('Это виджет <b>QWidget</b>')
        
        btn = QPushButton('Кнопочка', self)
        btn.setToolTip('"Это виджет <b>QPushButton</b>')
        btn.resize(btn.sizeHint())
        # btn.resize(100,100)
        btn.move(50, 50)

        qbtn = QPushButton('Выход', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(btn.sizeHint())
        qbtn.move(150, 50)


        self.setGeometry(50,50,300,300)
        self.center()
        self.setWindowTitle('Тупость')
        self.setWindowIcon(QIcon('piq.png'))

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Внезапно', "Ты хочешь выйти?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()      




app = QApplication(sys.argv)
# w = QWidget()
# w.resize(250,150)
# w.move(300, 300)
# w.setWindowTitle('Ничесе')
# w.show()
w = myWindow()

sys.exit(app.exec_())