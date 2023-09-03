"""
import sys
from PyQt5.QtWidgets import *
from anaekran_ui import Ui_Anaekran

class AnaekranPenceresi(QWidget,Ui_Anaekran):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AnaekranPenceresi()
    pencere.show()
    sys.exit(app.exec_())
"""
