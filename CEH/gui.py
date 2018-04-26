import sys
from PyQt5.QtWidgets import QDialog, QApplication
from youtube import Ui_Dialog


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


app = None


def main():

    global app
    app = QApplication(sys.argv)

    w = AppWindow()
    w.show()
    app.exec()


if __name__ == '__main__':
        main()

