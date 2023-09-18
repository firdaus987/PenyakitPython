import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton, QMessageBox

class EyeDiseaseDiagnosis(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sistem Pakar Penyakit Mata')
        self.setGeometry(100, 100, 400, 400)

        self.symptoms = {
            "G01": "Pandangan kabur saat melihat objek" ,
            "G02": "Sering menyipitkan mata",
            "G03": "Sakit kepala",
            "G04": "Mata lelah",
            "G05": "Sering menggosok mata",
            "G06": "Frekuensi mengedipkan mata yang berlebihan",
            "G07": "Melihat objek jauh terlihat jelas",
            "G08": "Melihat objek dekat terlihat buram",
            "G09": "Mengerlingkan mata untuk melihat objek jelas",
            "G10": "Kesulitan Membaca",
            "G11": "Mata terasa panas dan gatal",
            "G12": "Distorsi penglihatan",
            "G13": "Pandangan samar",
            "G14": "Sulit melihat saat malam hari",
            "G15": "Mata sering tegang dan mudah lelah",
            "G16": "Sensitif pada sorotan cahaya",
            "G17": "Kesulitan membedakan warna yang mirip",
            "G18": "Penglihatan ganda",
            "G19": "Membutuhkan penerangan lebih saat membaca",
            "G20": "Sulit membaca huruf berukuran kecil"
        }

        self.diseases = {
            "Miopia": {"G01": 0.25, "G03": 0.25, "G04": 0.25, "G05": 0.25, "G06": 0.25},
            "Hipermetropia": {"G03": 0.3, "G07": 0.3, "G08": 0.3, "G09": 0.3, "G10": 0.3, "G11": 0.3 },
            "Astigmatisma": {"G02": 0.4, "G03": 0.4, "G12": 0.4, "G13": 0.4, "G14": 0.4, "G15": 0.4, "G16": 0.4, "G18": 0.4},
            "Presbiopi": {"G01": 0.3, "G02": 0.3, "G03": 0.3, "G17": 0.3, "G19": 0.3, "G20": 0.3},
            # Tambahkan penyakit lainnya di sini
        }


        self.symptom_checkboxes = {}
        for symptom_code, symptom_desc in self.symptoms.items():
            checkbox = QCheckBox(symptom_desc)
            self.symptom_checkboxes[symptom_code] = checkbox

        self.diagnose_button = QPushButton('Diagnosa')
        self.diagnose_button.clicked.connect(self.diagnose)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Pilih Gejala:'))
        for checkbox in self.symptom_checkboxes.values():
            layout.addWidget(checkbox)
        layout.addWidget(self.diagnose_button)

        self.setLayout(layout)

    def diagnose(self):
        selected_symptoms = {}
        for code, checkbox in self.symptom_checkboxes.items():
            if checkbox.isChecked():
                selected_symptoms[code] = 1.0

        if not selected_symptoms:
            QMessageBox.warning(self, 'Peringatan', 'Pilih setidaknya satu gejala untuk melakukan diagnosa.')
            return

        disease_cf = {}
        for disease, disease_symptoms in self.diseases.items():
            cf = 1.0
            for symptom_code, symptom_cf in disease_symptoms.items():
                if symptom_code in selected_symptoms:
                    cf *= selected_symptoms[symptom_code] + symptom_cf * (1 - selected_symptoms[symptom_code])
                else:
                    cf *= 1 - symptom_cf
            disease_cf[disease] = cf

        max_disease = max(disease_cf, key=disease_cf.get)
        max_cf = disease_cf[max_disease]

        # Cari nilai keyakinan berdasarkan CF
        if max_cf < -0.8:
            confidence = 'Sangat tidak yakin'
        elif -0.8 <= max_cf < -0.4:
            confidence = 'Tidak Yakin'
        elif -0.4 <= max_cf < 0.4:
            confidence = 'Mungkin'
        elif 0.4 <= max_cf < 0.8:
            confidence = 'Yakin'
        else:
            confidence = 'Sangat Yakin'

        QMessageBox.information(self, 'Hasil Diagnosa', f'Berdasarkan gejala yang dipilih {confidence} anda terkena {max_disease} ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EyeDiseaseDiagnosis()
    ex.show()
    sys.exit(app.exec_())
