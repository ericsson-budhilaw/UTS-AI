# Aplikasi Pendeteksian Gejala Virus Corona (COVID-19)

class Diagnose:
    percentage = 0

    def yesorno(self, question, utama=0):
        prompt = f'{question} ? (y/n): '
        ans = input(prompt).strip().lower()
        if ans not in ['y', 'n']:
            print(f'{ans} is invalid, please only use y and n to answer the question.')
            return self.yesorno(question)
        if ans == 'y':
            self.percentage += 1 + utama
        return False

    def affected(self):
        print("======================")
        print("Hasil")
        print("======================")

        affect = round(self.percentage / 9 * 100)

        if affect > 100:
            print(f"Anda kemungkinan terpapar oleh Covid-19 100%, berdasarkan dari jawaban yang anda berikan")
        elif affect > 50:
            print(f"Anda kemungkinan terpapar oleh Covid-19 {affect}%, berdasarkan dari jawaban yang anda berikan")
        else:
            print(f"Anda kemungkinan tidak terpapar oleh Covid-19 dengan akurasi jawaban anda {affect}%")


diag = Diagnose()

print("=================================")
print("Jawab semua pertanyaan dengan y/n")
print("=================================")

# Referensi pertanyaan: https://www.alodokter.com/virus-corona
# Gejala utama maka diberikan poin tambahan 2
# Jika pasien mengalami gejala dibawah ini kemungkinan besar terpapar Covid-19
diag.yesorno("Mengalami demam (suhu tubuh diatas 38 derajat celcius): ", 2)
diag.yesorno("Mengalami batuk kering: ", 2)
diag.yesorno("Mengalami sesak nafas: ", 2)

print("=================================")
print("Gejala lain")
print("=================================")

diag.yesorno("Mengalami diare: ")
diag.yesorno("Mengalami sakit kepala: ")
diag.yesorno("Konjungtivitis (Mata memerah): ")
diag.yesorno("Hilangnya kemampuan untuk mengecap rasa: ")
diag.yesorno("Hilangnya kemampuan untuk mencium bau (anosmia): ")
diag.yesorno("Muncul ruam di kulit: ")

diag.affected()

print("=================================")
print("Informasi Tambahan")
print("=================================")
print("Untuk informasi lebih lengkap dan akurat, harap konsultasi ke dokter atau rumah sakit.")
