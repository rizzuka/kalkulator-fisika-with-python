# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 411, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.brpkecepatan = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.brpkecepatan.setObjectName("brpkecepatan")
        self.gridLayout.addWidget(self.brpkecepatan, 2, 1, 1, 1)
        self.brpwaktu = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.brpwaktu.setObjectName("brpwaktu")
        self.gridLayout.addWidget(self.brpwaktu, 1, 1, 1, 1)
        self.hitung = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hitung.setFont(font)
        self.hitung.setObjectName("hitung")
        self.gridLayout.addWidget(self.hitung, 3, 1, 1, 1)
        self.hapus = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hapus.setFont(font)
        self.hapus.setObjectName("hapus")
        self.gridLayout.addWidget(self.hapus, 3, 0, 1, 1)
        self.brpjarak = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.brpjarak.setObjectName("brpjarak")
        self.gridLayout.addWidget(self.brpjarak, 0, 1, 1, 1)
        self.labeljarak = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labeljarak.setFont(font)
        self.labeljarak.setAlignment(QtCore.Qt.AlignCenter)
        self.labeljarak.setObjectName("labeljarak")
        self.gridLayout.addWidget(self.labeljarak, 0, 0, 1, 1)
        self.labelwaktu = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelwaktu.setFont(font)
        self.labelwaktu.setAlignment(QtCore.Qt.AlignCenter)
        self.labelwaktu.setObjectName("labelwaktu")
        self.gridLayout.addWidget(self.labelwaktu, 1, 0, 1, 1)
        self.labelkecepatan = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelkecepatan.setFont(font)
        self.labelkecepatan.setAlignment(QtCore.Qt.AlignCenter)
        self.labelkecepatan.setObjectName("labelkecepatan")
        self.gridLayout.addWidget(self.labelkecepatan, 2, 0, 1, 1)
        self.judul = QtWidgets.QLabel(self.centralwidget)
        self.judul.setGeometry(QtCore.QRect(10, 19, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.judul.setFont(font)
        self.judul.setAlignment(QtCore.Qt.AlignCenter)
        self.judul.setObjectName("judul")
        self.labelket = QtWidgets.QLabel(self.centralwidget)
        self.labelket.setGeometry(QtCore.QRect(10, 290, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setItalic(True)
        self.labelket.setFont(font)
        self.labelket.setAlignment(QtCore.Qt.AlignCenter)
        self.labelket.setObjectName("labelket")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Menghubungkan tombol dengan fungsi
        self.hitung.clicked.connect(self.hitung_glb)
        self.hapus.clicked.connect(self.hapusInput)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hitung.setText(_translate("MainWindow", "HITUNG"))
        self.hapus.setText(_translate("MainWindow", "HAPUS"))
        self.labeljarak.setText(_translate("MainWindow", "Jarak (m)"))
        self.labelwaktu.setText(_translate("MainWindow", "Waktu (s)"))
        self.labelkecepatan.setText(_translate("MainWindow", "Kecepatan (m/s)"))
        self.judul.setText(_translate("MainWindow", "Gerak Lurus Beraturan (GLB)"))
        self.labelket.setText(_translate("MainWindow", "Ket : Kosongkan salah satu!"))

    def hitung_glb(self):
        try:
            waktu_text = self.brpwaktu.text()
            kecepatan_text = self.brpkecepatan.text()
            jarak_text = self.brpjarak.text()

            if not waktu_text and not kecepatan_text:
                self.brpjarak.setText("MASUKAN ANGKA!")
                self.brpkecepatan.setText("MASUKAN ANGKA!")
                self.brpwaktu.setText("MASUKAN ANGKA!")
                return

            if waktu_text and kecepatan_text:
                waktu = float(waktu_text)
                kecepatan = float(kecepatan_text)
                jarak = waktu * kecepatan
                self.brpjarak.setText(f"{jarak:.2f}")

            elif waktu_text and not kecepatan_text:
                waktu = float(waktu_text)
                jarak = float(jarak_text)
                kecepatan = jarak / waktu
                self.brpkecepatan.setText(f"{kecepatan:.2f}")

            elif kecepatan_text and not waktu_text:
                kecepatan = float(kecepatan_text)
                jarak = float(jarak_text)
                waktu = jarak / kecepatan
                self.brpwaktu.setText(f"{waktu:.2f}")

        except ValueError:
            self.brpjarak.setText("MASUKAN ANGKA!")
            self.brpkecepatan.setText("MASUKAN ANGKA!")
            self.brpwaktu.setText("MASUKAN ANGKA!")

    def hapusInput(self):
        self.brpwaktu.clear()
        self.brpkecepatan.clear()
        self.brpjarak.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
