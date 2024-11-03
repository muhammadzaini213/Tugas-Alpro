from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])
window = QMainWindow()
window.setGeometry(500, 100, 500, 500)
window.setWindowTitle("Tabel Barang dan Harga")

grid = QGridLayout()
labelBarang = QLabel(window)
labelBarang.setText("Masukkan Barang")

inputBarang = QLineEdit(window)

labelHarga = QLabel(window)
labelHarga.setText("Masukkan Harga")


tabel = QTableWidget(window)
tabel.setColumnCount(2)
tabel.setHorizontalHeaderLabels(["Barang", "Harga"])

inputHarga = QLineEdit(window)


def tambahItem():
    row = tabel.rowCount()

    if(inputHarga.text().isnumeric and inputHarga.text() != "" and inputBarang.text() != ""):
        tabel.insertRow(row)
        tabel.setItem(row, 1, QTableWidgetItem(inputHarga.text()))
        tabel.setItem(row, 0, QTableWidgetItem(inputBarang.text()))
    else:
        QMessageBox.warning(window, "Input Error", "Data tidak valid")

def test():
    print("S")

enterBtn = QPushButton(window)
enterBtn.setText("Enter")
enterBtn.clicked.connect(tambahItem)

grid.addWidget(labelBarang, 0,0)
grid.addWidget(labelHarga, 0, 1)
grid.addWidget(inputBarang, 1, 0)
grid.addWidget(inputHarga, 1,1)
grid.addWidget(enterBtn, 3, 0, 1,3)
grid.addWidget(tabel, 4, 0, 1,4)

widget = QWidget()
widget.setLayout(grid)
window.setCentralWidget(widget)



window.show()
app.exec()


