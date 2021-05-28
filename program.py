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
