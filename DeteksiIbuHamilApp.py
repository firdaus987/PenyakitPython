import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
            # Inisialisasi daftar gejala penyakit
    def __init__(self):
        self.gejala_penyakit = {
            'G01': {'nama': 'Pandangan kabur saat melihat objek', 'nilai_pakar': 0.8},
            'G02': {'nama': 'Sering menyipitkan mata', 'nilai_pakar': 0.8},
            'G03': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G04': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G05': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G06': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G07': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G08': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G09': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G10': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G11': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G12': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G13': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G14': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G15': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G16': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G17': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G18': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G19': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
            'G20': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        }
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_judul = QtWidgets.QLabel(self.centralwidget)
        self.label_judul.setGeometry(QtCore.QRect(0, 0, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_judul.setFont(font)
        self.label_judul.setAlignment(QtCore.Qt.AlignCenter)
        self.label_judul.setObjectName("label_judul")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(15, 90, 391, 351))
        self.listWidget.setObjectName("listWidget")
        self.ButtonPeriksa = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonPeriksa.setGeometry(QtCore.QRect(170, 450, 75, 23))
        self.ButtonPeriksa.setObjectName("ButtonPeriksa")
        self.label_hasil = QtWidgets.QLabel(self.centralwidget)
        self.label_hasil.setGeometry(QtCore.QRect(10, 479, 411, 20))
        self.label_hasil.setText("")
        self.label_hasil.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hasil.setObjectName("label_hasil")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 251, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # self.gejala_penyakit = {
        #     'G01': 'Pandangan kabur saat melihat objek',
        #     'G02': 'Sering menyipitkan mata',
        #     'G03': 'Sakit kepala',
        #     'G04': 'Mata lelah',
        #     'G05': 'Sering menggosok mata',
        #     'G06': 'Frekuensi mengedipkan mata yang berlebihan',
        #     'G07': 'Melihat objek jauh terlihat jelas',
        #     'G08': 'Melihat objek dekat terlihat buram',
        #     'G09': 'Mengerlingkan mata untuk melihat objek jelas',
        #     'G10': 'Kesulitan membaca',
        #     'G11': 'Mata terasa panas dan gatal',
        #     'G12': 'Distorsi penglihatan',
        #     'G13': 'Pandangan samar',
        #     'G14': 'Sulit melihat saat malam hari',
        #     'G15': 'Mata sering tegang dan mudah lelah',
        #     'G16': 'Sensitif pada sorotan cahaya',
        #     'G17': 'Kesulitan membedakan warna yang mirip',
        #     'G18': 'Penglihatan ganda',
        #     'G19': 'Membutuhkan penerangan lebih saat membaca',
        #     'G20': 'Sulit membaca huruf berukuran kecil'
        # }
        
                    
        # Inisialisasi data penyakit dan nilai Certainty Factor (CF)
        self.penyakit = {
            'P01': {'nama': 'Miopia', 'gejala': ['G01', 'G04', 'G05', 'G06']},
            'P02': {'nama': 'Hipermetropia', 'gejala': ['G02', 'G03', 'G04']},
            'P03': {'nama': 'Astigmatisma', 'gejala': ['G01', 'G03']},
            'P04': {'nama': 'Presbiopi', 'gejala': ['G02', 'G04']}
        }

        # Inisialisasi daftar gejala pasien
        self.gejala_pasien = {
            'G03': 0.2,
            'G04': 0.4,
            'G01': 0.5,
            'G05': 0.8,
            'G02': 0.3,
        }
        
        # Inisialisasi daftar gejala penyakit
        # self.gejala_penyakit = {
        #     'G01': {'nama': 'Pandangan kabur saat melihat objek', 'nilai_pakar': 0.8},
        #     'G02': {'nama': 'Sering menyipitkan mata', 'nilai_pakar': 0.8},
        #     'G03': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G04': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G05': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G06': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G07': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G08': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G09': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G10': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G11': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G12': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G13': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G14': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G15': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G16': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G17': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G18': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G19': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        #     'G20': {'nama': 'Sakit kepala', 'nilai_pakar': 0.8},
        # }
   
        # Menghubungkan tombol "PERIKSA" ke fungsi periksa_penyakit
        self.ButtonPeriksa.clicked.connect(self.periksa_penyakit)
            
            # Inisialisasi data penyakit dan nilai Certainty Factor (CF)
        self.penyakit = {
            'P01': {'nama': 'Miopia', 'gejala': ['G01', 'G04', 'G05', 'G06']},
            'P02': {'nama': 'Hipermetropia', 'gejala': ['G02', 'G03', 'G04']},
            'P03': {'nama': 'Astigmatisma', 'gejala': ['G01', 'G03']},
            'P04': {'nama': 'Presbiopi', 'gejala': ['G02', 'G04']}
        }

        # Inisialisasi daftar gejala pasien
        self.gejala_pasien = {
            'G03': 0.2,
            'G04': 0.4,
            'G01': 0.5,
            'G05': 0.8,
            'G02': 0.3,
        }
        

        
        # Menambahkan daftar gejala penyakit ke QListWidget
        for key, value in gejala_penyakit.items():
            item = QtWidgets.QListWidgetItem(f'{value}')
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)  # Menambahkan kotak centang
            item.setCheckState(QtCore.Qt.Unchecked)  # Awalnya tidak tercentang
            self.listWidget.addItem(item)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Deteksi Penyakit Refraksi Mata"))
        self.label_judul.setText(_translate("MainWindow", "Deteksi Penyakit Refraksi Mata"))
        self.label_judul.setStyleSheet("color: blue;")
        self.ButtonPeriksa.setText(_translate("MainWindow", "PERIKSA"))
        self.label.setText(_translate("MainWindow", "Pilih gejala yang anda rasakan:"))
        self.label_2.setStyleSheet("color: green;")
        self.label_2.setText(_translate("MainWindow", "dr. A4, Ph.D"))
        
  

    def periksa_penyakit(self):
        # Logika perhitungan penyakit (seperti yang Anda definisikan sebelumnya)
        hasil_penyakit = {}

        for kode_penyakit in gejala_penyakit.keys():
            gejala_penyakit = gejala_penyakit[kode_penyakit]['gejala']
            cf_penyakit = []

            for kode_gejala in gejala_penyakit:
                if kode_gejala in self.gejala_pasien and self.gejala_pasien[kode_gejala]:
                    nilai_gejala = self.gejala_pasien[kode_gejala]
                    nilai_pakar = self.gejala[kode_gejala]['nilai_pakar']
                    cf_gejala = self.hitung_cf(nilai_gejala, nilai_pakar)
                    cf_penyakit.append(cf_gejala)

            cf_hasil = cf_penyakit[0]
            for i in range(1, len(cf_penyakit)):
                cf_hasil = cf_hasil + cf_penyakit[i] * (1 - cf_hasil)

            hasil_penyakit[kode_penyakit] = cf_hasil

        hasil_penyakit = sorted(hasil_penyakit.items(), key=lambda x: x[1], reverse=True)
        for kode_penyakit, cf in hasil_penyakit:
            nama_penyakit = penyakit[kode_penyakit]['nama']
            self.label_hasil.setText(f"Diagnosa penyakit berdasarkan gejala yang dipilih adalah: {nama_penyakit} ({cf * 100:.2f}%)")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
