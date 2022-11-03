import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QDesktopWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('외출일지', self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titleFont = title.font()
        titleFont.setPointSize(20)
        title.setFont(titleFont)

        btn1 = QPushButton('기숙사생 명단 확인')
        btn2 = QPushButton('특정 기숙사생 상태 확인')
        btn3 = QPushButton('기숙사생 추가 / 삭제')
        btn4 = QPushButton('날짜 별 기숙사생 상태 확인')
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(title)
        vbox.addStretch(1)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('외출일지')
        self.resize(800, 600)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())