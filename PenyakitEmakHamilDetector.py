class PenyakitWongMeteng:
    def __init__(self):
        # Inisialisasi gejala penyakit dan nilai Certainty Factor (CF)
        self.gejala_penyakit = {
            'G01': 'Pandangan kabur saat melihat objek',
            'G02': 'Sering menyipitkan mata',
            'G03': 'Sakit kepala',
            'G04': 'Mata lelah',
            'G05': 'Sering menggosok mata',
            'G06': 'Frekuensi mengedipkan mata yang berlebihan',
            'G07': 'Melihat objek jauh terlihat jelas',
            'G08': 'Melihat objek dekat terlihat buram',
            'G09': 'Mengerlingkan mata untuk melihat objek jelas',
            'G10': 'Kesulitan membaca',
            'G11': 'Mata terasa panas dan gatal',
            'G12': 'Distorsi penglihatan',
            'G13': 'Pandangan samar',
            'G14': 'Sulit melihat saat malam hari',
            'G15': 'Mata sering tegang dan mudah lelah',
            'G16': 'Sensitif pada sorotan cahaya',
            'G17': 'Kesulitan membedakan warna yang mirip',
            'G18': 'Penglihatan ganda',
            'G19': 'Membutuhkan penerangan lebihsaat membaca',
            'G20': 'Sulit membaca huruf berukuran kecil'
        }
        
        # Inisialisasi data penyakit dan nilai Certainty Factor (CF)
        self.data_penyakit = {
            'Penyakit Miopia ': {'G01': 0.8, 'G03': -0.6, 'G04': -0.6, 'G05': 0.4, 'G06': -0.4},
            'Penyakit Hipermetropia ': {'G03': 0.6, 'G07': 0.8, 'G08': 0.4, 'G09': -0.6, 'G10': 0.8, 'G11': -0.4},
            'Penyakit Astigmatisma ': {'G02': 0.8, 'G03': -0.4, 'G12': -0.6, 'G13': -0.8, 'G14': -0.6, 'G15': -0.8, 'G16': -0.6, 'G18': -0.8},
            'Penyakit Presbiopi ': {'G01': 0.4, 'G02': -0.6, 'G03': -0.4, 'G17': -0.8, 'G19': -0.6, 'G20': -0.8}
        }

    def detect_penyakit(self, gejala):
        total_CF = {}
        
        # Menghitung Certainty Factor (CF) untuk setiap jenis penyakit
        for penyakit, gejala_penyakit in self.data_penyakit.items():
            CF_penyakit = 1
            for gejala, nilai_CF in gejala_penyakit.items():
                if gejala in gejala:
                    CF_penyakit *= nilai_CF
            total_CF[penyakit] = CF_penyakit

        # Menentukan jenis penyakit dengan CF tertinggi
        max_CF = max(total_CF, key=total_CF.get)
        return max_CF

    def get_gejala_penyakit(self):
        return self.gejala_penyakit

if __name__ == "__main__":
    detector = PenyakitWongMeteng()
    print("Daftar Gejala:")
    gejala_penyakit = detector.get_gejala_penyakit()
    for kode, gejala in gejala_penyakit.items():
        print(f"{kode}: {gejala}")

    gejala_input = input("Masukkan gejala (pisahkan dengan koma): ")
    gejala_input = gejala_input.split(',')
    
    penyakit_terdeteksi = detector.detect_penyakit(gejala_input)
    
    print(f"Diagnosa berdasarkan gejala yang Anda input adalah: {penyakit_terdeteksi}")
