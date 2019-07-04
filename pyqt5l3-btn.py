import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton(w)
    l = QtWidgets.QLabel(w)
    b.setText("Push me!")
    l.setText("Look at me!")
    w.setWindowTitle("PyQt5 lessons 4 and 5")
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)
    v_box.addWidget(l)
    w.setLayout(v_box)
    #b.move(100, 50)
    #l.move(110, 100)
    #w.setGeometry(100, 100, 300, 200)
    w.show()
    sys.exit(app.exec_())


window()
