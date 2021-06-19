# import modul
import datetime

# memasukkan identitas
print("Selamat datang di Website Registrasi Vaksinasi COVID-19")
print("Mohon persiapkan data-data di bawah ini untuk keperluan registrasi:")
listdata = ['1. KTP','2. Surat kesehatan dari dokter bagi penderita penyakit kronis']

# menampilkan listdata keperluan
keperluan = 0
for syarat in range (0,2) :
    print (listdata[keperluan])
    keperluan+=1
konfir = str(input("Apakah semua data yang diperlukan sudah Anda siapkan? (Y/N):"))
konfir2 = konfir.title()

# Mengisi identitas 
if konfir2=="Y" :
    print("Silakan mengisi identitas Anda dengan seksama dan jawablah pertanyaan sesuai dengan kondisi Anda saat ini")
    nama = str(input("Nama Lengkap="))
    nama2 = nama.title()

    nik = int(input("NIK="))

    nama_ayah= str(input("Nama Ayah="))
    nama_ayah2= nama_ayah.title()

    nama_ibu= str(input("Nama Ibu="))
    nama_ibu2= nama_ibu.title()
    
    print("Kelahiran:")
    tempat= str(input("Tempat Lahir="))
    tempat2= tempat.title()
    
    # Menghitung usia pengguna
    cllahir, clregistrasi = 0, 0

    # Input tanggal lahir
    while cllahir == 0:
        try:
            tanggal = str(input("Tanggal Lahir (dd mm yyyy) : "))
            tgl1, bln1, thn1 = tanggal.split(" ")
            ustanggal = datetime.date(int(thn1), int(bln1), int(tgl1))
        except:
            print("Harus berformat \"<hari> <bulan> <tahun>\"")
        else:
            lahir = f"{str(tgl1).zfill(2)}-{str(bln1).zfill(2)}-{thn1}"
            break
    
    # Input tanggal registrasi
   while clregistrasi == 0:
        try:
            tanggal1 = str(input("Tanggal Registrasi (dd mm yyyy) : "))
            tgl2, bln2, thn2 = tanggal1.split(" ")
            retanggal = datetime.date(int(thn2), int(bln2), int(tgl2))
        except:
            print("Harus berformat \"<hari> <bulan> <tahun>\"")
        else:
            registrasi = f"{str(tgl2).zfill(2)}-{str(bln2).zfill(2)}-{thn2}"
            break

    # Program menghitung usia
    usia = retanggal - ustanggal
    usia2 = (usia.days)
    usia3 = round((usia2 / 365),2)
    print("Usia :", usia3, "tahun")
    
    # Persyaratan vaksinasi
    # Syarat usia
    if usia3 >= 18:
        jk = str(input("Jenis Kelamin (P/L)="))
        jk2 = jk.title()
        
        # Syarat untuk perempuan
        if jk2 =="P":
            mengandung= str(input("Apakah anda sedang mengandung (Y/N)?"))
            mengandung2 = mengandung.title()
            if mengandung2=="Y":
                    print("Maaf anda belum dapat mengikuti program vaksinasi dikarenakan sedang mengandung")
        
        # Syarat riwayat covid-19
        terpapar = str(input("Apakah Anda pernah terpapar covid dalam jangka waktu 3 bulan terakhir?(Y/N)"))
        terpapar2 = terpapar.title()
        if terpapar2 == "Y":
            print("Maaf Anda belum dapat mengikuti program vaksinansi dikarenakan belum memenuhi persyaratan kesehatan")
        
        # Syarat riwayat penyakit kronis
        else:     
            riwayatsakit = str(input("Apakah Anda memiliki riwayat hipertensi atau penyakit kronis lain?(Y/N)"))
            riwayatsakit2 = riwayatsakit.title()
            if riwayatsakit2 == "Y":
                suratizin = str(input("Apakah Anda sudah mendapat surat layak vaksin dari dokter?(Y/N)"))
                suratizin2 = suratizin.title()
                if suratizin2 == "N":
                            print("Mohon maaf Anda belum dapat mengikuti program vaksinasi dikarenakan belum"
                                              "memenuhi persyaratan kesehatan")
            
            # Syarat riwayat vaksin
            vaksin= str(input("Apakah anda menerima vaksin lain dalam kurun waktu 1 bulan terakhir? (Y/N)"))
            vaksin2 = vaksin.title()
            if vaksin2 == "Y":
                print("Mohon maaf Anda belum dapat mengikuti program vaksinasi dikarenakan belum"
                                "memenuhi persyaratan kesehatan")
            
            # Persyaratan khusus
            else:
                pernyataan = ['1. Mengalami kesulitan saat menaiki anak tangga','2. Sering mengalami kelelahan',
                              '3. Mengalami kesulitan saat berjalan 100-200 meter',
                              '4. Adanya penurunan berat badan yang signifikan dalam satu tahun terakhir']
                Persyaratan_khusus = 0
                for syarat in range(0, 4):
                    print(pernyataan[Persyaratan_khusus])
                    Persyaratan_khusus += 1
                            
                pernyataan2 = str(input("Apakah dari pernyataan di atas terdapat 2 atau lebih gejala yang Anda alami (Y/N)?"))
                pernyataan3 = pernyataan2.title()
                if pernyataan3=="Y":
                    print("Maaf Anda belum dapat mengikuti program vaksinasi dikarenakan belum memenuhi syarat kesehatan")
                
                # Memasukkan kecamatan tempat tinggal
                else:
                    listkecamatan = ['1. Jebres','2. Laweyan', '3. Banjarsari', '4. Serengan','5. Pasar Kliwon']
                    kecamatan_solo = 0
                    for wilayah in range(0, 5):
                        print(listkecamatan[matahari])
                        kecamatan_solo += 1
                    kecamatan= str(input("Masukkan alamat Kecamatan Anda ="))
                kecamatan1 = kecamatan.title()
                kecamatan2 = kecamatan.title()
                kecamatan3 = kecamatan.title()
                kecamatan4 = kecamatan.title()
                kecamatan5 = kecamatan.title()
                
                # Memilih rumah sakit di kecamatan Laweyan
                if kecamatan1=="Laweyan":
                            rs1= ['1.RSUD Panti Waluyo','2.RSUD Kasih Ibu','3.RS JIH Surakarta','4.RSUP Surakarta',
                                      '5.RS Mata Solo','6. RSGM Sulastri','7.RS Onkologi Surakarta']
                            daftar1 = 0
                            for rs_solo1 in range(0, 7):
                                print(rs1[bunga1])
                                daftar1 += 1
                            print("Anda dapat melakukan vaksin di daftar rumah sakit tersebut")
                            rsmilih1= str(input("Masukkan nama rumah sakit yang Anda pilih="))
                            tvaksin = str("Anda akan divaksinasi 7 hari setelah registarsi. Mohon cek kalender dengan seksama")

                            # output 1
                            print("==========Data Registrasi==========")
                            print("Nama Pasien:", nama2)
                            print("NIK:", nik)
                            print("Tempat Lahir:", tempat2)
                            print("Tanggal Lahir= ", lahir)
                            print("Usia:", usia3, "Tahun")
                            print("Nama Ayah:", nama_ayah2)
                            print("Nama Ibu:", nama_ibu2)
                            print("Alamat:", kecamatan1)
                            print("Rumah Sakit Rujukan:", rsmilih1)
                            print("Tanggal Registrasi: ", registrasi)
                            print("Tanggal Vaksinasi:", tvaksin)

                            # save database
                            # format teks
                            teks ="\nNama Pasien: {}\nNIK: {}\nTempat Lahir: {}\nTanggal Lahir: {}\nUsia: {}\nNama Ayah: {}\nNama Ibu: {}\nAlamat: {}\nRS Rujukan: {}\nTanggal Registrasi: {}\nTanggal Vaksinasi {}\n----------".format(nama2,nik,tempat2,lahir,usia3,nama_ayah2, nama_ibu2, kecamatan1,rsmilih1, registrasi, tvaksin)

                            # buka file
                            file_data = open("database.txt", "a")

                            # tulis teks
                            file_data.write(teks)

                            # tutup file
                            file_data.close()

                # Memilih rumah sakit di kecamatan Jebres
                elif kecamatan2=="Jebres":
                            rs2= ['1.RSUD Dr.Moewardi','2.RSUD Oen Surakarta','3.RS Hermina','4.RSJP Surakarta']
                            daftar2 = 0
                            for rs_solo2 in range(0, 4):
                                print(rs2[bunga2])
                                daftar2 += 1
                            print("Anda dapat melakukan vaksin di daftar rumah sakit tersebut")
                            rsmilih2= str(input("Masukkan nama rumah sakit yang Anda pilih="))
                            tvaksin = str("Anda akan divaksinasi 7 hari setelah registarsi. Mohon cek kalender dengan seksama")

                            # output 2
                            print("==========Data Registrasi==========")
                            print("Nama Pasien:", nama2)
                            print("NIK:", nik)
                            print("Tempat Lahir:", tempat2)
                            print("Tanggal Lahir= ", lahir)
                            print("Usia:", usia3, "Tahun")
                            print("Nama Ayah:", nama_ayah2)
                            print("Nama Ibu:", nama_ibu2)
                            print("Alamat:", kecamatan2)
                            print("Rumah Sakit Rujukan:", rsmilih2)
                            print("Tanggal Registrasi: ", registrasi)
                            print("Tanggal Vaksinasi:", tvaksin)

                            # save database
                            # format teks
                            teks = "\nNama Pasien: {}\nNIK: {}\nTempat Lahir: {}\nTanggal Lahir: {}\nUsia: {}\nNama Ayah: {}\nNama Ibu: {}\nAlamat: {}\nRS Rujukan: {}\nTanggal Registrasi: {}\nTanggal Vaksinasi: {}\n----------".format(
                                nama2, nik, tempat2, lahir, usia3, nama_ayah2, nama_ibu2, kecamatan2, rsmilih2,
                                registrasi, tvaksin)

                            # buka file
                            file_data = open("database.txt", "a")

                            # tulis teks
                            file_data.write(teks)

                            # tutup file
                            file_data.close()

                # Memilih rumah sakit di kecamatan Serengan
                elif kecamatan3=="Serengan":
                            rsmilih3= "RS Bung Karno"
                            print("Anda dapat melakukan vaksin di", rsmilih3)
                            tvaksin = str("Anda akan divaksinasi 7 hari setelah registarsi. Mohon cek kalender dengan seksama")

                            # output 3
                            print("==========Data Registrasi==========")
                            print("Nama Pasien:", nama2)
                            print("NIK:", nik)
                            print("Tempat Lahir:", tempat2)
                            print("Tanggal Lahir= ", lahir)
                            print("Usia:", usia3, "Tahun")
                            print("Nama Ayah:", nama_ayah2)
                            print("Nama Ibu:", nama_ibu2)
                            print("Alamat:", kecamatan3)
                            print("Rumah Sakit Rujukan:", rsmilih3)
                            print("Tanggal Registrasi: ", registrasi)
                            print("Tanggal Vaksinasi:", tvaksin)

                            # save database
                            # format teks
                            teks = "\nNama Pasien: {}\nNIK: {}\nTempat Lahir: {}\nTanggal Lahir: {}\nUsia: {}\nNama Ayah: {}\nNama Ibu: {}\nAlamat: {}\nRS Rujukan: {}\nTanggal Registrasi: {}\nTanggal Vaksinasi: {}\n----------".format(
                                nama2, nik, tempat2, lahir, usia3, nama_ayah2, nama_ibu2, kecamatan3, rsmilih3,
                                registrasi, tvaksin)

                            # buka file
                            file_data = open("database.txt", "a")

                            # tulis teks
                            file_data.write(teks)

                            # tutup file
                            file_data.close()

                # Memilih rumah sakit di kecamatan Banjarsari
                elif kecamatan4=="Banjarsari":
                            rs4= ['1.RSUD Kota Surakarta','2.RSUD Brayat Minulyo','3.RS PKU Muhammadiyah Surakarta',
                                      '4.RS Triharsi']
                            daftar4 = 0
                            for rs_solo4 in range(0, 4):
                                print(rs4[daftar4])
                                daftar4 += 1
                            print("Anda dapat melakukan vaksin di daftar rumah sakit tersebut")
                            rsmilih4= str(input("Masukkan nama rumah sakit yang Anda pilih="))
                            tvaksin = str("Anda akan divaksinasi 7 hari setelah registarsi. Mohon cek kalender dengan seksama")

                            # output 4
                            print("==========Data Registrasi==========")
                            print("Nama Pasien:", nama2)
                            print("NIK:", nik)
                            print("Tempat Lahir:", tempat2)
                            print("Tanggal Lahir= ",lahir)
                            print("Usia:", usia3, "Tahun")
                            print("Nama Ayah:", nama_ayah2)
                            print("Nama Ibu:", nama_ibu2)
                            print("Alamat:", kecamatan4)
                            print("Rumah Sakit Rujukan:", rsmilih4)
                            print("Tanggal Registrasi: ",registrasi)
                            print("Tanggal Vaksinasi:", tvaksin)

                            # save database
                            # format teks
                            teks = "\nNama Pasien: {}\nNIK: {}\nTempat Lahir: {}\nTanggal Lahir: {}\nUsia: {}\nNama Ayah: {}\nNama Ibu: {}\nAlamat: {}\nRS Rujukan: {}\nTanggal Registrasi: {}\nTanggal Vaksinasi: {}\n----------".format(
                                nama2, nik, tempat2, lahir, usia3, nama_ayah2, nama_ibu2, kecamatan4, rsmilih4,
                                registrasi, tvaksin)

                            # buka file
                            file_data = open("database.txt", "a")
                            
                            # tulis teks
                            file_data.write(teks)

                            # tutup file
                            file_data.close()
                                
                # Memilih rumah sakit di kecamatan Pasar Kliwon
                elif kecamatan5 == "Pasar Kliwon":
                    rs5 = ['1.RSUD Bung Karno', '2.RS Kustati', '3.RS PKU Sampangan']
                    daftar5 = 0
                    for rs_solo5 in range(0, 3):
                        print(rs5[daftar5])
                        daftar5 += 1
                    print("Anda dapat melakukan vaksin di daftar rumah sakit tersebut")
                    rsmilih5 = str(input("Masukkan nama rumah sakit yang Anda pilih="))
                    tvaksin = str("Anda akan divaksinasi 7 hari setelah registarsi. Mohon cek kalender dengan seksama")

                    # output 5
                    print("===========Data Registrasi==========")
                    print("Nama Pasien:", nama2)
                    print("NIK:", nik)
                    print("Tempat Lahir:", tempat2)
                    print("Tanggal Lahir= ", lahir)
                    print("Usia:", usia3, "Tahun")
                    print("Nama Ayah:", nama_ayah2)
                    print("Nama Ibu:", nama_ibu2)
                    print("Alamat: Pasar Kliwon")
                    print("Rumah Sakit Rujukan:", rsmilih5)
                    print("Tanggal Registrasi: ", registrasi)
                    print("Tanggal Vaksinasi:", tvaksin)

                    # Save Database
                    # format teks
                    teks = "\nNama Pasien: {}\nNIK: {}\nTempat Lahir: {}\nTanggal Lahir: {}\nUsia: {}\nNama Ayah: " \
                           "{}\nNama Ibu: {}\nAlamat: {}\nRS Rujukan: {}\nTanggal Registrasi: {}\nTanggal Vaksinasi: " \
                           "{}\n----------".format(nama2, nik, tempat2, lahir, usia3, nama_ayah2, nama_ibu2, kecamatan5,
                                                   rsmilih5, registrasi, tvaksin)
                    # save database
                    # buka file
                    file_data = open("database.txt", "a")

                    # tulis teks
                    file_data.write(teks)

                    # tutup file
                    file_data.close()

                # Jika kecamatan tidak valid
                else:
                    print("Kecamatan yang dimasukkan tidak valid, mohon ulang program kembali.")
    else:
        print("Maaf Anda belum dapat mengikuti program vaksinasi dikarenakan usia Anda belum mencukupi / masih di bawah 18 tahun")
else:
    print("Mohon persiapkan dahulu seluruh data yang diperlukan!")

                                
