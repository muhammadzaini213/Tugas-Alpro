from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])
window = QMainWindow()
window.setGeometry(500, 100, 500, 500)
window.setWindowTitle("Tabel Barang dan Harga")

labelBarang = QLabel(window)
labelBarang.setText("Masukkan Barang")
labelBarang.setLineWidth(300)
labelBarang.move(20,20)

inputBarang = QLineEdit(window)
inputBarang.setFixedWidth(300)
inputBarang.move(20,50)

labelHarga = QLabel(window)
labelHarga.setText("Masukkan Harga")
labelHarga.setLineWidth(300)
labelHarga.move(20,80)


tabel = QTableWidget(window)
tabel.setColumnCount(2)
tabel.setHorizontalHeaderLabels(["Barang", "Harga"])
tabel.setFixedWidth(230)
tabel.setFixedHeight(500)
tabel.move(20, 190)

inputHarga = QLineEdit(window)
inputHarga.setFixedWidth(300)
inputHarga.move(20,110)


def tambahItem():
    row = tabel.rowCount()
    tabel.insertRow(row)

    if(inputHarga.text().isnumeric and inputHarga.text() != "" and inputBarang.text() != ""):
        tabel.setItem(row, 1, QTableWidgetItem(inputHarga.text()))
        tabel.setItem(row, 0, QTableWidgetItem(inputBarang.text()))
    else:
        QMessageBox.warning(window, "Input Error", "Data tidak valid")

def test():
    print("S")

enterBtn = QPushButton(window)
enterBtn.setText("Enter")
enterBtn.move(20, 150)
enterBtn.setFixedWidth(70)
enterBtn.clicked.connect(tambahItem)


window.show()
app.exec()


