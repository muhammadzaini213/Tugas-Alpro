from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])
window = QMainWindow()
window.setGeometry(500, 100, 500, 200)
window.setWindowTitle("Kalkulator")

grid = QGridLayout()


label = QLabel()
label.setText("Hasil")

hasil = QLineEdit()
hasil.setEnabled(False)

def addNumber(buttonLabel):
    hasil.setText(f"{hasil.text()}{buttonLabel}")

def tampilkanHasil(operasi):
    mOperasi = operasi
    mOperasi = mOperasi.replace("x","*")
    mOperasi =  mOperasi.replace("^","**")
    mOperasi = mOperasi.replace(" mod ","%")
    mOperasi = eval(mOperasi)
    hasil.setText(f"{mOperasi}")


button1 = QPushButton()
button1.setText("1")
button1.clicked.connect(lambda: addNumber("1"))

button2 = QPushButton()
button2.setText("2")
button2.clicked.connect(lambda: addNumber("2"))

button3 = QPushButton()
button3.setText("3")
button3.clicked.connect(lambda: addNumber("3"))

button4 = QPushButton()
button4.setText("4")
button4.clicked.connect(lambda: addNumber("4"))

button5 = QPushButton()
button5.setText("5")
button5.clicked.connect(lambda: addNumber("5"))

button6 = QPushButton()
button6.setText("6")
button6.clicked.connect(lambda: addNumber("6"))

button7 = QPushButton()
button7.setText("7")
button7.clicked.connect(lambda: addNumber("7"))

button8 = QPushButton()
button8.setText("8")
button8.clicked.connect(lambda: addNumber("8"))

button9 = QPushButton()
button9.setText("9")
button9.clicked.connect(lambda: addNumber("9"))

button0 = QPushButton()
button0.setText("0")
button0.clicked.connect(lambda: addNumber("0"))

buttonPlus = QPushButton()
buttonPlus.setText("+")
buttonPlus.clicked.connect(lambda: addNumber("+"))

buttonMinus = QPushButton()
buttonMinus.setText("-")
buttonMinus.clicked.connect(lambda: addNumber("-"))

buttonKali = QPushButton()
buttonKali.setText("x")
buttonKali.clicked.connect(lambda: addNumber("x"))

buttonBagi = QPushButton()
buttonBagi.setText("/")
buttonBagi.clicked.connect(lambda: addNumber("/"))

buttonPangkat = QPushButton()
buttonPangkat.setText("^")
buttonPangkat.clicked.connect(lambda: addNumber("^"))

buttonMod = QPushButton()
buttonMod.setText("mod")
buttonMod.clicked.connect(lambda: addNumber(" mod "))

buttonReset = QPushButton()
buttonReset.setText("C")
buttonReset.clicked.connect(lambda: hasil.setText(""))

buttonAns = QPushButton()
buttonAns.setText("=")
buttonAns.clicked.connect(lambda: tampilkanHasil(hasil.text()))

grid.addWidget(label, 0,0, 1, 1)
grid.addWidget(hasil, 1,0 , 1,4)

grid.addWidget(buttonPlus, 2,0)
grid.addWidget(buttonMinus, 2,1)
grid.addWidget(buttonKali, 2,2)
grid.addWidget(buttonBagi, 2,3)

grid.addWidget(button1, 3,0)
grid.addWidget(button2, 3,1)
grid.addWidget(button3, 3,2)
grid.addWidget(buttonPangkat, 3,3)

grid.addWidget(button4, 4,0)
grid.addWidget(button5, 4,1)
grid.addWidget(button6, 4,2)
grid.addWidget(buttonMod, 4,3)

grid.addWidget(button7, 5,0)
grid.addWidget(button8, 5,1)
grid.addWidget(button9, 5,2)
grid.addWidget(buttonReset, 5,3)

grid.addWidget(button0, 6, 0)
grid.addWidget(buttonAns, 6,3)

widget = QWidget()
widget.setLayout(grid)
window.setCentralWidget(widget)

window.show()
app.exec()
