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
            "Miopia": {"G01": 0.38, "G03": 0.07, "G04": 1.0, "G05": 1.0, "G06": 1.0},
            "Hipermetropia": {"G03": -0.01, "G07": 1.0, "G08": 1.0, "G09": 1.0, "G10": 1.0, "G11": 1.0 },
            "Astigmatisma": {"G02": 0.24, "G03": -0.13, "G12": 1.0, "G13": 1.0, "G14": 1.0, "G15": 1.0, "G16": 1.0, "G18": 1.0},
            "Presbiopi": {"G01": 0.36, "G02": 0.04, "G03": 0.04, "G17": 1.0, "G19": 1.0, "G20": 1.0},
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
        else :
            confidence = 'Sangat Yakin'

        QMessageBox.information(self, 'Hasil Diagnosa', f'Berdasarkan gejala yang dipilih {confidence} anda terkena {max_disease} ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EyeDiseaseDiagnosis()
    ex.show()
    sys.exit(app.exec_())
