#memasukkan identitas
print("Selamat datang di Website Registrasi Vaksinasi COVID-19")
print("Mohon persiapkan data-data di bawah ini untuk keperluan registrasi:")
listdata = ['1. KTP','2. Surat kesehatan dari dokter bagi penderita penyakit kronis']

#menampilkan listdata keperluan
rose = 0
for win in range (0,2) :
    print (listdata[rose])
    rose+=1
konfirmasi: str(input("Apakah semua data yang diperlukan sudah Anda siapkan? (Sudah/Belum):"))

if konfirmasi=="Sudah":
    print("Silakan mengisi identitas Anda dengan seksama dan jawablah pertanyaan sesuai dengan kondisi Anda saat ini")
else:
    print("Mohon persiapkan dahulu seluruh data yang diperlukan!")
