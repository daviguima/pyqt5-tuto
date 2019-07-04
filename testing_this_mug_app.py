# following this tuto: https://www.youtube.com/watch?v=FUlnu6DE1mI

import sys
from PyQt5.QtWidgets import QApplication, QWidget


def app():
    my_app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("testing this mug")
    w.show()
    sys.exit(my_app.exec_())


app()
