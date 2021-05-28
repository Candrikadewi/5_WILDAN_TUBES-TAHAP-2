#memasukkan identitas
print("Selamat datang di Website Registrasi Vaksinasi COVID-19")
print("Mohon persiapkan data-data di bawah ini untuk keperluan registrasi:")
listdata = ['1. KTP','2. Surat kesehatan dari dokter bagi penderita penyakit kronis']

#menampilkan listdata keperluan
rose = 0
for win in range (0,2) :
    print (listdata[rose])
    rose+=1
konfir = str(input("Apakah semua data yang diperlukan sudah Anda siapkan? (Sudah/Belum):"))
konfir2 = konfir.title()

if konfir2=="Sudah" :
    print("Silakan mengisi identitas Anda dengan seksama dan jawablah pertanyaan sesuai dengan kondisi Anda saat ini")
    nama = str(input("Nama Lengkap="))
    nik = int(input("NIK="))
    nama_ayah= str(input("Nama Ayah="))
    nama_ibu= str(input("Nama Ibu="))
    print("Kelahiran:")
    tanggal = int(input("Tanggal Lahir="))
    bulan = int(input("Bulan Lahir="))
    tahun = int(input("Tahun Lahir="))
    lahir = tanggal + (bulan*30) + (tahun*365)

    print("Tanggal registrasi:")
    tanggalregist = int(input("Tanggal Registrasi="))
    bulanregist = int(input("Bulan Registrasi="))
    tahunregist = int(input("Tahun Registrasi="))
    registrasi = tanggalregist + (bulanregist * 30) + (tahunregist * 365)
    tahunusia = int((registrasi - lahir) / 365)
    bulanusia = int(((registrasi - lahir) % 365) / 30)
    hariusia  = int(((registrasi - lahir) % 365) % 30)
    print("Usia=",tahunusia,"tahun")

    if tahunusia >= 18:
        jk = str(input("Jenis Kelamin (P/L)="))
        if jk =="P":
                mengandung= str(input("Apakah anda sedang mengandung (Y/N)?"))
                if mengandung=="Y":
                    print("Maaf anda belum dapat mengikuti program vaksinasi dikarenakan sedang mengandung")
                else:
                    terpapar = str(input("Apakah Anda pernah terpapar covid dalam jangka waktu 3 bulan terakhir?(Y/N)"))
                if terpapar == "Y":
                    print("Maaf Anda belum dapat mengikuti program vaksinansi dikarenakan belum memenuhi persyaratan kesehatan")
                else:
                    riwayatsakit = str(input("Apakah Anda memiliki riwayat hipertensi atau penyakit kronis lain?(Y/N)"))
                    if riwayatsakit == "Y":
                        suratizin = str(input("Apakah Anda sudah mendapat surat layak vaksin dari dokter?(Y/N)"))
                        if suratizin == "N":
                            print("Mohon maaf Anda belum dapat mengikuti program vaksinasi dikarenakan belum"
                                              "memenuhi persyaratan kesehatan")
                        else:
                            vaksin= str(input("Apakah anda menerima vaksin lain dalam kurun waktu 1 bulan terakhir? (Y/N)"))
                            if vaksin == "Y":
                                print("Mohon maaf Anda belum dapat mengikuti program vaksinasi dikarenakan belum"
                                "memenuhi persyaratan kesehatan")
                            else:
                                pernyataan = ['1.Mengalami kesulitan saat menaiki anak tangga','2.Sering mengalami kelelahan',
                                      '3. Mengalami kesulitan saat berjalan 100-200 meter',
                                      '4. Adanya penurunan berat badan yang signifikan dalam satu tahun terakhir']
                                rose2 = 0
                                for win in range(0, 4):
                                      print(pernyataan[rose2])
                                      rose2 += 1
                            pernyataan2 = str(input("Apakah dari pernyataan di atas terdapat 2 atau lebih gejala yang Anda alami (Y/N)?"))
                            if pernyataan2=="Y":
                                print("Maaf Anda belum dapat mengikuti program vaksinasi dikarenakan belum memenuhi syarat kesehatan")
