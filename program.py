#memasukkan identitas
print("Selamat datang di Website Registrasi Vaksinasi COVID-19")
print("Mohon persiapkan data-data di bawah ini untuk keperluan registrasi:")
listdata = ['1. KTP','2. Surat kesehatan dari dokter bagi penderita penyakit kronis']

#menampilkan listdata keperluan
rose = 0
for win in range (0,2) :
    print (listdata[rose])
    rose+=1
konfir = str(input("Apakah semua data yang diperlukan sudah Anda siapkan? (Y/N):"))
konfir2 = konfir.title()

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
                            else:
                                kecamatan= str(input("Masukkan alamat Kecamatan Anda ="))
                            kecamatan1= kecamatan.title()
                            kecamatan2 = kecamatan.title()
                            kecamatan3 = kecamatan.title()
                            kecamatan4 = kecamatan.title()
                            if kecamatan1=="Laweyan":
                                rs1= ['1.RSUD Panti Waluyo','2.RSUD Kasih Ibu','3.RS JIH Surakarta','4.RSUP Surakarta',
                                      '5.RS Mata Solo','6. RSGM Sulastri','7.RS Onkologi Surakarta']
                                bunga1 = 0
                                for win in range(0, 7):
                                    print(rs1[bunga1])
                                    bunga1 += 1
                                print("Anda dapat melakukan vaksin di daftar rumah sakit tersebut")
                                rsmilih1= str(input("Masukkan nama rumah sakit yang Anda pilih="))
                                tvaksin1= str(input("Tanggal vaksin (dd/mm/yyyy)= "))

                                #output 1
                                print("Data Registrasi")
                                print("Nama Pasien:", nama2)
                                print("NIK:",nik)
                                print("Tempat Lahir:", tempat2)
                                print("Tanggal Lahir= ", tanggal, "/", bulan, "/", tahun)
                                print("Usia:", tahunusia, "Tahun")
                                print("Nama Ayah:", nama_ayah2)
                                print("Nama Ibu:", nama_ibu2)
                                print("Alamat:", kecamatan1)
                                print("Rumah Sakit Rujukan:", rsmilih1)
                                print("Tanggal Registrasi: ", tanggalregist, "/", bulanregist, "/", tahunregist)
                                print("Tanggal Vaksinasi:", tvaksin1)
                                
                            elif kecamatan2=="Jebres":
                                rs2= ['1.RSUD Dr.Moewardi','2.RSUD Oen Surakarta','3.RS Hermina','4.RSJP Surakarta']
                                bunga2 = 0
                                for win in range(0, 4):
                                    print(rs2[bunga2])
                                    bunga2 += 1
                                print("Anda dapat melakukan vaksin di daftar rumah sakit tersebut")
                                rsmilih2= str(input("Masukkan nama rumah sakit yang Anda pilih="))
                                tvaksin2 = str(input("Tanggal vaksin (dd/mm/yyyy)= "))                          

                                # output 2
                                print("Data Registrasi")
                                print("Nama Pasien:", nama2)
                                print("NIK:", nik)
                                print("Tempat Lahir:", tempat2)
                                print("Tanggal Lahir= ", tanggal, "/", bulan, "/", tahun)
                                print("Usia:", tahunusia, "Tahun")
                                print("Nama Ayah:", nama_ayah2)
                                print("Nama Ibu:", nama_ibu2)
                                print("Alamat:", kecamatan2)
                                print("Rumah Sakit Rujukan:", rsmilih2)
                                print("Tanggal Registrasi: ", tanggalregist, "/", bulanregist, "/", tahunregist)
                                print("Tanggal Vaksinasi:", tvaksin2)

                            elif kecamatan3=="Serengan":
                                rsmilih3= "RS Bung Karno"
                                print("Anda dapat melakukan vaksin di", rsmilih3)
                                tvaksin3 = str(input("Tanggal vaksin (dd/mm/yyyy)= "))

                                # output 3
                                print("Data Registrasi")
                                print("Nama Pasien:", nama2)
                                print("NIK:", nik)
                                print("Tempat Lahir:", tempat2)
                                print("Tanggal Lahir= ", tanggal, "/", bulan, "/", tahun)
                                print("Usia:", tahunusia, "Tahun")
                                print("Nama Ayah:", nama_ayah2)
                                print("Nama Ibu:", nama_ibu2)
                                print("Alamat:", kecamatan3)
                                print("Rumah Sakit Rujukan:", rsmilih3)
                                print("Tanggal Registrasi: ", tanggalregist, "/", bulanregist, "/", tahunregist)
                                print("Tanggal Vaksinasi:", tvaksin3)
                                
                            elif kecamatan4=="Banjarsari":
                                rs4= ['1.RSUD Kota Surakarta','2.RSUD Brayat Minulyo','3.RS PKU Muhammadiyah Surakarta',
                                      '4.RS Triharsi']
                                bunga4 = 0
                                for win in range(0, 4):
                                    print(rs4[bunga4])
                                    bunga4 += 1
                                print("Anda dapat melakukan vaksin di daftar rumah sakit tersebut")
                                rsmilih4= str(input("Masukkan nama rumah sakit yang Anda pilih="))
                                tvaksin4 = str(input("Tanggal vaksin (dd/mm/yyyy)= "))
                                               
                                # output 4
                                print("Data Registrasi")
                                print("Nama Pasien:", nama2)
                                print("NIK:", nik)
                                print("Tempat Lahir:", tempat2)
                                print("Tanggal Lahir= ", tanggal, "/", bulan, "/", tahun)
                                print("Usia:", tahunusia, "Tahun")
                                print("Nama Ayah:", nama_ayah2)
                                print("Nama Ibu:", nama_ibu2)
                                print("Alamat:", kecamatan4)
                                print("Rumah Sakit Rujukan:", rsmilih4)
                                print("Tanggal Registrasi: ", tanggalregist, "/", bulanregist, "/", tahunregist)
                                print("Tanggal Vaksinasi:", tvaksin4)

                            else:
                                rs5 = ['1.RSUD Bung Karno', '2.RS Kustati','3.RS PKU Sampangan']
                                bunga5 = 0
                                for win in range(0, 3):
                                    print(rs5[bunga5])
                                    bunga5 += 1
                                print("Anda dapat melakukan vaksin di daftar rumah sakit tersebut")
                                rsmilih5 = str(input("Masukkan nama rumah sakit yang Anda pilih="))
                                tvaksin5 = str(input("Tanggal vaksin (dd/mm/yyyy)= "))

                                # output 5
                                print("Data Registrasi")
                                print("Nama Pasien:", nama2)
                                print("NIK:", nik)
                                print("Tempat Lahir:", tempat2)
                                print("Tanggal Lahir= ", tanggal, "/", bulan, "/", tahun)
                                print("Usia:", tahunusia, "Tahun")
                                print("Nama Ayah:", nama_ayah2)
                                print("Nama Ibu:", nama_ibu2)
                                print("Alamat: Pasar Kliwon")
                                print("Rumah Sakit Rujukan:", rsmilih5)
                                print("Tanggal Registrasi: ", tanggalregist, "/", bulanregist, "/", tahunregist)
                                print("Tanggal Vaksinasi:", tvaksin5)


    else:
        print("Maaf Anda belum dapat mengikuti program vaksinasi dikarenakan usia Anda belum mencukupi / masih di bawah 18 tahun")
else:
    print("Mohon persiapkan dahulu seluruh data yang diperlukan!")

                                
