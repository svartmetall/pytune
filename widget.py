import sys

from PyQt5.QtWidgets import QWidget, QLCDNumber, QVBoxLayout, QApplication


class PyTuneWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        lcd = QLCDNumber(7)
        vbox = QVBoxLayout()

        vbox.addWidget(lcd)

        self.setLayout(vbox)
        self.setGeometry(200, 200, 400, 150)
        self.setWindowTitle('Audio frequency - PyTune')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = PyTuneWidget()
    sys.exit(app.exec_())
