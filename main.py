import sys

from PyQt6.QtWidgets import QWidget, QApplication

from layout import Ui_Dialog


class myForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myForm()
    sys.exit(app.exec())